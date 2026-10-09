Python
scores = [72, 45, 90, 61, 38]

# Trackers for passes, failures, and running total
pass_count = 0
fail_count = 0
total_score = 0

# Loop through each score to evaluate grades and aggregate data
for score in scores:
    total_score += score
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Score: {score} - Grade: {grade}")
    
    # Track pass/fail count
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

# Calculate average
average = total_score / len(scores)

print(f"Passes: {pass_count}")
print(f"Fails: {fail_count}")
print(f"Average: {round(average, 1)}")
