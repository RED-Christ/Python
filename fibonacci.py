import sys

def fibonacci(a):
    global c_0_, c_1_
    if(a==0):
        c_0_ += 1
        return 0
    elif(a==1):
        c_1_ += 1
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)


n = int(sys.stdin.readline())
for i in range(n):
    c_0_ = 0
    c_1_ = 0
    fibonacci(int(sys.stdin.readline()))
    print(c_0_,c_1_)
