import click
import platform
from html2text import html2text
from scraper import search

@click.command()
@click.argument("game")
@click.option("--rec", default=False, help="Choose this option for echoing recommended instead of minimal requirements.")
def compare(game: str, rec: bool):
    """
    The main function for comparing your sys requirements with the game's
    recommended requirements
    """

    click.echo(f'So, you want to run "{game}"...')
    click.echo("Collecting data...\n")

    id, nm, req = search(game)
    print(f"Closest match: {nm}, with app id: {id}")

    if req == []:
        click.echo(f"The game isn't selling on Steam for {platform.system()}.")
    
    else:
        if rec:
            rec = req["recommended"]
            print("The recommended requirements are:")
            print(html2text(rec))

        else:
            min = req["minimum"]
            print("The minimal requirements are:")
            print(html2text(min))

if __name__ == '__main__':
    compare()
