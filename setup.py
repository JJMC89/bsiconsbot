"""Installer script."""
from setuptools import find_packages, setup


def readme():
    """Read the readme file."""
    with open("README.rst") as file:
        return file.read()


setup(
    author="JJMC89",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="BSicons bot",
    download_url="https://github.com/JJMC89/bsiconsbot",
    include_package_data=True,
    install_requires=["mwparserfromhell", "pywikibot"],
    keywords=["bot", "bsicon", "mediawiki"],
    license="MIT",
    long_description=readme(),
    name="bsiconsbot",
    packages=find_packages(exclude=["tests"]),
    project_urls={
        "Bug tracker": "https://github.com/JJMC89/bsiconsbot/issues",
        "Source code": "https://github.com/JJMC89/bsiconsbot",
    },
    version="0.1.dev3",
)
