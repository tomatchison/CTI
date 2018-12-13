# This project counts the total of bugs collected over 5 days.
# 26 October 2018
# CTI-110 P4T2 - Bug Collector
# Tom Atchison


# Input bugs collected per day for 5 days.
# Display 5 day total.

# Initialize accumulator.
total = 0
# Get number of bugs collected for each day.
for day in range (1, 6):
    print ("Enter the number of bugs collected for day", day)
    bugs = int(input())
    total += bugs
# Display total bugs.
print ("Congratulations! You collected a total of", total, "bugs")
