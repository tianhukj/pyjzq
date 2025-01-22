from setuptools import setup, find_packages

setup(
    name='pyjzq',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        setuptools
    ],
    entry_points={
        'console_scripts': [
            'pyjzq=pyjzq.game:main',
        ],
    },
)
