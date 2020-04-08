import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rs2wapy",
    version="1.0.0",
    packages=setuptools.find_packages(),
    url="https://github.com/tuokri/udk_configparser",
    author="tuokri",
    author_email="tuokri@tuta.io",
    description="Config parser for UDK .ini files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="ue3 udk configparser",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
