def count_chart(in_str):
    result = 0
    for i in in_str:
        result += 1
    return result
input_string = input('Input your string: ')
length_input_string = count_chart(input_string)
print('Length of string you typing is:',length_input_string)
