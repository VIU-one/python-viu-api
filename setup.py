from setuptools import setup, find_packages

setup(
    name="python_viu_api",
    version="0.1.0",
    packages=find_packages(include=["generated", "generated.*"]),
    install_requires=[
        "grpcio",
        "betterproto",
        "betterproto[compiler]"
    ],
    author="Michael Weber",
    author_email="Michael Weber",
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
