import os
from setuptools import setup

current_directory = os.path.dirname(__file__)

version = "3.0.0"

try:
    with open(os.path.join(current_directory, 'rev.txt')) as file:
        for line in file: version = "{}-{}".format(version,line.strip());break
except:
    pass

setup(
    name="rust_webrcon",
    author='fieu',
    url='https://github.com/fieu/rust_webrcon',
    version=version,
    packages=["rust_webrcon", "rust_webrcon.utils"],
    python_requires='>=3.6',
    platforms=['Windows', 'Linux', 'OSX'],
    description='Tried of trying to find working rust web rcon for python look no further.',
    keywords='Rust web rcon interaction tool',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "websocket-client >= 0.54.0"
    ]
)
