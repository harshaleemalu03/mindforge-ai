import streamlit as st
import json
import hashlib
import os
from gemini_client import init_gemini

# ---------- Cache Setup ---------- #
CACHE_FILE = "cache/cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

# ---------- Semantic Key Function ---------- #
def semantic_key(persona, task, constraints):
    """
    Generate a semantic hash key based on persona capabilities and user task.
    Ensures similar intent maps to same cache entry.
    """
    core_intent = f"{persona['depth']}|{','.join(persona['focus'])}|{task}|{constraints}"
    return hashlib.sha256(core_intent.encode()).hexdigest()

# ---------- Streamlit App ---------- #
st.set_page_config(page_title="MindForge AI", layout="centered")
st.title("🧠 MindForge AI")
st.caption("Controlled Reasoning • Persistent Personas • One-Call Gemini")

# Load personas
with open("prompt_templates/personas.json") as f:
    personas = json.load(f)

persona_name = st.selectbox("Select Expert Persona", personas.keys())
task = st.text_area("Your Task", placeholder="Describe what you want the AI to do...")
constraints = st.text_input("Optional Constraints (audience, tone, format, etc.)")

if st.button("Forge Response"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        persona = personas[persona_name]
        cache = load_cache()
        key = semantic_key(persona, task, constraints)

        if key in cache:
            st.success("Loaded from semantic cache")
            st.write(cache[key])
        else:
            try:
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
            except Exception as e:
                st.error(f"Error generating response: {e}")
