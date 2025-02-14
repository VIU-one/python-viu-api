from setuptools import setup, find_packages
import os

version = os.getenv("PACKAGE_VERSION", "0.1.0")

setup(
    name="python_viu_api",
    version=version,
    packages=find_packages(include=["generated", "generated.*"]),
    install_requires=[
        "grpcio",
        "betterproto",
        "betterproto[compiler]"
    ],
    author="Michael Weber",
    author_email="info@searchviu.com",
    description="gRPC client for VIU API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VIU-one/python-viu-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
