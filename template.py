import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

project_name = 'Chicken_Disease_classification'

list_of_classes = [
"github/workflow/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/constants/__init__.py",
"config/config.yaml",
"dvc.yaml",
"requirements.txt",
"setup.py",
"research/trails.ipynb",
"templates/index.html",
"test.py"
]

for file_path in list_of_classes:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Created empty file: {file_path}")

    else:
        logging.info(f"File already exists: {file_name}")