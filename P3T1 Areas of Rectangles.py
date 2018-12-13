# Find area of two rectangles
# 07 Oct 2018
# CTI-110 P3T1: Areas of Rectangles 
# Tom Atchison
#
# ask for length and width of 2 rectangles.
# find: area = length * width
# tell user which rectangle has greater area or if they are equal.
# does the first rectangle have the larger area?
# does the second rectangle have the larger area?
# do both rectangles have equal area?
def main():
    # Input length and width of rectangle 1.
    length1 = float (input('What is the length of rectangle 1? '))
    width1 = float (input('What is the width of rectangle 1? '))
    # Find area for rectangle 1 using area1 = length1 * width1.
    area1 = length1 * width1
    # Output the area of rectangle 1.
    print ('The area of rectangle 1 is', area1)
    # Input length and width of rectangle 2.
    length2 = float (input('What is the length of rectangle 2? '))
    width2 = float (input ('What is the width of rectangle 2? '))
    # Find area for rectangle 2 using area2 = length2 * width2.
    area2 = length2 * width2
    # Output the area of rectangle 2.
    print ('the area of rectangle 2 is', area2)
    # Output which rectangle has the larger area or are they equal?
    if area1 > area2:
        print ('Rectangle 1 has the larger area.')
    if area1 == area2:
        print ('Rectangle 1 and rectangle 2 have the same area.')
    else:
        print ('Rectangle 2 has the larger area.')
main()
