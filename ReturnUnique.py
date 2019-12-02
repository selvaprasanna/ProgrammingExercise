# Input: "Hello World" */
# Output: "HeWrd"


def get_unique_string(my_str):
    my_dict = {}
    unique_string=""
    for s in my_str:
        if s in my_dict:
            my_dict[s] = my_dict[s] + 1
        else:
            my_dict[s] = 1

    for each_dict in my_dict:
        if my_dict[each_dict] == 1:
            unique_string += each_dict

    return unique_string


print(get_unique_string("Hello World"))
