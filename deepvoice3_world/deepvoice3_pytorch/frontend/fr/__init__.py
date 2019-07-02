# coding: utf-8
from deepvoice3_pytorch.frontend.text.symbols import symbols
#import sys
#import nltk
from random import random

n_vocab = len(symbols)

#nltk.download('cmudict')
_xsampa = {}
_ipa = {}
with open("/lium/corpus/synthese/SynPaFlex-1.1/synpaflex-pronunciation-dictionary.txt") as fdict:
    for line in fdict:
        tab = line.split(';')
        word = tab[0]
        if word in _xsampa:
            continue
        else:
            _xsampa[word] = tab[1]
            _ipa[word] = tab[2]


def _maybe_get_arpabet(word, p):
    try:
        phonemes = _xsampa[word]
        #phonemes = " ".join(phonemes)
    except KeyError:
        return word

    return '{%s}' % phonemes if random() < p else word

def _dont_get_arpabet(word, phone, p):
    try:
        if phone == "\n":
            phonemes = word
        else:
            phonemes = phone
    except KeyError:
        return word
    return '{%s}' % phonemes if random() < p else word
    #return phonemes if random() < p else word

def mix_pronunciation(text, phonetic, p):
    phones = list(phone for phone in phonetic.split('§'))
    text_new = ''
    i = 0
    for word in text.split(' '):
        text_new += _dont_get_arpabet(word, phones[i], p)
        text_new += ' '
        i += 1
    return text_new

def text_to_sequence(text, phonetic, p=0.0):
	# 'text' = WordJTrans
	# Called during train.py.
    if p >= 0:
        text = mix_pronunciation(text, phonetic, p)
    from deepvoice3_pytorch.frontend.text import text_to_sequence
    text = text_to_sequence(text, ["french_cleaners"])
    return text

def text_to_sequence_original(text, p):
    from deepvoice3_pytorch.frontend.text import text_to_sequence
    text = text_to_sequence(text, ["french_cleaners"])
    return text
from deepvoice3_pytorch.frontend.text import sequence_to_text
