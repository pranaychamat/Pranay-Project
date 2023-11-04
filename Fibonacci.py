def fibonacci(n):
    if n==0:
        print(0)
    elif n==1:
        print(0)
        print(1)
    else:
        k,s=0,1
        i=0
        while(i<n):
            print(k)
            i=i+1
            s=s+k
            if i == n :
                break
            else:
                print(s)
                i=i+1
                k=k+s

num = int(input("Enter any Positive Intrger no.: "))
if num < 0:
	print("Number is not valid")

print("Fibonacci Sequence upto {} term: ".format(num))
fibonacci(num)