# find percentage of males and females in a class
# 22 Sep 2018
# CTI-110 P2HW2 - Male Female Percentage 
# Tom Atchison
#
# ask for number of males and number of females registered in a class.
# program should display percentage of males and females.
# hint 8 males and 12 females in a class.
# 20 students total.
# 8 / 20 = .4 or 40% for males
# 12 / 20 = .6 or 60% for females
# males + females = total 
# males / total * 100 = percentage males
# females / total * 100 = percentage females

# ask for total males, m
m = int( input ( "How many males are in the class? " ) )
# ask for total females, f
f = int( input ( "How many females are in the class? " ) )
# get total students, t
t = m + f
# get males percentage, mp
mp = (m / t ) * 100
# get female percentage, fp
fp = (f / t ) * 100
# show male percentage
print ( "Male percentage: " + str ( mp ) )
# female percentage
print ( "Female percentage: " + str ( fp ) )
