from setuptools import setup, find_packages

setup(
    name='pyjzq',
    version='0.1.0',
    author="tianhukj",
    author_email="tianhukj@outlook.com",
    description="一个用python制作的命令行井字棋游戏",
    long_description=open("README.md").read(),
    long_description_content_type="game",
    url="https://github.com/tianhukj/pyjzq",
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'pyjzq=pyjzq.game:main',
        ],
    },
)
