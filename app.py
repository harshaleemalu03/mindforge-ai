import streamlit as st
import json, os, hashlib
from gemini_client import init_gemini

CACHE_FILE = "cache/cache.json"

def load_cache():
    return json.load(open(CACHE_FILE)) if os.path.exists(CACHE_FILE) else {}

def save_cache(cache):
    json.dump(cache, open(CACHE_FILE, "w"), indent=2)

def semantic_key(persona, task, constraints):
    core = f"{persona['depth']}|{','.join(persona['focus'])}|{task}"
    return hashlib.sha256(core.encode()).hexdigest()

st.set_page_config(page_title="MindForge AI", layout="centered")
st.title("🧠 MindForge AI")
st.caption("Controlled Reasoning • Persistent Personas • One-Call Gemini")

with open("prompt_templates/personas.json") as f:
    personas = json.load(f)

persona_name = st.selectbox("Select Expert Persona", personas.keys())
task = st.text_area("Your Task")
constraints = st.text_input("Constraints (optional)")

if st.button("Forge Response"):
    persona = personas[persona_name]
    cache = load_cache()
    key = semantic_key(persona, task, constraints)

    if key in cache:
        st.success("Loaded from intelligent cache")
        st.write(cache[key])
    else:
        model = init_gemini()

        prompt = f"""
Persona Configuration:
Tone: {persona['tone']}
Depth: {persona['depth']}
Focus Areas: {', '.join(persona['focus'])}
Output Style: {persona['output_style']}

User Task:
{task}

Constraints:
{constraints}

Required Output Format:
- Clear title
- Structured sections
- Actionable insights
"""

        response = model.generate_content(prompt).text
        cache[key] = response
        save_cache(cache)

        st.success("Generated via Gemini reasoning engine")
        st.write(response)
