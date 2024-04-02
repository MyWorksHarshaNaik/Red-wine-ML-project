import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"  # Update with your actual package version

REPO_NAME = "Red-wine-ML-project"
AUTHOR_USER = "MyWorksHarshaNaik"
SRC_REPO = "wineQuality"
AUTHOR_EMAIL = "naikharshas235@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for ML applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src")
)
