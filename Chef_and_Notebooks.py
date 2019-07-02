# This is the solution for the problem Chef and Notebooks in CodeChef
# PYTHON 3.6

# print("X - Enter total number of pages used to write poetry.\n")
# print("Y - Enter the number of pages left to write the poetry.\n")
# print("N - Enter the number of notebooks, shopkeeper have.\n")
# print("K - Enter the total money left to spent by chef.\n")
# print("Pi - Number of pages ith rotebook have.\n")
# print("Ci - Cost of ith notebook.\n")

T = int(input("Enter the number of test cases: "))
x,y,n,k = input("Enter the values of X,Y,N,K respectively. \n").split()
X = int(x)
Y = int(y)
N = int(n)
K = int(k)

for x in range(T):
    for y in range(N):
        Pi,Ci = input("Enter the value of Pi and Ci: ").split()
        Pi = int(Pi)
        Ci = int(Ci)
        if Ci <= K:
            if Pi >= (X-Y):
                print("LuckyChef")
        else:
            print("UnluckyChef")


        

