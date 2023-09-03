# Name:
# Student number:

'''
There are many different ways to express the number e (Euler�s constant), which is 2.718281828459... 
One way is the following formula, which has an infinite number of fractions:
e= 2+1/(1+ 1/(2+ 2/(3+3/(4+4/(5+ 5/�)))))
Recursively, you can express this as: e = 2 + 1/cf(1)
where cf stands for �continued fraction,� which is defined as: cf(n) = n + n/cf(n+1)
For large n, this can be approximated by: cf(n) = n+1
Write a function approximate_e() which calculates the value of e using the formula given above. 
The function gets one parameter, which is the depth of the calculation (an integer valued zero 
or higher), i.e., the number of fractions that you include in the calculation. At the given depth, 
you approximate cf(n) by n+1. The function returns a float, which is the approximation of e.
At depth 0, you approximate cf(1) as 1+1, thus e is approximated by 2 + 1/(1+1) = 2.5
At depth 1, you approximate cf(2) as 2+1, and cf(1)=1+1/cf(2), thus e is approximated by
2 + 1/(1+1/(2+1)) = 2.75
Etcetera. You may choose whether to implement this function recursively or iteratively. 
The depth will not be higher than 100, so a recursive implementation should work.
'''
def approximate_e(depth):
    for i in range(depth):
        e = 2 + 1/(depth+

def main():
    print(approximate_e(0))     # 2.5
    print(approximate_e(1))     # 2.75
    print(approximate_e(5))     # 2.7182866556836904
    print(approximate_e(10))    # 2.7182818284466195
    print(approximate_e(100))   # 2.7182818284590455

if __name__ == "__main__":
    main()

