from setuptools import find_packages, setup

setup(
    name="housing",
    packages=find_packages(exclude=["housing_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
