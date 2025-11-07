def manipulating_words(): 

    # Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

    info = "Python is fun. Fun is good. Good is subjective."
    print(info.rfind ("subjective"))
    subjective_word = info[36:]
    print(subjective_word)