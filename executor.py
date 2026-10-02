import subprocess

class Executor:
    def run(self, command):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            result = {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }

        except Exception as e:
            result = {
                "stdout": "",
                "stderr": str(e),
                "returncode": -1
            }