# Name:
# Student number:

# The function gets a positive integer number, and a list of positive
# integers weights. It calculates the weighted 11-proof control digit
# for number, and returns it. Calculation is as follows (detailed
# description in the written exercise): if the number is ABCDE and the
# weights are [X,Y,Z], then calculate sum S as X*E+Y*D+Z*C+X*B+Y*A.
# R is the remainder when you divide S by 11. For R is 0 or 1, return R.
# Else return 11-R.
def weighted11proof( number, weights ):
    return -1

def main():
    print( weighted11proof( 619,     [2, 4, 8, 7]           ) ) # 7
    print( weighted11proof( 30000,   [2, 4, 8, 7]           ) ) # 5
    print( weighted11proof( 612053,  [2, 4, 8, 7]           ) ) # 0
    print( weighted11proof( 123456,  [1, 2, 3, 4, 5, 6]     ) ) # 1
    print( weighted11proof( 123456,  [6, 5, 4, 3, 2, 1]     ) ) # 8
    print( weighted11proof( 111111,  [1]                    ) ) # 5
    print( weighted11proof( 1234567, [2,4,8,5,10,9,7,3,6,1] ) ) # 1 
                        
if __name__ == "__main__":
    main()
