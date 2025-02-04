# naming convention
# 1. do not use reserved keywords (int, float, if, break)
# 2. we use snake_case for naming long variables
# 3. do not start variable name with numbers, but it's okay to use them in end or middle
# 4. only _ symbol is allowed in variable name (no: #, $, @, !, ...)
# 5. avoid using small names: l, O, s_n, ...

student_first_name = "Nick"
student_first_name_2 = "Leo" # this is ok
# 2_student_first_name # this is not ok
print(f'{student_first_name = }')
student_name = "Marry" # rather than s_n
length_of_person_name = len(student_name)
person_name_length = len(student_name)
print(f'{length_of_person_name = }')
print(f'{person_name_length = }')
