from setuptools import setup, find_packages

# Get the long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# get the dependencies and installs
with open("requirements.txt") as f:
    required = f.read().splitlines()

# Define the setup function
setup(
    name='algo_fermat',
    version='1.0.1',
    description='Algorithmic library for Python lovers',
    long_description=long_description,
    author='Abdoufermat5',
    find_packages=find_packages(),
    install_requires=required,
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=[
        'graphs',
        'algorithms',
        'data structures',
        'networkx',
        'matplotlib',
        'numpy',
        'scipy',
    ],
    project_urls={
        'Source': 'https://github.com/abdoufermat5/algorithmique',
    },
)