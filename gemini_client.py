import google.generativeai as genai
import os

def init_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="""
You are a persistent expert persona.
Maintain consistency in tone, depth, and reasoning style.
Think step-by-step internally but output only the final structured response.
Optimize for clarity, correctness, and real-world usefulness.
"""
    )
    return model
