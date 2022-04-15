import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="varnan",
    version="1.0.0",
    description="A CTF-Writeup Tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AmitGupta7580/Varnan",
    author="Amit Gupta",
    author_email="amitgupta758000@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["typer"],
    entry_points={
        "console_scripts": [
            "varnan=varnan.__main__:main",
        ]
    },
)