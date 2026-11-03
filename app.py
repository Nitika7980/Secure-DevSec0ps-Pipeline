import subprocess

def run_command(command):
    subprocess.call(command, shell=True)

password = "admin123"

run_command("echo Hello World")

print("Application started")
