def length_of_last_word(s):
    # Remove leading and trailing whitespaces from the input string
    s = s.strip()
    # Find the index of the last occurrence of a space in the string
    last_space_index = s.rfind(' ')
    
    # If there are no spaces in the string, return the length of the entire string
    if last_space_index == -1:
        return len(s)
    # If there are spaces, return the length of the substring after the last space
    return len(s[last_space_index + 1:])
# Get input from the user
input_string = input("Enter a string: ")
# Call the function with the user-input string and print the result
result = length_of_last_word(input_string)
print(result)
    