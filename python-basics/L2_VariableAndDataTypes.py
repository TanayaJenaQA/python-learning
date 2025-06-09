# formatting the code : ctrl + alt + l
name = "Tanay"  # String
age = 18  # Int
height = 5.5  # variable that holds float data
grade = 'A' # string variable
is_present = True # boolean
subjects = ["math", "science", "english"]  # list variable
friends = ("Ram", "hari", "naveen")  # tuple variable
__SCHOOL__ = "MKC HIGH SCHOOL"  # constant
set_data = {1, 2, 3, 5}  # set variable
dict_data = {"name": "Tanay", 1: "Bus Number"
             }  # dictionary

a, b, c = 1, 2, " data"  # assign multiple variable in single line

print(
    f"name : {name}\n age : {age} \n height :{height}\n grade: {grade}\n "
    f"subject: {subjects}\n friend names: {friends} \n"
    f"Constant School Name : {__SCHOOL__} a : {a} b : {b} c :{c}"
    f"dict : {dict_data.get("name")}")
print("_" * 50)
print(
    f"name type: {type(name)}\n age type: {type(age)} \n height type:{type(height)}\n grade type: {type(grade)}\n "
    f"subject type: {type(subjects)}\n friend names type : {type(friends)} \n"
    f"Constant School Name type: {type(__SCHOOL__)} a type: {type(a)} b type: {type(b)} c type:{type(c)}"
    f"dict type: {type(dict_data.get("name"))}  set type:{type(set_data)} \n"
    f"type of is_present: {type(is_present)}")


