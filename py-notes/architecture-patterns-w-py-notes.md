https://www.cosmicpython.com/book/preface.html

# monitor-controller/setup.py
from setuptools import setup, find_packages

setup(
    name="monitor-controller",
    version="0.1.0",
    packages=find_packages(where='src'),  # Find packages inside src/
    package_dir={'': 'src'},              # Root package is in src/
    install_requires=[
        'mido',
        'python-rtmidi',
        'monitorcontrol',
    ],
)