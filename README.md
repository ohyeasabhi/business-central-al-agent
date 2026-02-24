# 🧠 Business Central AL Agent

A **local AI-powered assistant** for **Microsoft Dynamics 365 Business Central** developers,  
designed to behave like a **senior BC technical consultant**.

What's the catch? - "Unlimited searches/tokens."

How did I make it happen? - Since this whole thing runs on your PC specs, it has unlimited tokens and searches.

Built using **Streamlit + Ollama**, this agent generates **production-ready AL code**, follows **Microsoft best practices**, and understands **tables, pages, reports, RDLC, and codeunits** — all while running **100% locally**.

---

## ✨ Key Highlights

- 🧑‍💼 Consultant-grade responses (not generic AI output)
- 🧩 Extension-first AL development (no base object modification)
- 📄 Report & RDLC-aware generation
- 🗄️ Table, Page, Codeunit & Event Subscriber support
- 🧠 Business Central domain-specific system prompt
- 🔐 Fully local LLM (no cloud, no data leakage)
- ⚡ Fast & clean Streamlit UI

---

## 🏗️ Project Structure

```
business-central-al-agent/
│
├── app.py               # Streamlit application
├── system_prompt.py     # System prompt (BC consultant brain)
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Prerequisites

- **Python** 3.9 or higher  
- **Ollama** installed → https://ollama.com  
- **RAM**:  
  - Minimum: 16 GB  
  - Recommended: 24–32 GB (for 30B model)

---

## 🚀 Setup & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/business-central-al-agent.git
cd business-central-al-agent
```

---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Pull the LLM model
```bash
ollama pull qwen3-coder:30b
```

---

### 5️⃣ Run the application
```bash
streamlit run app.py
```

---

## 🧪 Example Prompts

- “Create a table extension to add GST Verification Status to Vendor”
- “Extend the Sales Invoice report and add a custom footer in RDLC”
- “Why is my event subscriber not firing in Business Central?”
- “Create a page extension to show Location Code on Posted Sales Invoice”
- “Generate a report extension with dataset and RDLC changes”

---

## 🧠 How It Works

- Uses a **Business Central–specific system prompt**
- Enforces **Microsoft best practices**
- Always generates **extension-based solutions**
- Produces structured output:
  - Analysis
  - AL Code
  - RDLC Changes (if applicable)

---

## 🛡️ Design Principles

- ❌ Never modify base objects
- ✅ Extensions only
- ✅ Latest Business Central version assumed
- ✅ Clean, readable, production-ready AL
- ✅ Minimal but sufficient explanation

---

## 🛣️ Roadmap

- 🔍 Automatic task-type detection
- 🎛️ Agent modes (Consultant / Debugger / Reviewer)
- 📋 Copy buttons for AL & RDLC code
- 🔁 Hot-reload system prompt
- 🧠 Multi-agent orchestration

---

## 🤝 Contributing

Pull requests are welcome.  
Please keep changes clean and aligned with Business Central best practices.

---

## 📄 License

MIT License
