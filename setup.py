from setuptools import setup
from setuptools import find_packages

from cn2an import version


setup(
    name="cn2an",
    version=version.VERSION,
    author="HaveTwoBrush",
    author_email="kinggreenhall@gmail.com",
    url="https://github.com/HaveTwoBrush/cn2an",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("./requirements.txt", "r", encoding="utf-8").read().splitlines(),
    description="Convert Chinese numerals and Arabic numerals.",
    long_description=open("./README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
