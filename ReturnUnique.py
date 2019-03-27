# Input: "Hello World" */
# Output: "HeWrd"


def get_unique_string(my_str):
    my_dict = {}
    for s in my_str:
        if s in my_dict:
            my_dict[s] = my_dict[s] + 1
        else:
            my_dict[s] = 1

    for each_dict in my_dict:
        if my_dict[each_dict] == 1:
            print each_dict


get_unique_string("Hello World")
