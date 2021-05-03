"""Pacote Spectral - Computando índices espectrais."""

from setuptools import find_packages, setup

readme = open("README.rst").read()

history = open("CHANGES.rst").read()

packages = find_packages()

setup(
    name="spectral",
    version="1.0",
    description=__doc__,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    keywords=["Spectral Indices", "Earth Observations"],
    license="MIT",
    author="Gilberto Queiroz",
    author_email="user@email.org",
    url="https://github.com/prog-geo/spectral",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)