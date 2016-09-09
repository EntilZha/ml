from setuptools import setup, find_packages


setup(
    name='ml',
    description='',
    url='https://github.com/EntilZha/ml',
    author='Pedro Rodriguez',
    author_email='ski.rodriguez@gmail.com',
    maintainer='Pedro Rodriguez',
    maintainer_email='ski.rodriguez@gmail.com',
    license='Apache License 2.0',
    keywords='Machine Learning Utilities',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'test']),
    version='0.0.0',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
