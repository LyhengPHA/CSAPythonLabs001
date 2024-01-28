# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.




# Application 1
user_input = input("Enter any words: ")
user_input1 = list(user_input)
user_input2 = list(user_input)

user_input1_2 = [None]*(len(user_input1)+len(user_input2))
user_input1_2[::2] = user_input1
user_input1_2[1::2] = user_input2

user_str = ''. join(user_input1_2)
print(user_str)



# Application 2
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_input = input("Enter a range of letters (e.g., a-z):")
start, end = user_input.split("-")
start_letter = alpha.index(start)
end_letter = alpha.index(end)
result_string = alpha[start_letter:end_letter+1]

print(result_string)



