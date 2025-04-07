from setuptools import setup, find_packages

setup(
    name = "recallbum",
    version = "0.1.0",
    packages = find_packages(),
    install_requires = [
        "argparse",
        "bs4",
        "chardet"
    ],
    entry_points = {
        "console_scripts": [
            "recallbum=recallbum:recallbum"
        ],
    },
)
