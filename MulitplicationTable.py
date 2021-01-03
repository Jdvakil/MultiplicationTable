"""
This program first collects the number 'N' which is an input from the user and puts it in the nested for loop and finds out the multiplication table of range
1 - number N, the tasks are subtasked and called by one main function at the bottom of the program. 
"""
#input
def get_input():
    N = int(input("enter the number"))
    return N
"""
This is the input function where the user inputs the number whose multiplication table is to be displayed
and returns the input."""
#process and output
def mt(N):
    print("X |", end='')
    for i in range(1, N+1):
        print('\t',i, end='')
    print("")
    print("_" * N*9)
    print('  |')
    for j in range(1, N+1):
        print(j,"|", end='\t ')
        for k in range(1, N+1):
            multiplication = j* k
            print(multiplication, end= '\t ')
        print("")
"""
This function is both the process and output. The function takes N as an argument and puts it in the aforementioned nested for loop, to process and display
the multiplication table of the number N
"""
        
        
def main():
    N = get_input()
    mt(N)
"""
This is the main function, where all the previous functions are called.
"""
if __name__ == "__main__":
    main()#This uses the idiom and calls the main function, that calls the other functions.
