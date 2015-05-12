# cheater

Cheater is a cheetsheet display app


# Installation


** This has only been tested on ubuntu 14.04 with python 2.7 **

You need to have the webkit binding installed, on ubuntu:

    $ sudo apt-get install gir1.2-webkit2-3.0

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .

# Usage

First time you run the command, it will create a folder named "~/.cheater" and copy
a basic customizable stylesheet to render your cheatsheets. Markdown files need to
be placed under this directory, you could find some examples under the cheater/cheatsheets directory on this repository

To use it:

    $ cheater

