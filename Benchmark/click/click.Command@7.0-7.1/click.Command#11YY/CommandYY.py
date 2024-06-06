import click
command = click.Command('my_command',  None,  None, params=[click.Option(['--param'], default=42)])
