from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Intraday-Volatility-Model",
    version="0.1.0",
    author="Ignacio Pericet",
    author_email="ignacio.pericetnavar@udc.edu",
    description="A dashboard for analyzing 0-DTE options",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ignaciopericet/Intraday-Volatility-Model",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "dash==2.9.3",
        "yfinance==0.2.18",
        "numpy==1.24.3",
        "pandas==2.0.1",
        "scipy==1.10.1",
        "arch==5.3.1",
        "plotly==5.14.1",
    ],
    entry_points={
        "console_scripts": [
            "intraday-volatility-model=dashboard.app:main",
        ],
    },
)