# This file contains base rates for different categories of errors by field.
# Based on the source code of the FEBRL project
# Link: http://users.cecs.anu.edu.au/~Peter.Christen/Febrl/febrl-0.3/febrldoc-0.3/manual.html

# https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass

@dataclass
class ErrorRate:
    '''Class that keeps track of different error rates.'''
    selection: float = 0.0
    misspell_file: str = ''
    misspelling: float = 0.0
    insertion: float = 0.0
    deletion: float = 0.0
    substitution: float = 0.0
    transpostition: float = 0.0
    swap_fields: float = 0.0
    swap_words: float = 0.0
    space_deletion: float = 0.0
    missing: float = 0.0
    new_val_prob: float = 0.0

givenname = {
    'selection' : 0.10,
    'misspell_file':'data'+os.sep+'givenname-misspell.tbl',
    'misspelling' : 0.30,
    'insertion':0.05,
    'deletion':0.15,
    'substitution':0.35,
    'transpostition':0.05,
    'swap_fields':0.02,
    'swap_words':0.02,
    'space_insertion':0.01,
    'space_deletion':0.01,
    'missing':0.02,
    'new_val_prob':0.02 # This guy might go away
    }
