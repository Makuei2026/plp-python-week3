count = 1
total = 0

# BUG: Missing colon ':' at the end of the while loop statement. Fixed by adding a colon after 'count <= 5'.
# BUG: The condition 'count < 5' stopped execution before reaching 5. Fixed by changing condition to 'count <= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate string with int using '+'. Fixed by converting total to string using str(total).
print("Sum of 1 to 5 is: " + str(total))
