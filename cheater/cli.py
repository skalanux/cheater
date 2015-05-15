#   Cheater. Cheatsheet display from markdown notes
#   Copyright (C) 2015  Juan Manuel Schillaci
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
#   cheater 0.1, Copyright (C) 2014  Juan Manuel Schillaci
#   cheater comes with ABSOLUTELY NO WARRANTY.
#   This is free software, and you are welcome to redistribute it
#   under certain conditions;
from cheater.render import render_cheatsheets
import click

@click.command()

def main():
    """Cheater is a cheetsheet display app"""
    import ipdb; ipdb.set_trace()  # XXX BREAKPOINT
    render_cheatsheets()
    # Fixme: temporary imports, should be methods
    from cheater import app
