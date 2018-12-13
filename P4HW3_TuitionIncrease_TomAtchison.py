# Write program with loop that displays projected semester tuition over 
# 5 years
# 26 October 2018
# CTI-110 P4HW3 - Tuition Increase
# Tom Atchison

# tuition is $8000 with a 3% increase each yr for the next 5 yrs.
# increase = (8000 * .03) for 5 yrs 

# Assign value.
tuition = 8000
# Print title.
print("$8000.00 tuition with 3% increase over 5 years.")
# Add space.
print()
# Print table heading.
print("year\t tuition")
print("-----------------")
# Use for loop for output of tuition totals for 5 consecutive years
# with a 3% increase each year.
for year in range(1, 6): 
    tuition += (.03) * tuition
    print(year, "\t", "$",format(tuition, ".2f"))    
    


