age = 17
age_str= str(age)
message="I am "+ age_str +" years old"
print(message)
# str to int
num_str= "24"
num_int= int(num_str)
print(num_int)
#non numeric str to int
non_num_str = "Hello"
try:
    non_num_int = int(non_num_str)
    print(non_num_int)
except ValueError as e:
    print(f"Error: {e}")



