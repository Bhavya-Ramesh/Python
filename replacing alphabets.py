def modify_string(s):
    result=""
    for char in s:
        frequency=s.count(char)
        new_char=chr((ord(char)-ord('a')+frequency)%26+ord('a'))
        result+=new_char
    return result
input_str=input("enter a string:")
output_str=modify_string(input_str)
print("output:",output_str)
