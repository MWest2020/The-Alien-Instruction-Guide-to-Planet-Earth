import os
import sys
import subprocess
import venv
from pathlib import Path

def check_python():
    """Check if Python is installed and meets requirements."""
    try:
        import platform
        python_version = platform.python_version_tuple()
        if int(python_version[0]) < 3 or (int(python_version[0]) == 3 and int(python_version[1]) < 7):
            print("Python 3.7 or higher is required.")
            sys.exit(1)
    except ImportError:
        print("Python is not installed or not in PATH.")
        sys.exit(1)

def create_venv():
    """Create a virtual environment."""
    venv_dir = Path("venv")
    if not venv_dir.exists():
        print("Creating virtual environment...")
        venv.create(venv_dir, with_pip=True)
    else:
        print("Virtual environment already exists.")

def get_venv_python():
    """Get the path to the virtual environment's Python executable."""
    if sys.platform == "win32":
        return Path("venv/Scripts/python.exe")
    else:
        return Path("venv/bin/python")

def install_dependencies():
    """Install required packages."""
    python = get_venv_python()
    print("Installing dependencies...")
    
    # Upgrade pip
    subprocess.run([str(python), "-m", "pip", "install", "--upgrade", "pip"], check=True)
    
    # Install requirements
    subprocess.run([str(python), "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def create_directories():
    """Create necessary directories."""
    directories = [
        "ai/trained_model",
        "ai/training_data"
    ]
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

def main():
    print("Setting up The Alien Instruction Guide AI system...")
    
    # Check Python installation
    check_python()
    
    # Create virtual environment
    create_venv()
    
    # Install dependencies
    install_dependencies()
    
    # Create directories
    create_directories()
    
    print("\nInstallation complete!")
    print("\nTo activate the environment:")
    if sys.platform == "win32":
        print("venv\\Scripts\\activate.bat")
    else:
        print("source venv/bin/activate")
    
    print("\nTo train the model:")
    print("python ai/train_model.py")

if __name__ == "__main__":
    main() 