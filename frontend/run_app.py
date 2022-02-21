import subprocess

cmd = 'source ./venv/bin/activate; streamlit run main.py'
subprocess.call(cmd, shell=True, executable='/bin/bash')