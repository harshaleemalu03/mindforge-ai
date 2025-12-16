import google.generativeai as genai
import os

SYSTEM_PROMPT = """
You are an expert reasoning engine.

INTERNAL PROCESS (do not reveal):
1. Analyze the task
2. Apply persona capabilities
3. Reason step-by-step
4. Synthesize final answer

OUTPUT RULES:
- Do NOT mention your reasoning steps
- Produce only the final structured response
- Follow the output format strictly
"""

def init_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY")

    genai.configure(api_key=api_key)

    return genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )
