# -*- coding: utf-8 -*-
"""
 Note: This script was borrowed in part from:
 https://github.com/DjangoGirls/resources/tree/master/cheatsheets
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
from os import path
import shutil

import jinja2
import markdown


def get_template(template_name):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

    return env.get_template(template_name)


BASE_URL = path.abspath(path.dirname(__file__))

def render_cheatsheets():
    unexpanded_path = '~/.cheater'
    expanded_path = os.path.expanduser(unexpanded_path)
    path_exists = os.path.exists(expanded_path)
    if not path_exists:
        message_1 = 'Creating cheatsheet directory {} for cheater on , please put some markdown files on it and then rerun this command. You can find some examples inside de cheatsheet directory of the github repository'.format(expanded_path)
        message_2 = 'Copying base stylesheet, modify it to suit your needs'
        print(message_1)
        os.mkdir(expanded_path)
        print(message_2)
        stylesheet_path = os.path.join(BASE_URL, 'cheatsheets', 'stylesheet.css')
        shutil.copy(stylesheet_path, expanded_path)
    else:
        for filepath in os.listdir(expanded_path):
            if filepath.endswith(".md"):
                try:
                    print('Converting markdown to HTML...')
                    markdown_filename = os.path.join(expanded_path, filepath)
                    with open(markdown_filename) as f:
                        raw_markdown = f.read()

                    filename_noext, _ = path.splitext(markdown_filename)
                    html_filename = '%s.html' % filename_noext

                    print('Converting markdown to HTML...')
                    html = markdown.markdown(raw_markdown, output='html5')
                    print('Done.')

                    template = get_template('cheatsheets/template.html')

                    print('Rendering template...')
                    rendered = template.render({
                        'html': html,
                    })

                    print('Done.')

                    print('Writing HTML file...')
                    with open(html_filename, 'w+') as f:
                        f.write(rendered)
                    print('Done.')
                except:
                    print('Failed to render HTML file for {}...'.format(markdown_filename))

if __name__=="__main__":
    render_cheatsheets()
