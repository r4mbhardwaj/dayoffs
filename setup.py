from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="dayoffs",
    version="0.0.1",
    author="Ram Bhardwaj",
    author_email="r4mbhardwaj@gmail.com",
    description="A Python library for managing holidays and days off.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r4mbhardwaj/dayoffs",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
