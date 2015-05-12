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
