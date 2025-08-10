import os
import subprocess
import shutil
import requests
import time

OLLAMA_PATH = "/Applications/Ollama.app"

def is_internet_available():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

def install_or_repair_ollama():
    if not os.path.exists(OLLAMA_PATH):
        print("Ollama nu este instalat. Îl descarc...")
        subprocess.run(["curl", "-L", "https://ollama.com/download/Ollama-darwin.zip", "-o", "ollama.zip"])
        subprocess.run(["unzip", "ollama.zip", "-d", "/Applications"])
        os.remove("ollama.zip")
    else:
        print("Ollama este deja instalat.")

    # Pornire Ollama
    subprocess.run(["open", OLLAMA_PATH])

    time.sleep(5)  # timp pentru a porni

def move_to_external_drive(external_path="/Volumes/ExternalDisk/OllamaModels"):
    src = os.path.expanduser("~/Library/Application Support/Ollama")
    if os.path.exists(src):
        os.makedirs(external_path, exist_ok=True)
        shutil.move(src, external_path)
        os.symlink(external_path, src)
        print(f"Modelele Ollama mutate pe {external_path}")

def ensure_models():
    if not is_internet_available():
        print("Internet indisponibil. Fallback la model local...")
        subprocess.run(["ollama", "run", "llama2"])
    else:
        print("Internet OK. Verific modelele...")
        subprocess.run(["ollama", "pull", "llama2"])
