import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sa2-seed-key", 
    version="0.0.1",
    author="Brian Ledbetter",
    author_email="brian@brianledbetter.com",
    description="SA2 Seed/Key Authorization for Volkswagen AG Vehicles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bri3d/sa2_seed_key",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
