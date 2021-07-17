# pip install --editable .
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pqcvt',
    version='0.1.0',
    author="Fernando Garcia",
    author_email="fergarciadlc@gmail.com",
    description="A simple CLI to covert parquet, csv and excel files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fergarciadlc/pqcvt",
    py_modules=['pqcvt'],
    install_requires=[
        'Click',
        'pandas',
        'pyarrow',
        'openpyxl',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pqcvt = pqcvt:cli',
        ],
    },
)