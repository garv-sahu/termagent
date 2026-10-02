import platform
import os
import sys

class SystemInfo:
    def __init__(self):
        self.info = self._detect_system()

    def _detect_system(self):
        return {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.architecture()[0],
            "Processor": platform.processor(),
            "Shell": os.environ.get("SHELL") or os.environ.get("COMSPEC"),
            "Current Directory": os.getcwd(),
        }

    def get_info(self):
        return self.info

    def display(self):
        print("TermAgent\n")
        for key, value in self.info.items():
            print(f"{key}: {value}")
        print("------------------\n")