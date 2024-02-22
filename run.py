import subprocess

command = "uvicorn main:app --reload"
subprocess.run(command, shell=True)
