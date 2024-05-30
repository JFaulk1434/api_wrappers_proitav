from setuptools import setup, find_packages

setup(
    name="apiwrappers",
    version="0.5",
    packages=find_packages(),
    description="API Wrapper for ProITAV Products",
    author="Justin Faulk",
    author_email="jfaulk@proitav.us",
    url="proitav.us",
    install_requires=[
        "pyserial",
        "pexpect",
        "telnetlib3",
    ],
)
