import ast
import os

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)

PACKAGE_NAME = "private-package-b"

EXTRAS_REQUIRE = {
    "reco": ["python-dateutil>=2.7.0", "simplejson"],
    "tests": [
        "pytest",
        "pytz",
    ],
    "lint": [
        "flake8==3.7.7",
        "pre-commit==1.16.0",
    ],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["reco"] + EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


setup(
    name="private-package-b",
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={
        "": ["LICENSE*", "README*"],
    },
    extras_require=EXTRAS_REQUIRE,
    zip_safe=False,
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
    version="0.0.3",
)
