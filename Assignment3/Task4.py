"""TASK 4:
Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and print its type.
<br><br><em><strong>Hint:</strong> The bool() function alone won’t work as expected. 
Think about string comparison.</em>
"""
is_premium='True'
print(is_premium)
print(type(is_premium))

bool_type=bool(is_premium)
print(bool_type)
print(type(bool_type))