# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_config.ipynb.

# %% auto 0
__all__ = ['fetch_env_var']

# %% ../nbs/05_config.ipynb 1
import os
from dotenv import load_dotenv
from pathlib import Path

# %% ../nbs/05_config.ipynb 2
def fetch_env_var(var_name):
    # First, check if the environment variable is set
    env_var_value = os.getenv(var_name)
    if env_var_value is not None:
        return env_var_value

    # If the environment variable is not set, check in the .env file
    env_path = Path.home() / '.audio-journal' / 'config'
    if not env_path.is_file():
        print(f"Error: {env_path} does not exist.")
        print("Please create this file with the format:")
        print('\n'.join([
            'NOTION_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"',
            'NOTION_PAGE_ID="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"'
        ]))
        exit(1)

    load_dotenv(dotenv_path=env_path, override=True)

    env_var_value = os.getenv(var_name)
    if env_var_value is None:
        print(f"Error: {var_name} not found in environment variables or {env_path}.")
        print("Please add it to the file or set it as an environment variable.")
        exit(1)
