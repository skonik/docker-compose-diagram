import click

from docker_compose_diagram.draw import draw


@click.command()
@click.option('--file', default='docker-compose.yml', help='docker-compose file')
@click.option('--direction', default="TB", type=click.Choice(["TB", "BT", "LR", "RL"], case_sensitive=True))
def main(file, direction):
    draw(file, direction)


if __name__ == '__main__':
    main()
