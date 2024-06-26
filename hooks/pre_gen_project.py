import os
import sys

repo_name = "{{ cookiecutter.repo_name }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if repo_name.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {repo_name=} is not a valid name for this template.{RESET_ALL}")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")