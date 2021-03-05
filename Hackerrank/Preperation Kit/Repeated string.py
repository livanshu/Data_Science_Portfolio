# First approach
# do not work when n > 10^6
# Complete the repeatedString function below.
def repeatedString(s, n):
    if n < 10^6:
        a =s*n 
        b = a[0:n]
        count = b[0:n].count('a')
    else:
        count = n    
     
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

    
#Second approach
