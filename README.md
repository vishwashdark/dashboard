#  Aegis TrustEngine
**Platform-Scale Protection Against AI Deception**

An AI-powered authenticity engine for social platforms that detects deepfakes, analyzes influencer credibility, and measures financial & reputational risk using advanced machine learning and multi-agent analysis.

---

##  Table of Contents

- [Overview](#overview)
- [Intelligence Pipeline](#-the-intelligence-pipeline)
- [Agent Swarm Architecture](#-the-agent-swarm-personas)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Setup & Installation](#-setup--installation)
- [Usage](#-usage)
- [Features](#-features)
- [Contributing](#-contributing)
- [Code Standards](#-code-standards)

---

## Overview

Aegis TrustEngine provides enterprise-grade content verification and influencer vetting through advanced AI models and multi-agent analysis. The platform protects brand reputation by identifying:

- **Deepfake Detection**: Multi-modal AI analysis using CLIP and custom models
- **Influencer Fraud Detection**: Bot network identification and engagement analysis
- **Content Moderation**: OpenAI-powered safety screening
- **Risk Assessment**: Multi-agent evaluation system
- **Real-time Analysis**: Fast inference for production environments

---

##  The Intelligence Pipeline

Data flows through a multi-stage pipeline designed to eliminate high-risk content before it reaches the brand.

```mermaid
graph TD
    A[Social Platforms Input] --> B[Vision Model CvT-13]
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
2. **Vision Analysis**: Vision model detect visual anomalies
3. **Content Moderation**: OpenAI moderation screens for policy violations
4. **Semantic Alignment**: CLIP ensures context-content consistency
5. **Multimodal Intelligence**: Gemini AI performs deep content analysis
6. **Agent Swarm**: Specialized agents provide domain-specific evaluation
7. **Reporting**: Generates actionable insights and risk scores

---

##  The Agent Swarm (Personas)

Multi-agent personas designed with cynical, brand-protective prompt engineering to maximize risk detection

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

##  Project Structure

```
dashboard/
├── app.py                  # Main application logic & API routes
├── mcp.py                  # Model Context Protocol / AI helper functions
├── CLIP_openai.py          # CLIP integration for semantic analysis (3 KB)
├── openai_moderation.py    # OpenAI moderation API wrapper (3 KB)
├── custom_dataset.py       # Custom dataset loader and preprocessing (1 KB)
├── test_ai.py              # AI model testing utilities (2 KB)
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

##  Tech Stack

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

##  Setup & Installation

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
YOUR_DATABASE=mongodb+srv://username:password@cluster.mongodb.net/database
FLASK_SECRET=your_secret_key_here
```





##  Usage

### Authentication

1. Navigate to `/login`
2. Use credentials:
   - **Email**: `admin@aegis.ai`
   - **Password**: `admin123`

### AegiesEngine Navigation

- **AdTech Audit** (`/adtech`): Upload and analyze ad creatives
- **Influencer Analysis** (`/influencer`): Vet influencer profiles
- **Enterprise View** (`/enterprise`): Executive summary of analyzed media



##  Features

###  Core Capabilities

- **Deepfake Detection**: Multi-model approach to identify AI-generated content
- **Influencer Fraud Detection**: Bot network identification and engagement analysis
- **Brand Safety Scoring**: Content toxicity and alignment measurement
- **Regulatory Compliance**: AI Policy Adherence




##  Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 for Python code
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation as needed



**Built by the Aegis Team**  
*Protecting Brands in the Age of AI Deception*
