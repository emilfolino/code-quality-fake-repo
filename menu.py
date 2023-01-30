#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text analyzer menu module
"""
def build_full_menu(current_file):
    """Return full menu with ascii art"""
    return ascii_menu_art() + "\n" + command_list(current_file)

def ascii_menu_art():
    """Returns ascii of menu list"""
    return r"""
   ._________________.
   |.---------------.|
   || Text analyzer ||
   ||   -._ .-.     ||
   ||   -._| | |    ||
   ||   -._|"|"|    ||
   ||   -._|.-.|    ||
   ||_______________||
   /.-.-.-.-.-.-.-.-.\
  /.-.-.-.-.-.-.-.-.-.\
 /.-.-.-.-.-.-.-.-.-.-.\
/______/__________\___o_\ DrS
\_______________________/
    """


def command_list(current_file):
    """Returns string of menu choices"""
    return f"Current file -> {current_file}\n" r"""
Commands {
    menu -> prints menu?
    lines -> count lines
    words -> count words
    letters -> count letters
    word_frequency -> find 7 most used words
    letter_frequency -> find 7 most used letters
    all -> do all of the above
    change -> change file
    q -> quit
}>>>"""
