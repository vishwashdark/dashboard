# 🛡️ Aegis TrustEngine Dashboard

**A Multi-Agent Forensic Auditing System for AdTech & Influencer Marketing**

The Aegis TrustEngine is a forensic auditing dashboard designed for brands, agencies, and compliance teams. It detects deepfakes, analyzes influencer credibility, and measures financial & reputational risk using a Zero-Tolerance Multi-Agent Swarm architecture.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Intelligence Pipeline](#-the-intelligence-pipeline)
- [Agent Swarm Architecture](#-the-agent-swarm-personas)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Setup & Installation](#-setup--installation)
- [Usage](#-usage)
- [Features](#-features)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

---

## Overview

Aegis TrustEngine provides enterprise-grade content verification and influencer vetting through advanced AI models and multi-agent analysis. The platform protects brand reputation by identifying:

- **Deepfakes and AI-generated content**
- **Influencer fraud and bot networks**
- **Toxic or non-compliant content**
- **Financial risk in partnership deals**

---

## 🧠 The Intelligence Pipeline

Data flows through a multi-stage pipeline designed to eliminate high-risk content before it reaches the brand.

```mermaid
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
```

### Pipeline Stages

1. **Input Layer**: Ingests content from social platforms
2. **Vision Analysis**: OpenCV and vision models detect visual anomalies
3. **Content Moderation**: OpenAI moderation screens for policy violations
4. **Semantic Alignment**: CLIP ensures context-content consistency
5. **Multimodal Intelligence**: Gemini AI performs deep content analysis
6. **Agent Swarm**: Specialized agents provide domain-specific evaluation
7. **Reporting**: Generates actionable insights and risk scores

---

## 🤖 The Agent Swarm (Personas)

Multi-agent personas designed with cynical, brand-protective prompt engineering to maximize risk detection.

### 1. 🦈 The Deal Architect — "Shark Tank Investor"

**Role**: Financial structure & negotiation  
**Logic**: Evaluates efficiency ratio of Followers vs Revenue

**Behavior**:
- **Devaluation**: Low revenue vs high followers → assumes botting
- **Lowballing**: Protects brand P&L, not influencer ego
- **Skeptical**: Treats all metrics as inflated until proven real

**Decision Matrix**:
```
Engagement Rate < 2% + High Followers = RED FLAG
Cost per Engagement > Industry Benchmark = OVERPRICED
Follower Growth Spike without Content Quality = BOT PURCHASE
```

---

### 2. 🕵️‍♀️ The Forensic Analyst — "Zero Tolerance"

**Role**: Deepfake detection  
**Policy**: Flags ANY content with even a 1% likelihood of AI involvement

**Detection Vectors**:
- Skin smoothness / lack of pores
- Eye/teeth artifacts
- Background distortions
- Incorrect anatomy (hands, proportions)
- Lighting inconsistencies
- Unnatural motion patterns

**Technology Stack**:
- OpenCV for frame analysis
- CLIP for semantic-visual mismatch
- Gemini Vision for contextual anomalies

---

### 3. ⚖️ The Risk Auditor

**Role**: Toxicity, fraud, and safety auditing

**Logic**:
- Generic content + high followers = bot suspicion
- Safe to Collaborate = **FALSE** unless profile is flawless
- Toxicity detection in comments, captions, and engagement patterns

**Risk Categories**:
| Risk Type | Detection Method | Threshold |
|-----------|-----------------|-----------|
| Bot Networks | Engagement velocity analysis | >40% suspicious accounts |
| Toxic Content | NLP sentiment + moderation API | Any violation |
| Fraud Indicators | Follower-to-engagement ratio | <1.5% engagement rate |
| Brand Misalignment | Semantic content analysis | Mismatch score >30% |

---

### 4. 🐝 The Compliance Swarm

A 4-node cluster enforcing strict brand safety & regulatory rules.

#### Nodes:

**Authenticity Agent**
- Deepfake inspection using computer vision
- Verifies content originality
- Cross-references known AI patterns

**Safety Agent**
- Detects political/violent/aggressive cues
- Monitors hate speech and harassment
- Flags controversial associations

**Compliance Agent**
- Identifies absolute marketing claims
- Detects regulatory violations (FDA, FTC)
- Ensures disclosure compliance

**Trust Agent**
- Detects spammy/cheap aesthetics
- Evaluates brand fit and alignment
- Assesses professional presentation quality

---

## 📂 Project Structure

```
dashboard/
├── app.py                  # Main application logic & API routes
├── mcp.py                  # Model Context Protocol / AI helper functions
├── insert_data.py          # Database seeding script
├── requirements.txt        # Python dependencies
├── .env                    # API configuration (not tracked)
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
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **AI Models** | Gemini 2.0 Flash, OpenAI Moderation, CLIP |
| **Computer Vision** | OpenCV, PIL, NumPy |
| **Database** | MongoDB Atlas |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Authentication** | Flask-Session |
| **Deployment** | Docker, Gunicorn (production) |

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.8+
- MongoDB Atlas account
- Gemini API Key ([Get one here](https://ai.google.dev/))
- OpenAI API Key (for moderation)

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/aegis-trustengine.git
cd aegis-trustengine/dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/database
FLASK_SECRET=your_secret_key_here
```

### 4. Seed Database

```bash
python insert_data.py
```

This will populate MongoDB with sample influencer data and test cases.

### 5. Run Application

**Development Mode**:
```bash
python app.py
```

**Production Mode**:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Access the application at: **http://localhost:5000**

---

## 💼 Usage

### Authentication

1. Navigate to `/login`
2. Use credentials:
   - **Email**: `admin@aegis.ai`
   - **Password**: `admin123`

### Dashboard Navigation

- **AdTech Audit** (`/adtech`): Upload and analyze ad creatives
- **Influencer Analysis** (`/influencer`): Vet influencer profiles
- **Enterprise View** (`/enterprise`): Executive summary and ROI metrics
- **Admin Console** (`/console`): System configuration and logs

### Analyzing an Influencer

1. Go to **Influencer Analysis**
2. Enter Instagram/TikTok handle
3. Upload recent content samples
4. Click **Run Audit**
5. Review multi-agent risk assessment

---

## ✨ Features

### 🎯 Core Capabilities

- **Deepfake Detection**: Multi-model approach to identify AI-generated content
- **Influencer Fraud Detection**: Bot network identification and engagement analysis
- **Brand Safety Scoring**: Content toxicity and alignment measurement
- **Financial Risk Assessment**: ROI prediction and negotiation insights
- **Regulatory Compliance**: FTC disclosure and claim verification

### 📊 Analytics

- Real-time risk dashboards
- Historical trend analysis
- Comparative benchmarking
- Exportable audit reports (PDF/CSV)

### 🔐 Security

- Role-based access control (RBAC)
- Encrypted API communications
- Audit logging for compliance
- Data retention policies

---

## 📡 API Reference

### POST `/api/analyze_influencer`

Analyzes an influencer profile for fraud and risk.

**Request Body**:
```json
{
  "handle": "@influencer_name",
  "platform": "instagram",
  "image_url": "https://example.com/profile.jpg"
}
```

**Response**:
```json
{
  "risk_score": 67,
  "authenticity": "MEDIUM RISK",
  "agents": {
    "deal_architect": {
      "score": 45,
      "verdict": "Overpriced - high follower count, low engagement"
    },
    "forensic_analyst": {
      "score": 72,
      "verdict": "Possible AI enhancement detected"
    },
    "risk_auditor": {
      "score": 88,
      "verdict": "SAFE - No toxicity detected"
    },
    "compliance_swarm": {
      "score": 55,
      "verdict": "Missing FTC disclosures in 3/10 posts"
    }
  }
}
```

### POST `/api/analyze_creative`

Audits ad creative for brand safety and compliance.

**Request Body**:
```json
{
  "image": "base64_encoded_image",
  "campaign_type": "product_launch"
}
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 for Python code
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Gemini AI team for multimodal capabilities
- OpenAI for content moderation APIs
- OpenCV community for computer vision tools
- MongoDB for scalable database infrastructure

---

## 📞 Support

For questions or support:
- **Email**: support@aegis-trust.ai
- **Documentation**: [docs.aegis-trust.ai](https://docs.aegis-trust.ai)
- **Issues**: [GitHub Issues](https://github.com/yourusername/aegis-trustengine/issues)

---

**Built with 🛡️ by the Aegis Team**  
*Protecting Brands in the Age of AI Deception*
