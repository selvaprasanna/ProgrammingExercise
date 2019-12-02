def is_palindrome(input_str):
    str_length = len(input_str)
    end = str_length
    for i in range(0, int(str_length/2)):
        end = end - 1
        while not input_str[i].isalpha():
            i = i + 1
        while not input_str[end].isalpha():
            end = end - 1
        if input_str[i] != input_str[end]:
            print(i)
            print(end)
            print(input_str[i])
            print(input_str[end])
            return False
    return True


print(is_palindrome('never odd or even'))
