
def palidrome(n):
    return n==n[::-1]

n='radar'

ans=palidrome(n)

if ans:
    print("yes")

else:
    print("no")


