import pathlib

from setuptools import find_packages, setup


def read(fname):
    with open(pathlib.Path(fname)) as fh:
        data = fh.read()
    return data


base_packages = read("requirements.txt")

dev_packages = [
    "jupyterlab>=0.35.4",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "flake8>=3.6.0",
    "pre-commit>=2.2.0",
    "mkdocs>=1.1",
    "mkdocs-material==4.6.3",
    "mkdocstrings>=0.11.0",
    "mkdocs-jupyter>=0.17.1",
]

setup(
    name="football_strava",
    version="0.0.1",
    packages=find_packages(exclude=["data", "docs", "notebooks"]),
    long_description=read("readme.md"),
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
)
