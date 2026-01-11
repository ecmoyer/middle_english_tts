# Read in line of text from terminal, return list containing words and meaningful characters
def read_terminal_input(phrase):
    word_list = []
    phrase = phrase.lower()

    word = ""
    for c in phrase:
        if c not in [" ", ".", ",", "!", "?", ";"]:
            word += c
        else:
            word_list.append(word)
            word = ""
            word_list.append(c)         

    if word != "":
        word_list.append(word)

    return word_list

# Convert list of words to list of lists; each sublist contains one word represented as phonemes
def word_list_to_phonemes(word_list):
    phoneme_list = []
    for word in word_list:
        if word in [" ", ".", ",", "!", "?", ";"]:
            if word == " ":
                phoneme_list.append(["short_pause"])
            elif word == "," or word == ";":
                phoneme_list.append(["medium_pause"])
            else:
                phoneme_list.append(["long_pause"])
        else:
            phonemes = word_to_phonemes(word)
            phoneme_list.append(phonemes)

    return phoneme_list

# Convert individual word to list of phonemes
def word_to_phonemes(word):
    word_phonemes = []
    position = 0

    while position < len(word):
        char = word[position]
        if char in ["'", "\""]:
            position += 1
        elif char in ["a", "e", "i", "o", "u", "y"]:
            characters_parsed = parse_vowel(word, position, word_phonemes)
            position += characters_parsed
        else:
            characters_parsed = parse_consonant(word, position, word_phonemes)
            position += characters_parsed

    return word_phonemes
    
# Parse phoneme abbreviation for vowels and add to list of phonemes in word, return number of characters covered by phoneme
def parse_vowel(word, position, phoneme_list):
    if position == 0 and len(word) != 1 and word[position] == "y":
        phoneme_list.append("gpp")
        return 1

    if position == (len(word) - 1) and word[position] == "e":
        phoneme_list.append("mcls")
        return 1
    else:
        if (word[position:(position + 1)]) in diphthong_dict:
            phoneme = diphthong_dict.get(word[position:(position + 1)])
            phoneme_list.append(phoneme)
            return 2
        elif (word[position:(position + 1)]) in double_letter_monophthong_dict:
            phoneme = double_letter_monophthong_dict.get(word[position:(position + 1)])
            phoneme_list.append(phoneme)
            return 2
        else:
            phoneme = single_letter_monophthong_dict.get(word[position])
            phoneme_list.append(phoneme)
            return 1
    
# Parse phoneme abbreviation for consonants and add to list of phonemes in word, return number of characters covered by phoneme
def parse_consonant(word, position, phoneme_list):
    if (position < (len(word) - 4)):
        # -cioun is pronounced see-oon
        if word[position:(position + 4)] == "cioun":
            phoneme_list.append("naf")
            phoneme_list.append("hftl")
            phoneme_list.append("hbtl")
            phoneme_list.append("van")
            return 5
    
    if (position < (len(word) - 2)):
        if word[position:(position + 2)] == "sch":
            phoneme_list.append("vef")
            return 3
    
    if (position < (len(word) - 1)):
        if word[position] == "c":
            if word[position + 1] in ["e", "i", "y"]:
                phoneme_list.append("naf")
                return 1
            elif word[position + 1] == "c":
                phoneme_list.append("nvs")
                return 2
            else:
                phoneme_list.append("nvs")
                return 1

        # Double consonants should not be pronounced twice separately
        if word[position] == word[position + 1]:
            phoneme = consonant_dict.get(word[position])
            phoneme_list.append(phoneme)
            return 2
        else:
            two_chars = word[position:(position + 1)]
            if two_chars == "ng":
                phoneme_list.append("vvn")
                phoneme_list.append("vvs")
                return 2
            elif two_chars == "wh":
                phoneme_list.append("ngf")
                phoneme_list.append("gvp")
            elif two_chars in ["ch", "gh", "sh", "th"]:
                phoneme = consonant_dict.get(two_chars)
                phoneme_list.append(phoneme)
                return 2
    
    if word[position] == "q":
        phoneme_list.append("nvs")
        phoneme_list.append("gvp")
        return 2
    
    phoneme = consonant_dict.get(word[position])
    phoneme_list.append(phoneme)
    return 1

# Diphthong spellings and corresponding phonemes
diphthong_dict = {
    "ai": "lfhf",
    "ay": "lfhf",
    "ei": "lfhf",
    "ey": "lfhf",
    "oi": "mbhf",
    "oy": "mbhf",
    "au": "lchb",
    "aw": "lchb",
    "ou": "mbhb",
    "ow": "mbhb",
    "eu": "hfhb",
    "ew": "hfhb"
}

# Two letter monophthong spellings and corresponding phonemes
double_letter_monophthong_dict = {
    "ij": "hftl",
    "ee": "mftl",
    "ie": "mftl",
    "oo": "mbll"
}

# Single letter monophthong spellings and corresponding phonemes
single_letter_monophthong_dict = {
    "a": "lbls",
    "e": "mftl",
    "i": "hftl",
    "o": "mbll",
    "u": "hbls",
    "y": "hftl"
}

# Consonant spellings and corresponding phonemes
consonant_dict = {
    "b": "vbs",
    "c": "nvs",
    "d": "vas",
    "f": "nlf",
    "g": "vvs",
    "h": "ngf",
    "j": "vea",
    "k": "nvs",
    "l": "lap",
    "m": "vbn",
    "n": "van",
    "p": "nbs",
    "r": "rap",
    "s": "naf",
    "t": "nas",
    "v": "vlf",
    "w": "gvp",
    "x": "nvs",
    "z": "vaf",
    "ch": "nea",
    "gh": "nvf",
    "sh": "vef",
    "th": "nif"
}