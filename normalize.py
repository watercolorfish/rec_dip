from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def encode_sequences(tokenizer, length, lines):
    print("toke")
    print(tokenizer)
    print(lines)
    seq = tokenizer.texts_to_sequences(lines)
    seq = pad_sequences(seq, maxlen=length, padding='post')
    return seq

def read(filename):
    with open(filename, mode='rt', encoding='utf-8') as file:
        text = file.read()
        sents = text.strip().split('\n')
        return [i.split('\t') for i in sents]

def get_syllable(n, tokenizer):
    if n == 0:
        return ""
    for syllable, index in tokenizer.word_index.items():
        if index == n:
            return syllable
    return ""
