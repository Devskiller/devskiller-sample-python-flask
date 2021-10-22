from setuptools import find_packages, setup

setup(
    name="sample-flask-calculator",
    version="1.0.0",
    author="Devskiller.com",
    author_email="support@devskiller.com",
    packages=find_packages(),
    test_suite="tests",
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "pytest-timeout",
    ],
    install_requires=[
        "flask",
    ],
)
