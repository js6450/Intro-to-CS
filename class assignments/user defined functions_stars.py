#printing square stars

def sqr(h,w):
    for rows in range(h):
        for columns in range(w):
            print('*', end = '')
        print('')

#printing triangle stars

def tri(b):
    for trows in range(b):
        for tcolumns in range(trows + 1):
            print('*', end = '')
        print('')

#putting user-defined function under main
def main():
    
    h = int(input("please enter number of rows of stars you want: "))
    w = int(input("please enter number of columns of stars you want: "))

    b = int(input("please enter number of stars you want:"))

    sqr(h, w)
    tri(b)

main( )

