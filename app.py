import subprocess

def add(a, b):
    return a + b

print("CI/CD practice app is running")

# Intentionally insecure code for testing Bandit
subprocess.call("dir", shell=True)