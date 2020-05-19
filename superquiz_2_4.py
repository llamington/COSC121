def englishize_word(word):
    """englishizes word"""
    suffix = word[-4:]
    if suffix[0] == 'b' and word[0] not in 'bcdfghjklmnpqrstvwxyz':
        text = f'(b{word[:-4]} or {word[:-4]})'
    else:
        text = word[-4] + word[:-4]
    return text


def englishize_sentence(sentence):
    """englishizes sentence"""
    words = sentence.split()
    english_words = [englishize_word(word) for word in words]
    return ' '.join(english_words) + '\n'


def englishize_file(filename, character_limit):
    """Englishizes file"""
    text = ''
    index = 0
    with open(filename) as file:
        lines = file.readlines()
        english_lines = [englishize_sentence(line) for line in lines]
        alen = len(english_lines[0])
        while alen <= character_limit and index < len(english_lines):
            text += english_lines[index]
            try:
                alen += len(english_lines[index + 1])
            except IndexError:
                pass
            index += 1
        if alen > character_limit:
            text += '<<Output limit exceeded>>'
        return text


ans = englishize_file('big_test.txt', 112)
print(ans)
