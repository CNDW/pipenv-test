import os

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)

PACKAGE_NAME = "private-package-a"

setup(
    name=PACKAGE_NAME,
    # These really don't work.
    package_dir={"": "src"},
    packages=find_packages("src"),
    # I don't know how to specify an empty key in setup.cfg.
    package_data={
        "": ["LICENSE*", "README*"],
    },
    install_requires=[
        "cachetools~=4.1.0",
        "camel_snake_kebab~=0.3.2",
        "Cython>=0.29.28,<3",
        "first>=2.0.1,<3",
        "gain-requests-futures~=0.9.7",
        "google-cloud-secret-manager>=1.0.0,<3",
        "jsonpointer~=2.2",
        "munch>=2.5,<3",
        "pydantic>=1.10,<2",
        "pyjwt>2,<3",
        "python-dateutil~=2.8",
        "pyyaml~=5.4",
        "requests>=2.28,<3",
        "rsa~=4.0",
        "singleton-decorator~=1.0.0",
        "orjson>=3.6.0,<4",
        "private-package-b>=0.0.1",
    ],
    description="A fake python package.",
    author="Dan Ryan",
    author_email="dan@danryan.co",
    url="https://github.com/sarugaku/legacy_backend_package",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python",
    ],
    version="0.0.4",
)
