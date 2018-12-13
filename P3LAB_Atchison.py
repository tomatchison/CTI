# CTI-110 
# P3LAB - Debugging 
# Tom Atchison 
# 07 Oct 2018
#
#
def main():
    # This program will allow the user to input a numeric grade and then display
    # a letter grade
    # The system uses 10-point grading scale.
    # Variables to represent the grade thresholds.
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    # TO DO: define the rest of the scores.
    # Scores defined.
    # input numeric grade.
    score = int (input('Enter numeric grade: '))
    # output letter grade.
    # if-else statements properly indented.
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:    
            if score >= C_score:
                print ('Your grade is: C')
            else:
                if score >= D_score:
                    print ('Your grade is: D')
                else:
                    if score < D_score:
                        print('Your grade is: F')
            # TO DO: finish this.
            # Finished!


# program start
main()
