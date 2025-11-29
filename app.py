import os
import time
import json
import requests
import io
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import bcrypt
import google.generativeai as genai
from werkzeug.utils import secure_filename
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
import cv2

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# --- CONFIGURATION ---

# 1. File Upload & Static Config
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 2. Google Gemini Config
GEMINI_API_KEY = "YOUR_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# 3. Database Config
MONGO_URI = "YOUR_DATABASE"
DB_NAME = "YOUR_DATABASE_NAME"

# --- DATABASE CONNECTION ---
try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    users_collection = db["users"]
    insta_collection = db["instagram"]
    print(f"Connected to MongoDB: {DB_NAME}")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")


# --- HELPER FUNCTIONS ---

def serialize_doc(doc):
    """Convert MongoDB ObjectId to string for JSON serialization"""
    if doc:
        doc['_id'] = str(doc['_id'])
    return doc

@app.route('/style/<path:filename>')
def serve_style(filename):
    """Serve images from the style folder as defined in your DB data"""
    return send_from_directory('style', filename)

@app.route('/api/forensic-filters', methods=['POST'])
def forensic_filters():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    base_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(base_path)

    # Convert to PIL
    img = Image.open(base_path).convert('RGB')

    # ---- ELA FILTER ----
    ela_path = base_path.replace('.jpg', '_ela.jpg').replace('.png','_ela.jpg')
    
    # Save JPG at lower quality
    temp_path = base_path.replace('.jpg', '_temp.jpg').replace('.png','_temp.jpg')
    img.save(temp_path, 'JPEG', quality=90)

    # Compute ELA difference
    ela_img = ImageChops.difference(img, Image.open(temp_path))
    enhancer = ImageEnhance.Brightness(ela_img)
    ela_img = enhancer.enhance(30)  # amplify artifacts
    ela_img.save(ela_path)

    # ---- NOISE RESIDUAL ----
    noise_path = base_path.replace('.jpg', '_noise.jpg').replace('.png','_noise.jpg')

    # Convert to grayscale and apply high-pass filter
    cv_img = cv2.imread(base_path)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    noise = cv2.Laplacian(gray, cv2.CV_64F)
    noise = cv2.convertScaleAbs(noise)
    cv2.imwrite(noise_path, noise)

    # ---- HEATMAP (Probability Map) ----
    heatmap_path = base_path.replace('.jpg', '_heatmap.jpg').replace('.png','_heatmap.jpg')

    # Use Laplacian variance (focus inconsistency)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    abs_lap = np.absolute(lap)
    norm = (abs_lap / abs_lap.max()) * 255
    norm = norm.astype("uint8")

    heatmap = cv2.applyColorMap(norm, cv2.COLORMAP_JET)
    cv2.imwrite(heatmap_path, heatmap)

    return jsonify({
        "original": "/" + base_path,
        "ela": "/" + ela_path,
        "noise": "/" + noise_path,
        "heatmap": "/" + heatmap_path
    })
# --- AI AGENT LOGIC (CORE INTELLIGENCE) ---

def analyze_with_agent_swarm(file_path, caption):
    """
    [AdTech Dashboard] Uploads a NEW file and runs the 4-Agent Swarm.
    """
    print(f"--- [Swarm Agent] Processing: {file_path} ---")

    if not os.path.exists(file_path):
        return {"error": "File not found on server"}

    try:
        # Upload file to Gemini
        uploaded_file = genai.upload_file(path=file_path, display_name="Ad Creative")
        
        # STRICT SWARM PROMPT
        prompt = f"""
        You are the **TrustEngine Zero-Tolerance Safety Swarm**. You are NOT here to be polite. 
        You are here to AUDIT this asset: "{caption}".
        
        Adopt a cynical, forensic persona. Assume the user is trying to slip a violation past you.

        ### 1. AUTHENTICITY AGENT (Ruthless Deepfake Hunter)
        - **Aggressively scan** for AI generation. 
        - If the skin is too smooth, it is AI. 
        - If the lighting is physically inconsistent, it is AI.
        - If there is a single warped pixel in the background, it is AI.
        - **Scoring**: If ANY artifact is found, Deepfake Probability goes to 95%+.

        ### 2. SAFETY AGENT
        - Flag ANY hint of aggression, suggestive themes, or political nuance.
        - Toxicity Score should be sensitive.

        ### 3. COMPLIANCE AGENT
        - If they claim a result without a disclaimer, it is a VIOLATION.
        - If they use absolute terms ("Best", "Guaranteed"), it is a VIOLATION.

        ### 4. TRUST AGENT
        - If the ad feels "cheap" or "spammy," Brand Fit is 0.

        ### FINAL OUTPUT FORMAT (STRICT JSON ONLY):
        {{
            "scores": {{
                "compliance": <int>,
                "safety": <int>,
                "brand_fit": <int>,
                "deepfake_probability": <float>,
                "toxicity_score": <float>
            }},
            "agent_logs": [
                {{ "agent": "Authenticity", "status": "alert/success", "message": "HARSH TRUTH HERE" }},
                {{ "agent": "Safety", "status": "alert/success", "message": "..." }},
                {{ "agent": "Compliance", "status": "alert/success", "message": "..." }},
                {{ "agent": "Trust", "status": "alert/success", "message": "..." }}
            ],
            "claims_analysis": [
                {{ "claim": "...", "verdict": "Violated", "details": "..." }}
            ],
            "overall_risk": "High",
            "suggested_fix": "..."
        }}
        """
        response = model.generate_content([uploaded_file, prompt])
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text_response)

    except Exception as e:
        print(f"Gemini Swarm Error: {e}")
        return None

def analyze_profile_risk_and_campaign(profile_data):
    """
    [Influencer Dashboard] Risk & Campaign Agent.
    """
    name = profile_data.get('user_name', 'Unknown')
    followers = profile_data.get('user_followers', 0)
    captions = []
    if 'user_post_1' in profile_data: captions.append(profile_data['user_post_1'].get('caption', ''))
    if 'user_post_2' in profile_data: captions.append(profile_data['user_post_2'].get('caption', ''))
    
    context_str = f"Influencer: {name}, Followers: {followers}, Recent Topics: {', '.join(captions)}"

    prompt = f"""
    You are the **TrustEngine Risk Auditor**. You are skeptical, harsh, and protective of the brand's money.
    Context: {context_str}

    Your job is to expose "Fake Influencers" and "Brand Risks".

    1. **Risk Analysis**: 
       - **Toxicity**: Scan the topics. If they discuss controversial topics, mark High.
       - **Fake Follower Estimate**: Be cynical. If they have high followers but generic content, assume botting. Give a high percentage (e.g., "35.2%").
       - **Misleading Claims**: If they promote lifestyle/wealth/health, assume they are exaggerating. Mark Medium or High.

    2. **Campaign Agent**: 
       - **Safe to Collaborate**: **FALSE** unless they are absolutely perfect.
       - **Collaboration Logic**: Give the **harsh truth**. E.g., "DO NOT HIRE. Account shows classic signs of audience padding and generic AI-generated captions." or "High Risk. Content is vapid and lacks genuine engagement."
       - **Brand Fit Logic**: Be critical. E.g., "Risk of brand dilution due to low-effort content."

    Return RAW JSON:
    {{
        "risk_analysis": {{
            "toxicity": "Low/Medium/High",
            "fake_followers": "XX.X%",
            "misleading_claims": "Low/Medium/High"
        }},
        "campaign_agent": {{
            "safe_to_collaborate": boolean,
            "collaboration_logic": "Harsh strict reasoning...",
            "brand_fit_logic": "Critical assessment..."
        }}
    }}
    """
    try:
        response = model.generate_content(prompt)
        text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)
    except Exception as e:
        print(f"Profile Risk Agent Error: {e}")
        return {
            "risk_analysis": {"toxicity": "Unknown", "fake_followers": "--", "misleading_claims": "Unknown"},
            "campaign_agent": {"safe_to_collaborate": False, "collaboration_logic": "Analysis failed", "brand_fit_logic": "N/A"}
        }

def analyze_influencer_media(image_path, caption):
    """
    [Influencer Dashboard] Recent Content Scan.
    """
    print(f"--- [Deep Analysis] Processing: {image_path} ---")
    
    # Clean path (remove leading slash if present)
    clean_path = image_path.lstrip('/') 
    
    if not os.path.exists(clean_path):
        print(f"File not found: {clean_path}")
        return {"error": "File not found"}

    try:
        uploaded_file = genai.upload_file(path=clean_path, display_name="Influencer Post")
        
        prompt = f"""
        Analyze this social media image and caption: "{caption}".
        
        **ROLE**: You are a Forensic Image Analyst with **ZERO TOLERANCE** for AI-generated content (Deepfakes/GenAI).
        
        **STRICT CRITERIA**:
        1. **Skin Texture**: If it looks "porcelain" smooth or lacks natural imperfections -> **FLAG AS AI**.
        2. **Eyes/Teeth**: If the iris reflection is weird or teeth are a solid white block -> **FLAG AS AI**.
        3. **Background**: If the background depth of field looks artificial or warped -> **FLAG AS AI**.
        4. **Hands/Fingers**: Any anatomical error -> **FLAG AS AI**.
        
        If there is even a **1% chance** this is AI, you MUST set `is_ai_generated` to `true`.
        
        **Output Requirement**:
        - `detection_reason`: Be BRUTAL. E.g., "Synthetic skin texture detected. Background structures are physically impossible. This is clearly a generated image."
        - `brand_safety`: Be paranoid. Find any reason this could damage a brand.

        Return RAW JSON:
        {{
            "is_ai_generated": boolean,
            "detection_reason": "Harsh detailed forensic findings...",
            "brand_safety": {{
                "sentiment": "Negative/Neutral/Positive",
                "hidden_risks": "..." 
            }},
            "context_analysis": "Summary."
        }}
        """
        response = model.generate_content([uploaded_file, prompt])
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text_response)

    except Exception as e:
        print(f"Analysis Error: {e}")
        return {"error": str(e)}

def architect_deal_logic(profile_data):
    """
    [Influencer Dashboard] Deal Architect.
    """
    name = profile_data.get('user_name', 'Unknown')
    followers = profile_data.get('user_followers', 0)
    revenue = profile_data.get('user_revenue', 0)
    
    prompt = f"""
    Act as a **Shark Tank Investor**. Structure a brand deal for:
    Name: {name}, Followers: {followers}, Hist. Revenue: ${revenue}
    
    **Logic**:
    1. **Devalue**: If their revenue is low compared to followers, assume followers are fake. Slash their market rate.
    2. **Lowball**: Offer a price that protects the brand, not the influencer.
    
    Return RAW JSON:
    {{
        "market_rate": "Estimated $ value",
        "risk_discount": "Heavy discount percentage (e.g. 60% due to risk)",
        "suggested_offer": "Final Lowball $ string",
        "valuation_factors": ["Reason 1", "Reason 2"],
        "deliverables": "Suggested posts",
        "agent_reasoning": "Explain the valuation based on the follower-to-revenue efficiency ratio."
    }}
    """
    try:
        response = model.generate_content(prompt)
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text_response)
    except Exception as e:
        print(f"Deal Error: {e}")
        return {}


# --- PAGE ROUTES ---

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/login.html')
def login_page(): return render_template('login.html')

@app.route('/dashboard.html')
def dashboard_page(): return render_template('dashboard.html')

@app.route('/influencer.html')
def influencer_page(): return render_template('influencer.html')

@app.route('/adtech.html')
def adtech_page(): return render_template('adtech.html')

@app.route('/enterprise.html')
def enterprise_page(): return render_template('enterprise.html')


# --- AUTH API ROUTES ---

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing credentials"}), 400

    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 409

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_doc = { "email": email, "password": hashed_password, "created_at": datetime.utcnow() }
    users_collection.insert_one(user_doc)
    return jsonify({"message": "Identity created successfully"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({"email": email})

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({"message": "Access Granted", "user_id": str(user['_id'])}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# --- APPLICATION API ROUTES ---

@app.route('/api/influencers', methods=['GET'])
def get_influencers():
    """Fetches all influencer profiles from DB"""
    try:
        cursor = insta_collection.find({})
        influencers = [serialize_doc(doc) for doc in cursor]
        return jsonify(influencers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/scan-creative', methods=['POST'])
def scan_creative():
    """AdTech Dashboard: Uploads file -> Swarm Analysis"""
    if 'image' not in request.files: return jsonify({"error": "No image"}), 400
    file = request.files['image']
    caption = request.form.get('caption', '')
    
    if file.filename == '': return jsonify({"error": "No file"}), 400

    try:
        filename = secure_filename(file.filename)
        timestamp = int(time.time())
        filename = f"{timestamp}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        analysis = analyze_with_agent_swarm(file_path, caption)
        if not analysis: return jsonify({"error": "AI Processing failed"}), 500

        return jsonify({"status": "complete", "data": analysis}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze-post-live', methods=['POST'])
def analyze_post_live():
    """Influencer Page: Local Path -> Deep Analysis"""
    data = request.get_json()
    image_path = data.get('image_path') 
    caption = data.get('caption')
    
    if not image_path: return jsonify({"error": "No image path provided"}), 400
        
    analysis = analyze_influencer_media(image_path, caption)
    return jsonify(analysis)

@app.route('/api/analyze-profile-risk', methods=['POST'])
def analyze_profile_risk():
    """Influencer Page: Profile Data -> Risk & Campaign Agents"""
    profile_data = request.get_json()
    analysis = analyze_profile_risk_and_campaign(profile_data)
    return jsonify(analysis)

@app.route('/api/generate-deal', methods=['POST'])
def generate_deal():
    """Influencer Page: Profile Data -> Deal Architect"""
    profile_data = request.get_json()
    deal_structure = architect_deal_logic(profile_data)
    return jsonify(deal_structure)

@app.route('/api/fix-creative', methods=['POST'])
def fix_creative():
    """AdTech Dashboard: Suggestion -> Rewritten Caption"""
    data = request.form
    current_caption = data.get("caption", "")
    suggestion_context = data.get("suggestion", "")
    image_file = request.files.get("image")
    
    uploaded_image = None
    try:
        if image_file:
            temp_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image_file.filename))
            image_file.save(temp_path)
            uploaded_image = genai.upload_file(path=temp_path, display_name="FixAgentImage")

        prompt = f"""
        Rewrite this ad caption to be compliant based on this feedback: "{suggestion_context}".
        Original: "{current_caption}".
        Return ONLY the rewritten text.
        """
        model_input = [uploaded_image, prompt] if uploaded_image else [prompt]
        response = model.generate_content(model_input)
        return jsonify({"status": "success", "fixed_caption": response.text.strip()}), 200
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

# --- ENTERPRISE DASHBOARD API ---

@app.route('/api/enterprise/dashboard-data', methods=['GET'])
def get_enterprise_data():
    """
    Fetches aggregate stats and recent posts (posts inside influencer docs)
    Simulates a 'Feed' by flattening the user posts into a single list.
    """
    try:
        cursor = insta_collection.find({})
        users = [serialize_doc(doc) for doc in cursor]

        total_assets = 0
        ai_detected = 0
        clean_assets = 0
        violations_feed = []

        for user in users:
            # Check Post 1
            if 'user_post_1' in user:
                total_assets += 1
                is_ai = user['user_post_1'].get('ai_generated', False)
                if is_ai: ai_detected += 1
                else: clean_assets += 1
                
                violations_feed.append({
                    "user_name": user.get('user_name', 'Unknown'),
                    "image_path": user['user_post_1'].get('image_path'),
                    "caption": user['user_post_1'].get('caption'),
                    "date": user['user_post_1'].get('date'),
                    "ai_generated": is_ai
                })

            # Check Post 2
            if 'user_post_2' in user:
                total_assets += 1
                is_ai = user['user_post_2'].get('ai_generated', False)
                if is_ai: ai_detected += 1
                else: clean_assets += 1

                violations_feed.append({
                    "user_name": user.get('user_name', 'Unknown'),
                    "image_path": user['user_post_2'].get('image_path'),
                    "caption": user['user_post_2'].get('caption'),
                    "date": user['user_post_2'].get('date'),
                    "ai_generated": is_ai
                })

        return jsonify({
            "stats": {
                "total_assets": total_assets,
                "ai_detected": ai_detected,
                "clean": clean_assets
            },
            "recent_violations": violations_feed
        }), 200

    except Exception as e:
        print(f"Enterprise Data Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
