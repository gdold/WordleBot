from setuptools import setup, find_packages

setup(
    name = "WordleBot",
    version = "0.2",
    author='Gavin Dold',
	description='This bot solves wordles.',
	url='https://github.com/gdold/WordleBot',
    license='The MIT License (MIT)',
    packages = find_packages(exclude=['*test']),
    #scripts = ['scripts/wordlebot'],
    install_requires = ['argparse','numpy','pandas'],
	entry_points={ 'console_scripts': ['wordlebot=WordleBot:run_bot_from_cmd'] },
	python_requires=">=3.6"
)