import streamlit as st
import json
import hashlib
import os

from gemini_client import init_gemini

CACHE_FILE = "cache/cache.json"

# ---------------- Cache Utilities ---------------- #

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

# ---------------- App Setup ---------------- #

st.set_page_config(
    page_title="MindForge AI",
    layout="centered"
)

st.title("🧠 MindForge AI")
st.subheader("Persona-Driven Deep Reasoning Engine")

st.write(
    "Generate expert-level content in **one prompt** using a persistent persona powered by the **Gemini API**."
)

# ---------------- Load Personas ---------------- #

with open("prompt_templates/personas.json") as f:
    personas = json.load(f)

persona_name = st.selectbox(
    "Choose Expert Persona",
    list(personas.keys())
)

task = st.text_area(
    "Describe your task",
    placeholder="e.g. Explain caching strategies for interviews"
)

constraints = st.text_input(
    "Optional constraints",
    placeholder="Audience, tone, length, format, etc."
)

# ---------------- Gemini Logic ---------------- #

if st.button("Generate Response"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        cache = load_cache()
        cache_key = hashlib.md5(
            f"{persona_name}{task}{constraints}".encode()
        ).hexdigest()

        if cache_key in cache:
            st.success("Loaded from cache")
            st.write(cache[cache_key])
        else:
            try:
                model = init_gemini()

                prompt = f"""
Persona Description:
{personas[persona_name]['description']}

Task:
{task}

Constraints:
{constraints}

Produce a clear, final, well-structured response.
"""

                response = model.generate_content(prompt)
                output = response.text

                cache[cache_key] = output
                save_cache(cache)

                st.success("Generated using Gemini API")
                st.write(output)

            except Exception as e:
                st.error(str(e))
