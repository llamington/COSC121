def latanize_word(word):
    """performs bee latin on a word"""
    if word[0].lower() in 'bcdfghjklmnpqrstvwxyz':
        word = word[1:] + word[0] + 'uzz'
    else:
        word += 'buzz'
    return word.lower()


def latinize_sentence(sentence):
    """performs bee latin on a sentence"""
    words = sentence.split()
    latanized_words = [latanize_word(word) for word in words]
    return " ".join(latanized_words)

