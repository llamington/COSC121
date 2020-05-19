"""asks the user for english words to latinize"""


def latinize_word(word):
    """performs bee latin on a word"""
    if word[0].lower() in 'bcdfghjklmnpqrstvwxyz':
        word = word[1:] + word[0] + 'uzz'
    else:
        word += 'buzz'
    return word.lower()


def latinize_sentence(sentence):
    """performs bee latin on a sentence"""
    words = sentence.split()
    latanized_words = [latinize_word(word) for word in words]
    return " ".join(latanized_words)


def main():
    """main function"""
    english_sentence = input('Enter English sentence: ')
    while english_sentence != 'q':
        print(f'Bee latin = {latinize_sentence(english_sentence)}')
        english_sentence = input('Enter English sentence: ')
    print(latinize_word('goodbye'))


main()