#venv\Scripts\activate
from openai import OpenAI
from dotenv import load_dotenv
import json
import os
from Tools.file_open import read_file, write_file
from Tools.project_tools import create_project_structure
from Tools.command_runner import run_command, open_browser
from pathlib import Path
import sys

# Load environment and system prompt
load_dotenv()
client = OpenAI()

with open("System_Prompts.txt", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# Set initial messages and tools
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

def run_npm_command(command, cwd=None):
    """Run npm commands with proper error handling"""
    try:
        if sys.platform == "win32":
            result = run_command(f"npm {command}", cwd)
        else:
         result = run_command(f"npm {command}", cwd)
        return result
    except Exception as e:
        return f"Error running npm command: {str(e)}"

def run_pip_command(command, cwd=None):
    """Run pip commands with proper error handling"""
    try:
        if sys.platform == "win32":
            result = run_command(f"pip {command}", cwd)
        else:
            result = run_command(f"pip3 {command}", cwd)
        return result
    except Exception as e:
        return f"Error running pip command: {str(e)}"

available_tools = {
    "create_project_structure": create_project_structure,
    "write_file": write_file,
    "read_file": read_file,
    "run_command": run_command,
    "open_browser": open_browser,
    "run_npm_command": run_npm_command,
    "run_pip_command": run_pip_command,
}

def print_welcome():
    print("\n🤖 Welcome to the AI Development Assistant!")
    print("I can help you with:")
    print("  • Creating full-stack projects")
    print("  • Managing dependencies (npm/pip)")
    print("  • Writing and modifying code")
    print("  • Running development servers")
    print("\nType 'exit' to quit or start by describing your project!")

# Main loop
print_welcome()

while True:
    user_input = input("\n 🧑‍💻 > ")
    
    if user_input.lower() == 'exit':
        print("👋 Goodbye!")
        break
        
    messages.append({"role": "user", "content": user_input})

    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                response_format={"type": "json_object"},
                messages=messages
            )

            assistant_message = response.choices[0].message.content
            print(f"\n🤖 JSON: {assistant_message}")
            messages.append({"role": "assistant", "content": assistant_message})

            parsed = json.loads(assistant_message)
            step = parsed.get("step")

            if step == "plan":
                print(f"🧠: {parsed['content']}")

            elif step == "ask_user":
             if "Final improvements" in parsed["content"]:
              print(f"✨ Final touch: {parsed['content']}")
              follow_up = input("\n 🧑‍💻 > ")
              messages.append({"role": "user", "content": follow_up})
              break
             elif parsed["content"].strip() == "":
        # skip empty follow-ups
              messages.append({"role": "user", "content": "Yes, go ahead."})
              continue
             else:
              print(f"❓ Follow-up: {parsed['content']}")
             follow_up = input("\n 🧑‍💻 > ")
             messages.append({"role": "user", "content": follow_up})
             break
            # Let it re-enter the outer while True to trigger next assistant message


            elif step == "output":
                print(f"✅ Done: {parsed['content']}")
                print("-" * 50)
                break

            elif step == "action":
                func_name = parsed.get("function")
                tool_input = parsed.get("input")

                print(f"⚙️ Auto-executing: `{func_name}` with input: {tool_input}")


                print(f"⚙️ Action: Calling `{func_name}` with input: {tool_input}")
                try:
                    tool_fn = available_tools[func_name]
                    if isinstance(tool_input, dict):
                        result = tool_fn(**tool_input)
                    else:
                        result = tool_fn(tool_input)

                    messages.append({"role": "user", "content": json.dumps({
                        "step": "observe",
                        "output": result
                    })})
                except Exception as e:
                    print(f"❌ Tool execution failed: {e}")
                    messages.append({
                        "role": "user",
                        "content": json.dumps({
                            "step": "observe",
                            "output": f"Error: {str(e)}"
                        })
                    })

                break
                
        except json.JSONDecodeError:
            print("❌ Error: Invalid JSON response from assistant")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            break

