#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

#I'm to lazy to do anthing else 

import random
import sys
import re


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    f=open(filename,"r+")
    r="(?:-{2})|(?:[\W]'[\W])|(?:[\W]')|(?:'[\W])?[^a-zA-Z0-9'-]+"
    all_words_list = []
    mimic_dict = {}
    last_word_check = False
    last_word = ""

    for line in f.readlines():
        new_line = filter(None,re.compile(r).split(line))
        all_words_list.extend(new_line)
        for (i, key_word) in enumerate(new_line):
            if last_word_check:
                mimic_dict.setdefault(last_word, []).append(key_word)
                last_word_check = False
            if i != len(new_line)-1:
                mimic_dict.setdefault(key_word, []).append(new_line[i+1])
            else:
                last_word_check = True
                last_word = key_word



    f.close()Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (9/9), 56.56 KiB | 56.56 MiB/s, done.
Total 9 (delta 0), reused 7 (delta 0)
To github.com:nate998877/backend-mimic-assessment.git
 * [new branch]      master -> master
(base) nate@debian:/mnt/Files/Programming/School_Project/Q3/mimic$ git checkout -b dev
Switched to a new branch 'dev'
(base) nate@debian:/mnt/Files/Programming/School_Project/Q3/mimic$ 

    return mimic_dict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    # print(mimic_dict[word][random.randrange(len(mimic_dict[word]))])
    for rand_word in mimic_dict[word]:
        print(rand_word)


# Provided main(), calls mimic_dict() and mimic()
def main():
    """hard coding values for bugtesting I won't remove"""

    d = mimic_dict("alice.txt")
    print_mimic(d, 'Geography')


if __name__ == '__main__':
    main()

