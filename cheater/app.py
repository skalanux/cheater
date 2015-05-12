#!/usr/bin/python
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


from gi.repository import Gio, Gtk, WebKit2

from cheatsheets_discovery import (CHEATSHEET_KEY_FILE, CHEATSHEET_KEY_INDEX,
                                   get_cheatsheets)

CHEATSHEETS = get_cheatsheets()


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cheater - cheatsheet discovery tool")

        self.label = Gtk.Label(label="Cheater", angle=24, halign=Gtk.Align.START, valign=Gtk.Align.START)

        self.set_border_width(10)
        self.set_default_size(400, 200)

        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.set_titlebar(self.hb)

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        self.hb.pack_end(button)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        btn_backwards = Gtk.Button()
        btn_backwards.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        btn_backwards.connect("clicked", self.on_btn_backwards_clicked)
        box.add(btn_backwards)

        btn_forward = Gtk.Button()
        btn_forward.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        btn_forward.connect("clicked", self.on_btn_forward_clicked)
        box.add(btn_forward)

        self.hb.pack_start(box)

        next_cheatsheet = CHEATSHEETS.next()
        doc = "file://" + next_cheatsheet[CHEATSHEET_KEY_FILE]
        self.hb.props.title = next_cheatsheet[CHEATSHEET_KEY_INDEX]
        self.view = WebKit2.WebView()
        self.view.load_uri(doc)
        self.add(self.view)

    def on_btn_forward_clicked(self, widget):
        next_cheatsheet = CHEATSHEETS.next()
        doc = "file://" + next_cheatsheet[CHEATSHEET_KEY_FILE]
        self.hb.props.title = next_cheatsheet[CHEATSHEET_KEY_INDEX]
        self.view.load_uri(doc)

    def on_btn_backwards_clicked(self, widget):
        next_cheatsheet = CHEATSHEETS.prev()
        doc = "file://" + next_cheatsheet[CHEATSHEET_KEY_FILE]
        self.hb.props.title = next_cheatsheet[CHEATSHEET_KEY_INDEX]
        self.view.load_uri(doc)

win = MainWindow()
win.set_opacity(0.9)
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
