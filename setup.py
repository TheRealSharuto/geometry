from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="geometry",
    version="0.0.1",
    author="Shara Belton",
    author_email="sharabelton@proton.me",
    description="Calculating geometric things with authors of Neuroimaging and Data Science",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRealSharuto/geometry",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.8',
    install_requires=["pandas"]
)
