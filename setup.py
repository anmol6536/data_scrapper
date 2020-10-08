import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allergan",  # Replace with your own username
    version="0.0.7.11",
    author="Anmol Gorakashakar",
    author_email="anmol@genecentrix.com",
    description="Data collection package",
    long_description_content_type="text/markdown",
    url="https://github.com/anmol6536/nlp_hr.git",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["pandas", "numpy", "elsapy", "requests", "matplotlib"],
)
