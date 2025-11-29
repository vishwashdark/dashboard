🛡️ Aegis TrustEngine Dashboard

A Multi-Agent Forensic Auditing System for AdTech & Influencer Marketing

The Aegis TrustEngine is a sophisticated dashboard designed to audit digital assets, detect deepfakes, and calculate financial risk. It employs a "Zero-Tolerance" multi-agent swarm to analyze social media inputs through a rigorous pipeline of computer vision, multimodal AI, and strict compliance logic.

🧠 The Intelligence Pipeline

Data flows through a multi-stage analysis pipeline designed to filter out high-risk content before it reaches the brand.

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

This system utilizes prompt engineering to create distinct, cynical, and protective personas for its AI agents.

1. 🦈 The Deal Architect ("Shark Tank Investor")

Role: Financial structure & Negotiation.

Logic: Analyzes the efficiency ratio between Followers and Historical Revenue.

Behavior:

Devaluation: If revenue is low compared to followers, it assumes botting and slashes the market rate.

Lowballing: Generates offers designed to protect the brand's P&L, not the influencer's ego.

2. 🕵️‍♀️ The Forensic Analyst ("Zero Tolerance")

Role: Deepfake & GenAI Detection.

Criteria: Flags assets if there is even a 1% chance of AI generation.

Detection Vectors:

Skin: "Porcelain" smoothness or lack of pores.

Eyes/Teeth: Solid white blocks or weird iris reflections.

Background: Warped depth of field or physical inconsistencies.

Anatomy: Extra fingers or unnatural joints.

3. ⚖️ The Risk Auditor

Role: Toxicity & Fraud Analysis.

Logic:

Fake Follower Estimate: Cynically assumes generic content + high followers = Bots.

Campaign Safety: Returns FALSE for "Safe to Collaborate" unless the profile is flawless.

4. 🐝 The Compliance Swarm

A 4-node swarm that aggressively audits ad creatives:

Authenticity Agent: Ruthless deepfake hunter.

Safety Agent: Scans for political nuance or aggression.

Compliance Agent: Flags absolute terms ("Guaranteed", "Best") and missing disclaimers.

Trust Agent: Measures "Brand Fit" and filters out "cheap/spammy" aesthetics.

📂 Project Structure

dashboard/
├── app.py                 # Main application logic & API routes
├── mcp.py                 # Model Context Protocol / AI Helper functions
├── insert_data.py         # Database seeding script
├── requirements.txt       # Python dependencies
├── .env                   # API Keys and Config
│
├── static/                # Static assets
│   ├── style/             # CSS files
│   └── uploads/           # Temporary storage for analyzed images
│
├── templates/             # HTML Interfaces
│   ├── index.html         # Landing page
│   ├── login.html         # Authentication
│   ├── dashboard.html     # Main Hub
│   ├── adtech.html        # Ad Creative Audit Interface
│   ├── influencer.html    # Influencer Risk Analysis Interface
│   ├── enterprise.html    # C-Suite Executive View
│   └── console.html       # Debug/Admin Console
│
└── __pycache__/           # Compiled Python files


🚀 Setup & Installation

Prerequisites

Python 3.8+

MongoDB Atlas Account

Google Gemini API Key

1. Clone & Install

git clone <repo-url>
cd dashboard
pip install -r requirements.txt


2. Configuration

Create a .env file in the root directory:

GEMINI_API_KEY=your_key_here
MONGO_URI=your_mongodb_connection_string
FLASK_SECRET=your_secret_key


3. Database Seeding

Initialize your MongoDB with default data:

python insert_data.py


4. Run the Application

python app.py


Access the dashboard at http://localhost:5000.

🛠️ Tech Stack

Core: Python, Flask

AI Models: Google Gemini 2.0 Flash, OpenAI Moderation, CLIP

Computer Vision: OpenCV (cv2), PIL, NumPy

Database: MongoDB

Frontend: HTML5, CSS3
