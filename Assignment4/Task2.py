#TASK 2: Given the product name ' OnePlus Nord-CE 3 ',
# write code to clean it by removing extra spaces, converting all letters to uppercase, and replacing the dash with a colon.
# <br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>

product_name=" OnePlus Nord-CE 3 "

print(product_name.strip())
print(product_name.upper())
print(product_name.replace("-",":"))