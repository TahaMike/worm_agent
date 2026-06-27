from setuptools import setup, find_packages

setup(
    name="worm-agent",
    version="0.1",
    packages=find_packages(),
    py_modules=["worm"],
    entry_points={
        "console_scripts": [
            "worm=worm:main",
        ],
    },
)