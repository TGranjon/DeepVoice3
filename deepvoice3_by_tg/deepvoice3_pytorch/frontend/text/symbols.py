'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
#from .cmudict import valid_symbols

_pad = '_'
_eos = '~'
_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÀÉÈÙÎÔÛÊÇabcdefghijklmnopqrstuvwxyzàéèùûîêôç!\'(),-.:;? []"«»—–'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
#_arpabet = ['@' + s for s in valid_symbols]
# Export all symbols:
#symbols = [_pad, _eos] + list(_characters) + _arpabet
valid_symbols = [
    'i', 'e', 'E', 'a', 'A', 'O', 'o', 'u', 'y', '2', '9', '@',
    'e~', 'a~', 'o~', '9~', 'E~', 'A~', 'O~',
    'p', 'b', 't', 'd', 'k', 'g',
    'f', 'v', 's', 'z', 'S', 'Z', 'j',
    'l', 'R', 'w', 'H',
    'm', 'n', 'J', 'N',
]

# Prepend "%" to Xsampa symbols to ensure uniqueness (some are the same as uppercase letters):
_xsampa = ['+' + s for s in valid_symbols]

# Export all symbols:
symbols = [_pad, _eos] + list(_characters) + _xsampa
