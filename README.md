# 🤖 AI Autonomous Web Testing Platform

### Enterprise-Grade Natural Language Driven Test Automation System

An intelligent AI-powered web automation framework that converts natural language instructions into structured executable test workflows using Large Language Models (LLMs) and Playwright.

This platform demonstrates a scalable, modular, and extensible architecture suitable for real-world enterprise QA automation environments.

---

## 🚀 Executive Summary

The AI Autonomous Web Testing Platform enables users to:

* Provide a website URL
* Describe test scenarios in natural language
* Automatically generate structured automation steps using LLMs
* Execute browser tests via Playwright
* Perform dynamic assertions
* Generate detailed PDF reports
* Maintain execution history
* Operate through a secure UI interface

This system bridges the gap between manual QA and intelligent autonomous test generation.

---

# 🏗 High-Level Architecture

```
User (Streamlit UI)
        │
        ▼
Authentication Layer
        │
        ▼
Natural Language Input
        │
        ▼
LLM Parsing Engine (Gemini API)
        │
        ▼
Structured Test Steps (JSON)
        │
        ▼
Execution Engine (Playwright)
        │
        ├── Browser Automation
        ├── Assertion Engine
        ├── Error Handling
        └── Optional AI Debugging
        │
        ▼
Reporting Layer (PDF Generator)
        │
        ▼
Persistence Layer (SQLite History DB)
```

---

# 🧠 Core System Components

---

## 1️⃣ User Interface Layer (`ui_app.py`)

**Technology:** Streamlit

Responsibilities:

* Accept website URL input
* Accept natural language test cases
* Toggle headless execution mode
* Trigger test execution
* Display real-time execution logs
* Provide PDF report download
* Display historical execution records
* Manage authentication

This layer acts as the user-facing orchestration layer.

---

## 2️⃣ Natural Language Parsing Engine (`test_case_parser.py`)

**Technology:** Google Gemini API (LLM)

Responsibilities:

* Convert free-form test instructions into structured JSON
* Enforce strict output schema
* Clean and validate LLM output
* Handle parsing errors
* Support retry logic for API failures

### Example Structured Output

```json
[
  {
    "action": "fill",
    "params": {
      "selector": "input[name='username']",
      "value": "Admin"
    }
  }
]
```

This abstraction decouples human language from execution logic.

---

## 3️⃣ Automation Execution Engine (`playwright_executor.py`)

**Technology:** Playwright (Chromium)

Capabilities:

* Headed / headless browser execution
* Structured action handling:

  * open
  * click
  * fill
  * select
  * hover
  * scroll
  * wait
  * clear
* Assertion execution using dynamic evaluation
* Timeout handling
* Failure detection
* Optional AI-powered debugging suggestions

This module represents the core automation engine.

---

## 4️⃣ Reporting Engine (`report_generator.py`)

**Technology:** FPDF

Generates enterprise-style PDF reports including:

* Test metadata
* Timestamp
* Execution summary
* Pass/fail statistics
* Failure diagnostics
* AI debug suggestions

Reports are downloadable directly via the UI.

---

## 5️⃣ Persistence Layer (`database.py`)

**Technology:** SQLite

Stores:

* Website tested
* Execution timestamp
* Status (PASS / FAIL)
* Step counts
* Execution time

Supports auditability and historical analysis.

---

## 6️⃣ Security Layer

Implements:

* Basic authentication system
* Password hashing using bcrypt
* Secure environment variable management via `.env`

---

# 🛠 Technology Stack

| Layer                  | Technology        |
| ---------------------- | ----------------- |
| Frontend               | Streamlit         |
| Backend Logic          | Python            |
| AI Engine              | Google Gemini API |
| Automation             | Playwright        |
| Database               | SQLite            |
| Reporting              | FPDF              |
| Authentication         | bcrypt            |
| Version Control        | Git               |
| Environment Management | Python venv       |

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd ai-agent-automation-websites-testing
```

---

## 2️⃣ Create Virtual Environment (Python 3.11 Recommended)

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install streamlit playwright fpdf bcrypt pandas plotly langchain langchain-google-genai python-dotenv
playwright install
```

---

## 4️⃣ Configure Environment Variables

Create `.env` file:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

## 5️⃣ Launch Application

```bash
streamlit run ui_app.py
```

---

# 🧪 Example Enterprise Test Scenario

### Target Website:

```
https://opensource-demo.orangehrmlive.com
```

### Natural Language Input:

```
Enter username as Admin.
Enter password as admin123.
Click login button.
Click on the Admin menu.
Verify the page contains System Users.
Logout from the application.
Verify login page is visible.
```

---

# 📊 Key Features

* Natural language driven automation
* Modular architecture
* AI-based test generation
* Dynamic assertion evaluation
* AI-powered debugging suggestions
* Headless execution support
* Execution history tracking
* Enterprise-style reporting
* Secure credential handling
* Extensible design for future agent-based upgrades

---

# 📈 Scalability & Extensibility

This platform is designed to be extensible with:

* DOM-aware LLM prompting
* Self-healing selector engine
* Retry-based agent loops
* Model fallback mechanisms
* Caching layer for LLM responses
* CI/CD integration
* Cloud deployment
* Role-based access control
* Multi-user dashboard

---

# 🔍 Known Limitations

* Free-tier LLM API rate limits
* Complex dynamic SPAs may require enhanced selector strategies
* Current architecture does not yet include full DOM context reasoning

---

# 🏢 Enterprise Value Proposition

This system demonstrates how AI can:

* Reduce manual QA scripting effort
* Accelerate test case generation
* Improve automation flexibility
* Enable non-technical users to generate test scenarios
* Serve as foundation for AI-driven QA platforms

---

# 🧩 Future Enterprise Enhancements

* Advanced AI agent loop architecture
* DOM extraction and contextual prompting
* Intelligent selector healing
* Model usage monitoring
* Cost-aware LLM orchestration
* Distributed execution support
* Cloud-native deployment

---

# 👨‍💻 Author

Developed as an internship final project demonstrating AI-integrated automation architecture with production-oriented design principles.

---



