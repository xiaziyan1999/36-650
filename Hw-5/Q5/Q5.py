def make_pyramid(size):
    for i in range(0,size):
        for j in range(0,size-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")   
make_pyramid(5)
