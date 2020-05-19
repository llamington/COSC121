def englishize_word(word):
    """englishizes word"""
    suffix = word[-4:]
    if suffix[0] == 'b' and word[0] in 'aeiou':
        return f'(b{word[:-4]} or {word[:-4]})'
    else:
        return word[-4] + word[:-4]


def englishize_sentence(sentence):
    """englishizes sentence"""
    words = sentence.split()
    english_words = [englishize_word(word) for word in words]
    return ' '.join(english_words)


sentence = "onuzz hankyoutuzz ibuzz ambuzz allergicbuzz otuzz eggsbuzz"
english = englishize_sentence(sentence)
print(english)