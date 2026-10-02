import os
from langchain.tools import tool
from executor import Executor

executor = Executor()

@tool
def execute_command(command: str):
    """
    Execute a terminal command on the user's computer.

    IMPORTANT:
    Use this tool whenever the user asks you to perform
    an action on the computer or retrieve information
    from the terminal.

    The command will be executed directly by the operating
    system shell.
    """
    return executor.run(command)