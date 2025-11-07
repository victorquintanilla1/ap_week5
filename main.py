# refactoring means to
#restructure code without
# charging its external behavior
# This helps imrpove code readability
# and maintainability
# importing the functions
from problem_set1 import problem1
from advanced import advanced_slice
#call the functions
problem1() # this is 
# an abstract representation
# of the function.
advanced_slice()

# c. Reverse the entire string using slicing.

from extracting_info import extracting_info

from manipulating_words import manipulating_words

from string_methods import string_methods

from  import 


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
















sentence = "Life is what happens when you are busy making other plans."
replaced_busy = sentence.replace("busy", "distracted")
replaced_plans = sentence.replace("plans", "mistakes")


word = "Iteration"
repeated_word = word * 7


quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
has_moonlight = "moonlight" in quote2


phrase = "Supercalifragilisticexpialidocious"
num_chars = len(phrase)
count_i = phrase.count('i')