def advanced_slice(): 

        # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    # a. Extract the letters 'hij'.
    # b. Extract every second letter starting from 'a' to 'm'.
    pass


alphabet = "abcdefghijklmnopqrstuvwxyz"

hij = alphabet[7:10]
hij_index = alphabet.index(hij)
print(hij_index)
every_second_letter = alphabet[0:13:2]
reversed_alphabet = alphabet[::-1]
print(reversed_alphabet)
