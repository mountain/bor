# -*- coding: utf-8 -*-


sizes = {
    'huge': 48,
    'large': 42,
    'normal': 36,
    'small': 30,
    'tiny': 24,
}

fontnames = [
]

with open('metafont-names.txt') as f:
    for line in f:
        fontnames.append(line.strip())
