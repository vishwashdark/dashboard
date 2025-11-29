🛡️ Aegis TrustEngine Dashboard
A Multi-Agent Forensic Auditing System for AdTech & Influencer Marketing

The Aegis TrustEngine is a forensic auditing dashboard for brands, agencies, and compliance teams. It detects deepfakes, analyzes influencer credibility, and measures financial & reputational risk using a Zero-Tolerance Multi-Agent Swarm.

🧠 The Intelligence Pipeline

Data flows through a multi-stage pipeline designed to eliminate high-risk content before it reaches the brand.

Mermaid diagram (paste directly into your .md):

graph TD
    A[Social Platforms Input] --> B[Vision Model / OpenCV]
    B --> C[OpenAI Moderation]
    C --> D[CLIP Alignment]
    D --> E[Gemini Multimodal AI + Google Search]
    E --> F{Multi-Agent Layer}
    F --> G[Authenticity Agent]
    F --> H[Safety Agent]
    F --> I[Compliance Agent]
    F --> J[Trust Agent]
    G & H & I & J --> K[Reporting & Analytics]

🤖 The Agent Swarm (Personas)

Multi-agent personas designed with cynical, brand-protective prompt engineering.

1. 🦈 The Deal Architect — “Shark Tank Investor”

Role: Financial structure & negotiation
Logic: Evaluates efficiency ratio of Followers vs Revenue

Behavior

Devaluation: Low revenue vs high followers → assumes botting

Lowballing: Protects brand P&L, not influencer ego

Skeptical: Treats all metrics as inflated until proven real

2. 🕵️‍♀️ The Forensic Analyst — “Zero Tolerance”

Role: Deepfake detection
Policy: Flags ANY content with even a 1% likelihood of AI involvement

Detection Vectors

Skin smoothness / lack of pores

Eye/teeth artifacts

Background distortions

Incorrect anatomy

3. ⚖️ The Risk Auditor

Role: Toxicity, fraud, and safety auditing

Logic

Generic content + high followers = bot suspicion

Safe to Collaborate = FALSE unless profile is flawless

Toxicity detection in comments, captions, patterns

4. 🐝 The Compliance Swarm

A 4-node cluster enforcing strict brand safety & regulatory rules.

Nodes

Authenticity Agent: Deepfake inspection

Safety Agent: Detects political/violent/aggressive cues

Compliance Agent: Flags absolute marketing claims

Trust Agent: Detects spammy/cheap aesthetics; evaluates brand fit

📂 Project Structure
dashboard/
├── app.py                 # Main application logic & API routes
├── mcp.py                 # Model Context Protocol / AI helper functions
├── insert_data.py         # Database seeding script
├── requirements.txt        # Python dependencies
├── .env                    # API configuration
│
├── static/
│   ├── style/             # CSS files
│   └── uploads/           # Temporary image storage
│
├── templates/
│   ├── index.html         # Landing page
│   ├── login.html         # Authentication
│   ├── dashboard.html     # Main dashboard
│   ├── adtech.html        # Ad creative audit
│   ├── influencer.html    # Influencer risk analysis
│   ├── enterprise.html    # C-Suite view
│   └── console.html       # Admin console
│
└── __pycache__/           # Compiled Python files

🚀 Setup & Installation
Prerequisites

Python 3.8+

MongoDB Atlas

Gemini API Key

1. Clone & Install
git clone <repo-url>
cd dashboard
pip install -r requirements.txt

2. Configure Environment

Create .env:

GEMINI_API_KEY=your_key_here
MONGO_URI=your_mongodb_connection_string
FLASK_SECRET=your_secret_key

3. Seed Database
python insert_data.py

4. Run Application
python app.py


Access at:

http://localhost:5000

🛠️ Tech Stack
Layer	Stack
Backend	Python, Flask
AI Models	Gemini 2.0 Flash, OpenAI Moderation, CLIP
Computer Vision	OpenCV, PIL, NumPy
Database	MongoDB
Frontend	HTML5, CSS3
