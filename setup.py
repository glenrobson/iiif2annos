import os
# read the contents of your README file
from pathlib import Path

from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if os.path.exists("version.txt"):
    VERSION = (this_directory / "version.txt").read_text().strip()
else:
    VERSION = "0.0.0.dev0"

setup(
    name="iiif2annos",  # Replace with your package name
    version=VERSION,
    description="OCR a IIIF images in a manifest and generate annotations ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Glen Robson",
    author_email="glen.robson@gmail.com",
    url="https://github.com/glenrobson/iiif2annos",  # Project URL
    license="MIT",  # License type
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[
        # List your dependencies here
        "pillow < 12.0.0",
        "requests < 3.0.0",
        "pytesseract < 4.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.6",  # Minimum Python version
)