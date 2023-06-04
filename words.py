# for a list of words, print out each word on a separate line, but in all uppercase.
# turn that into a function, print_upper_words. Test it out. (Dont forget to add a docstring to your function!)
# change that function so that it only prints words that start with the letter 'e' (either upper or lowercase)
# Make your function more general you should be able to pass in a set of letters and it only prints words that start with the letter 'e' (either uppercase or lowercase)

def print_upper_words(word_list, letters):
    """prints out a new list of words that are uppercase and start with the set of letters passed in  """
    uppercase_word_list = []
    letters_string = ''.join(letters)
    for word in word_list:
        if any(word.startswith(letter) for letter in letters):
            uppercase_word = word.upper()
            uppercase_word_list.append(uppercase_word)
    print(uppercase_word_list)


print_upper_words(["mango", "orange", "dragonfruit"], ["d", "o"])
