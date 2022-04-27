import pathlib
from setuptools import setup, find_packages
import versioneer

here = pathlib.Path(__file__).parent.resolve()
long_description = open("README.md").read()

# Requirements

install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("dev-requirements.txt").read().strip().split("\n")

# Human-Readable/Reusable Extras
# Add these to `optional-requirements.txt` as well
fastapi = "fastapi==0.68"

extras = {"fastapi": [fastapi]}
extras["all"] = sum(extras.values(), [])

setup(
    name="fideslang",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Fides Taxonomy Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ethyca/fideslang",
    python_requires=">=3.7, <4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Ethyca, Inc.",
    author_email="fidesteam@ethyca.com",
    license="Apache License 2.0",
    install_requires=install_requires,
    dev_requires=dev_requires,
    extras_require=extras,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
)
