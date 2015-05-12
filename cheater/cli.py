from cheater.render import render_cheatsheets
import click

@click.command()

def main():
    """Cheater is a cheetsheet display app"""
    render_cheatsheets()
    # Fixme: temporary imports, should be methods
    from cheater import app
