import click
import logging
logger = logging.getLogger()

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.option('--loglevel', '-ll', nargs=2, type=click.Choice(['DEBUG','INFO','WARNING','ERROR','CRITICAL']))
@click.argument('name', default='world', required=False)
def main(name, loglevel, as_cowboy):
    """{{ cookiecutter.project_short_description }}"""
    logging.basicConfig(level=loglevel)

    greet = 'Howdy' if as_cowboy else 'Hello'

    logger.debug('Sending greeting')
    click.echo('{0}, {1}.'.format(greet, name))
