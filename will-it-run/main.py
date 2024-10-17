import click
import platform
from html2text import html2text
from scraper import search

@click.command()
@click.argument("game")
def compare(game: str):
    """
    The main function for comparing your sys requirements with the game's
    recommended requirements
    """

    click.echo(f'So, you want to run "{game}"...')
    click.echo("Collecting data...\n")

    req = search(game)
    if req == []:
        click.echo(f"The game isn't selling on Steam for {platform.system()}.")
    
    else:
        min = req["minimum"]
        rec = req["recommended"]

        print("The minimal requirements are:")
        print(html2text(min))
        print("\n")

        print("The recommended requirements are:")
        print(html2text(rec))

if __name__ == '__main__':
    compare()
