# 🤖 AI-Driven Autonomous Web Testing Agent

An intelligent AI-powered automation framework that performs end-to-end (E2E) testing on web applications using **Playwright + Google Gemini LLM + LangGraph**.

This system allows users to provide test instructions in natural language, which are then converted into structured automation steps, dynamically generated assertions, and executed in a real browser environment.

## 🚀 Key Features

* 🧠 Natural Language Test Case Parsing using LLM
* 🔍 Automatic Playwright Assertion Generation
* 🌐 Headless/Headed Browser Execution
* 📊 Structured Test Execution Reports
* 🤖 AI-based Debugging Suggestions on Failure
* 🔄 Modular & Extensible Architecture

---

# 🏗️ System Architecture

```
User Input (Natural Language)
        ↓
LLM Test Case Parser
        ↓
Assertion Generator (LLM)
        ↓
Playwright Executor
        ↓
Execution Report + AI Debug Suggestions
```

---

# 🛠️ Tech Stack

* Python 3.10+
* Playwright (Browser Automation)
* Google Gemini (LLM)
* LangChain
* LangGraph
* python-dotenv
* Regular Expressions (re module)

---

# 📂 Project Structure

```
AI-agent-to-automate-website-testing/
│
├── playwright_executor.py
├── test_case_parser.py
├── llm_assertion_generator.py
├── LangGraphImplementation.py
├── LangGraphToWritePlaywrightScript.py
├── README.md
└── .env
```

---

# 📄 File Explanations

---

## 1️⃣ playwright_executor.py

🔹 Core execution engine of the framework.
🔹 Launches Chromium browser (headless or headed).
🔹 Executes test steps sequentially.
🔹 Evaluates AI-generated Playwright assertions dynamically.
🔹 Generates structured execution summary.
🔹 Provides AI debugging suggestions if test fails.

### Responsibilities:

* Browser lifecycle management
* Action handling (open, click, fill, select, hover, wait)
* Assertion evaluation
* Error handling
* AI failure analysis

---

## 2️⃣ test_case_parser.py

🔹 Converts natural language instructions into structured JSON commands.
🔹 Uses Google Gemini LLM for semantic parsing.

Example:

Input:

```
Open login page.
Enter username as Admin.
Click login.
```

Output:

```json
[
  {"action": "open", "params": {...}},
  {"action": "fill", "params": {...}},
  {"action": "click", "params": {...}}
]
```

---

## 3️⃣ llm_assertion_generator.py

🔹 Generates Playwright assertion statements from expected outcomes.
🔹 Ensures:

* Valid Playwright syntax
* Only executable `expect()` statements
* No extra comments or markdown

This reduces manual assertion writing effort.

---

## 4️⃣ LangGraphImplementation.py

🔹 Demonstrates basic conversational AI agent using LangGraph.
🔹 Shows state-based LLM workflow design.
🔹 Serves as foundation for agent architecture.

---

## 5️⃣ LangGraphToWritePlaywrightScript.py

🔹 Uses LLM to generate complete Playwright JavaScript test scripts.
🔹 Extracts generated code blocks automatically.
🔹 Saves script as `.spec.js` file.

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-agent-to-automate-website-testing.git
cd AI-agent-to-automate-website-testing
```

---

## 2️⃣ Install Dependencies

```bash
pip install playwright
pip install langchain
pip install langchain-google-genai
pip install langgraph
pip install python-dotenv
```

Install browser binaries:

```bash
playwright install
```

---

## 3️⃣ Configure API Key

Create a `.env` file in root folder:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get your API key from:
[https://aistudio.google.com](https://aistudio.google.com)

---

# ▶️ How To Execute

## Run Main Automation Flow

```bash
python playwright_executor.py
```

This will:

* Launch browser
* Perform automated test steps
* Run assertions
* Print execution summary
* Provide AI debugging (if failure occurs)

---

## Run Test Case Parser

```bash
python test_case_parser.py
```

---

## Run Assertion Generator

```bash
python llm_assertion_generator.py
```

---

## Run LangGraph Agent

```bash
python LangGraphImplementation.py
```

---

# 📊 Sample Execution Output

```
🧪 TEST EXECUTION : OrangeHRM — HR Workflow Automation
📊 Total Steps    : 7
✅ Status         : PASS
📈 Pass Rate      : 100%
⏱️ Execution Time : 00:00:15
```

---

# 🧠 Key Concepts Demonstrated

* Agent-based architecture
* LLM prompt engineering
* AI-assisted test automation
* Dynamic code evaluation
* Headless browser automation
* Self-healing testing concept
* Intelligent failure analysis

---

# 🔒 Security Note

API keys are managed using `.env` file and are not committed to version control.

---

# 🎯 Future Improvements

* Parallel test execution
* CI/CD pipeline integration
* Screenshot/video capture on failure
* Self-healing locator mechanism
* Multi-browser support

---

# 👨‍💻 Author

Final Year Project
AI-Powered Autonomous Web Testing Framework





