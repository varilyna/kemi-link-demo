from pathlib import Path
import subprocess
import sys
root = Path(__file__).resolve().parent
database = root / "backend" / ".demo" / "db.sqlite3"
database.parent.mkdir(exist_ok=True)
fresh = not database.exists()
subprocess.run([sys.executable, "manage.py", "migrate", "--noinput"], cwd=root / "backend", check=True)
if fresh:
    subprocess.run([sys.executable, "manage.py", "loaddata", str(root / "demo-data.json")], cwd=root / "backend", check=True)
