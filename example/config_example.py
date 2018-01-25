from pathlib import Path
import sys

def set_config():
    sys.path.append(str(Path.cwd().parents[0]))