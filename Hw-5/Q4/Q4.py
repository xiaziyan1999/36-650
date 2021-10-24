def make_triangle(digit):
    i=1
    j=1
    if isinstance(digit,float):
        print("“Invalid Input")
    elif digit>0:
        while i<(digit+1):
            for m in range(j,j+i):
                print(m,end=" ")
            i+=1
            j=j+i-1
            print("\r")
    else:
        print("“Invalid Input")

make_triangle(6)