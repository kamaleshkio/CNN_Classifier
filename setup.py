import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "CNN_Classifier"
AUTHOR_USER_NAME = "KAMALESH_B"
SRC_REPO = "Chicken_Disease_classification"
AUTHOR_EMAIL = "kamaleshbaskaran4310@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A CNN classifier for image classification using TensorFlow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    package=setuptools.find_packages(where="src")) 


