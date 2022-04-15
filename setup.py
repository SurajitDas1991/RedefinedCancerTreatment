from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

## edit below variables as per your requirements -
REPO_NAME = "Machine Learning template"
AUTHOR_USER_NAME = "SurajitDas1991"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = required

setup(
    name=SRC_REPO,
    packages=find_packages(),
    version='0.0.1',
    description='A simple template for Machine Learning',
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="dsurajitd@gmail.com",
    author=AUTHOR_USER_NAME,
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS,
    license='MIT',
)
