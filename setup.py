import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LinkCrypt", # Replace with your own username
    version="0.0.1",
    author="DrScriptastic",
    author_email="codeusstudio@gmail.com",
    description="LinkCrypt is an enecyption program to encrypt and decrypt files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SplitScreenStudios/LinkCrypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
