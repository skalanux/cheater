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

import os
from itertools import cycle

CHEATSHEET_KEY_INDEX = 'name'
CHEATSHEET_KEY_FILE = 'filename'


def get_cheatsheets():
    # TODO: Make this a dynamic function that retrieves and indexes all
    # cheatsheets in a directory
    cheatsheets = []
    unexpanded_path = '~/.cheater'
    expanded_path = os.path.expanduser(unexpanded_path)
    path_exists = os.path.exists(expanded_path)

    if not path_exists:
        message = "There aren't any cheatsheets present."
        print(message)
        os.mkdir(expanded_path)
    else:
        for filepath in os.listdir(expanded_path):
            if filepath.endswith(".html"):
                cheatsheet_data = {}
                cheatsheet_data[CHEATSHEET_KEY_INDEX] = os.path.basename(filepath)
                cheatsheet_data[CHEATSHEET_KEY_FILE] = os.path.join(expanded_path,filepath)
                cheatsheets.append(cheatsheet_data)

    cheatsheet_cycle = cycle(cheatsheets)
    return cheatsheet_cycle
