from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from config import MODEL
from tools import execute_command
from system import SystemInfo

class TermAgent:
    def __init__(self):
        self.system = SystemInfo()

        self.model = ChatOllama(
            model = MODEL,
            temperature = 0,
        )

        self.agent = self._create_agent()

    def _create_agent(self):
        system_info = self.system.get_info()

        return create_agent(
            model = self.model,
            tools = [execute_command],
            system_prompt=f"""
                You are TermAgent, a terminal AI agent.

                Your purpose is to ACTUALLY perform tasks on the user's
                computer, not merely explain how to perform them.

                Current system:
                {system_info}

                IMPORTANT RULES:

                1. When the user asks you to DO something on the computer,
                you MUST use the execute_command tool.

                2. Do NOT simply tell the user which command they could run.

                3. Do NOT claim that a command was executed unless you
                actually called execute_command and received its result.

                4. You can call execute_command multiple times if needed.

                5. After executing a command, inspect its output and decide
                whether another command is necessary.

                6. Use commands appropriate for the detected OS and shell.

                7. For requests such as:
                - list files
                - create files
                - delete files
                - create folders
                - install packages
                - check system information
                - search files
                - run programs
                - inspect processes

                actually execute the required terminal commands.

                8. If the user asks a normal conversational question that
                requires no computer action, answer normally.

                9. Never fabricate command output.

                10. Keep the final response concise.
                """)

    def run(self, user_input: str):
        return self.agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        })

    def get_response(self, result):
        return result["messages"][-1].content