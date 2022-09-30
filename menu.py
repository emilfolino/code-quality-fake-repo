#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menu for the analyzer program
"""


def print_menu():
    """
    Prints menu for the analyzer program
    """
    analyzer_image = r"""
     ____________________________
    !\_________________________/!\
    !!                         !! \
    !!                         !!  \
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  !
    !!                         !!  /
    !!_________________________!! /
    !/_________________________\!/
       __\_________________/__/!_
      !_______________________!/
    ________________________
   /oooo  oooo  oooo  oooo /!
  /ooooooooooooooooooooooo/ /
 /ooooooooooooooooooooooo/ /
/C=_____________________/_/

    """


    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(analyzer_image)
    print("lines) Count the number of lines.")
    print("words) Count the number of words.")
    print("letters) Count the number of letters.")
    print("word_frequency) Find 7 most used words.")
    print("letter_frequency) Find 7 most used letters.")
    print("all) Do everything.")
    print("change) Change text file.")
    print("q) Quit.")
