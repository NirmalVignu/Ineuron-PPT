import time

def timer(func):
    def inner():
        start_time=time.time()
        func()
        end_time=time.time()
        print(f"Time take to execute {func}() is {end_time-start_time}")
    return inner



@timer
def my_function():
    l=[]
    l=[i for i in range(1,101) if i%2==0]
    print("list of even numbers from 1 to 100000000000000000000000000000")
    print(l)

my_function()

    
'''
Output

list of even numbers from 1 to 100000000000000000000000000000
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
Time take to execute <function my_function at 0x000001D0DD4F7380>() is 0.038901567459106445

'''
