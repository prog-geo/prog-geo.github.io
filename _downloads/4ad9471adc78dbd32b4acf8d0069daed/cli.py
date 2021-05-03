"""Command-Line Interface for Spectral."""

import click

from .evi import EVI
from .ndvi import NDVI

@click.group()
@click.version_option()
def cli():
    """Spectral commands.
    .. note:: You can invoke more than one subcommand in one go.
    """


@cli.command()
@click.option('-n', '--nir', required=True, type=float,
              help='Near-infrared spectral band.')
@click.option('-r', '--red', required=True, type=float,
              help='Red spectral band.')
@click.option('-b', '--blue', required=True, type=float,
              help='Blue spectral band.')
def evi(nir, red, blue):
    result = EVI(nir, red, blue)

    print(f"EVI: {result}")


@cli.command()
@click.option('-n', '--nir', required=True, type=float,
              help='Near-infrared spectral band.')
@click.option('-r', '--red', required=True, type=float,
              help='Red spectral band.')
def ndvi(nir, red):
    result = NDVI(nir, red)

    print(f"NDVI: {result}")