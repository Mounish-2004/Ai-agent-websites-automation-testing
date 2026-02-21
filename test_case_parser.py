import os
import json
from typing import List, Dict, Union, Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


# -------------------------
# LOAD ENVIRONMENT VARIABLES
# -------------------------
load_dotenv()

# -------------------------
# INITIALIZE GEMINI MODEL
# -------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)

# -------------------------
# SYSTEM PROMPT
# -------------------------
SYSTEM_PROMPT = """
You are an instruction parser for an automated web testing system.

Your task:
Convert a natural language test case into structured test commands.

Output ONLY valid JSON.
Do not explain anything.
Do not add extra keys.

Allowed actions:
open
fill
click
select
hover
wait
scroll
clear
assert

Output format:
[
  {
    "action": "<action>",
    "params": {
        "selector": "<css selector if needed>",
        "value": "<value if needed>",
        "url": "<url if needed>"
    }
  }
]
"""

# -------------------------
# HELPER FUNCTION
# -------------------------
def clean_json_output(content: str) -> str:
    """
    Removes markdown formatting if LLM wraps JSON in code blocks.
    """
    if "```json" in content:
        content = content.replace("```json", "").replace("```", "")
    elif "```" in content:
        content = content.replace("```", "")
    return content.strip()


# -------------------------
# CORE LLM PARSER FUNCTION
# -------------------------
def llm_parse_instruction(instruction: str) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Sends system prompt and user instruction to Gemini
    and returns parsed JSON.
    """
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=instruction)
    ]

    try:
        response = llm.invoke(messages)
        content = response.content

        if isinstance(content, list):
            if len(content) > 0 and isinstance(content[0], dict) and 'text' in content[0]:
                text_content = content[0]['text']
                cleaned_text = clean_json_output(text_content)
                return json.loads(cleaned_text)
            return content

        if isinstance(content, str):
            cleaned_text = clean_json_output(content)
            return json.loads(cleaned_text)

        raise TypeError(f"Unexpected Gemini response format: {type(content)}")

    except json.JSONDecodeError as e:
        return {
            "error": "Failed to parse JSON",
            "details": str(e)
        }

    except Exception as e:
        return {
            "error": "An error occurred during processing",
            "details": str(e)
        }


# -------------------------
# WRAPPER FUNCTION FOR UI
# -------------------------
def generate_test_steps(natural_input: str) -> List[Dict[str, Any]]:
    """
    Converts natural language input into structured
    test steps compatible with PlaywrightExecutor.
    """
    result = llm_parse_instruction(natural_input)

    if isinstance(result, dict) and "error" in result:
        raise Exception(f"LLM Parsing Error: {result}")

    structured_steps = []

    for step in result:
        action = step.get("action")
        params = step.get("params", {})

        structured_steps.append({
            "action": action,
            "params": params,
            "assertions": []
        })

    return structured_steps


# -------------------------
# STANDALONE TESTING
# -------------------------
if __name__ == "__main__":

    test_case = """
    Open https://opensource-demo.orangehrmlive.com.
    Enter username as Admin.
    Enter password as admin123.
    Click login button.
    """

    print("\nProcessing Test Case:\n")
    print(test_case)
    print("-" * 50)

    output = generate_test_steps(test_case)

    print(json.dumps(output, indent=2))