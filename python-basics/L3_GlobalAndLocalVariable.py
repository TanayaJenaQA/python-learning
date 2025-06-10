my_std_name = "Rohit"

print(my_std_name)  # Rohit


def get_name():
    print(my_std_name)


get_name()  # Rohit


def get_name_with_local_var():
    my_local_var = "Ratna"
    global my_std_name
    my_std_name = "Rahul"
    print(my_local_var)
    print(my_std_name)


get_name_with_local_var()  # Ratna RAHUL
get_name()  # Rahul
