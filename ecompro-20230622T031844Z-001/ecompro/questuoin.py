'''r =int(input("enter\n"))
a = 0
i = 0
l = int (input('enter\n'))
for i in range(l,r-1):
    if i % 2!=0:
        a = max(i,1)
print('\n',a,'\n')
'''

'''arr = [1,2,3,5]
sum2 = 0
x = 0
n  = len(arr)
sum1=((n)*(n+1))/2
for i in range(0,n):
    sum2=sum2+arr[i]
    x = int(sum1-sum2)
print(x+5)
'''

# Find Missing Element
'''
def findMissing(arr, N):
   
    # create a list of zeroes
    temp = [0] * (N+1)
    print(temp)
 
    for i in range(0, N):
        temp[arr[i] - 1] = 1
 
        for i in range(0, N+1):
            if(temp[i] == 0):
                ans = i + 1
 
    print(ans)
 
# Driver code
if __name__ == '__main__':
    arr = [1, 2, 4,5,6 ]
    N = len(arr)
 
    # Function call
    findMissing(arr, N)

'''
'''string = "abaaa"
a = sorted(string)
count = 0
count = str(count)
for i in range (len(string)):
    if a==string:
        count+=count
print(i)
'''
'''
n = 5
arr = [100,180,260,310,40,535,695,7]
count = 0
max_num = arr[0]
min_num = arr[0]
for i in range(0,n):
    if arr[i]>=max_num:
        max_num = arr[i]
    if arr[i]<=min_num:
        min_num = arr[i]
if max_num>min_num:
    count = count+1
print(count)
'''

''' 
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
 
 
# Driver code
if __name__ == '__main__':
    S1 = "hrushikesh"
    S2 = "hrushi"
    print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))
    '''
alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet_values = {alpha: value for alpha, value in zip(alphabets, range(1, 27))}
print(alphabet_values)
