from setuptools import setup

setup(
    name="pymockdata",
    version="0.0.1",
    description="A Python library for generating mock data "
                "and exporting in various formats or directly into a database",
    author="Vlad Calin",
    author_email="vlad.s.calin@gmail.com",
    license="MIT",
    url="https://github.com/vladcalin/pymockdata",
    packages=["pymockdata"],
    entry_points={
        # "console_scripts": [
        #     "pymockdata = pymockdata.cli:main"
        # ]
    },
    test_suite="tests",
    install_requires=[
    ]
)
