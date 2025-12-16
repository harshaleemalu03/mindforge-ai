```md
# MindForge AI 🧠
Persona-Driven Deep Reasoning Engine using Gemini API

MindForge AI uses the Gemini API as a reasoning engine to generate expert-level, consistent, and structured content in a single API call through persistent personas.

---

## Key Features
- Persona-driven reasoning
- Single Gemini API call per request
- Consistent tone, depth, and structure
- Semantic caching to reduce API usage
- Free-tier optimized using gemini-2.5-flash

---

## Hackathon Theme
**Theme 2: Reasoning & Personalized Experience (Maximized Context)**

---

## Gemini API Integration
- Model: gemini-2.5-flash
- Role: Core reasoning and generation engine
- Gemini is essential for persona persistence and high-quality single-call output

---

## Architecture
```

User Input
↓
Persona Configuration
↓
Prompt Orchestrator
↓
Gemini API (1 call)
↓
Structured Output
↓
Semantic Cache (JSON)

```

---

## Tech Stack
- Frontend: Streamlit
- Backend: Python
- AI Model: Gemini API
- Caching: Local JSON

---

## Setup & Run
```bash
pip install -r requirements.txt
export GEMINI_API_KEY=your_api_key_here
streamlit run app.py
````

⚠️ Do not commit your API key to GitHub.

---

## Free Tier Optimization

* Flash model for higher request limits
* One API call per generation
* Semantic caching for repeated intents

---

### Example Prompts
**Persona:** Senior Software Engineer  
**Task:** Explain caching strategies for Python apps  
**Constraints:** Beginner-friendly, with examples

**Expected Output:**  
- Introduction to caching  
- Types of caches (memory, disk)  
- Example Python code snippet  
- Best practices
