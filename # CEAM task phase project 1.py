 # CEAM task phase project 1

# initialise the image
import random

def inputimage():
    image=[]
    innerimage=[]
    for i in range(0,5):
        for j in range (0,5):
            
            innerimage.append(random.randint(0,255))
        image.append(innerimage)
        innerimage=[]
    print("input image:")
    for i in image:
        print(i)
    return(image)
rows=5
columns=5
#invert function 
def invert(image):
    list2=[]
    list3=[]
    for i in image:
        for j in i:
            list2.append(255-j)
        list3.append(list2)
        list2=[]
    print("inverted list:")
    for i in list3:
        print(i)
    

#mirroring pixels for blur function
def mirror(index, size):
    if index < 0:
        return -index
    elif index >= size:
        return 2 * size - 2 - index
    return index
#mean blur with kernel that mirrors edge picels for smoother gradient and no harsh borders
def blur(image):
    blurred = []

    sum=0
    for i in range(0,5):
        newrow=[]
        for j in range(0,5):
            sum=0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    r = mirror(k, rows)
                    c = mirror(l, columns)
                    sum=sum+image[r][c]
                average=sum//9
            newrow.append(average)
        blurred.append(newrow)
    print("Blurred list:")
    for i in blurred:
        print(i)

#brightening the image
def brighten(image):
    newrow=[]
    newimage=[]
    p=str(input("Do you want to darken or brighten[D/B]:"))
    if p=="B":
        adjust=int(input("Darken by how many units?"))
        for i in image:
            newrow=[]
            for j in i:
                if adjust+j>255:#max brightness is 255
                    newrow.append(255)
                else:
                    newrow.append(j+adjust)
            newimage.append(newrow)
    elif p=="D":
            adjust=int(input("Darken by how many units?"))
            for i in image:
                for j in i:
                    if adjust>j:#min brightness will be zero
                        newrow.append(0)
                    else:
                        newrow.append(j-adjust)
                newimage.append(newrow)
                newrow=[]
    else:
        print("Invalid input")
    print("Changed image:")
    for i in newimage:
        print(i)
#geometric operations
#rotations
def rotate(image):
    clock=int(input("Rotate Anti-Clockwise or Clockwise [1/2]"))
    columns=5
    rows=5
    if clock==1:
        for i in range(0,rows):

            for j in range(0,columns):
                image[i][j],image[j][i]=image[j][i],image[i][j]#perform transpose
                for row in image:
                    row.reverse()
        print("rotated image:")
        for i in image:
                print(i)
    elif clock==2:
            for i in range(0,rows):
    
                for j in range(0,columns):
                    for row in image:#perform reverse of rows
                        row.reverse()
                    image[i][j],image[j][i]=image[j][i],image[i][j]#perform transpose
            print("rotated image:")
            for i in image:
                print(i)
    else:
        print("Invalid input")

#flipping an image
def flip(image):
    x=int(input("Do you want vertical or horizontal flip?[1/2]"))
    if x==1:
        for i in range(columns):
            for j in range(rows//2):
                image[j], image[rows-j-1] = image[rows-j-1], image[j] #vertically swapping column elements
        print("Vertically rotated image:")
        for i in image:
            print(i)
    elif x==2:
        for row in image:
            row.reverse() #using reverse function on list
        print("Horizontally rotated image:")
        for row in image:
            print(row)
    else:
        print("Invalid input")

def threshold(image,cutoff):
    result=[]
    
    for i in image:
        newrow=[]
        for j in i:
            if j>=cutoff:
                newrow.append(255)
            else:
                newrow.append(0)
        result.append(newrow)

    print("Image with threshold applied:")
    for i in result:
        print(i)
image=[]
while True: # MENU FOR PROGRAM
    z=int(input("""Welcome to image processor :
    1. For image invert
    2. For image brightening/darkening
    3. For image thresholding
    4. For image blurring
    5. For image rotation
    6. For image flip
    SELECT OPTION:"""))
    if z==1:
        image=inputimage()
        invert(image)
    elif z==2:
        image=inputimage()
        brighten(image)
        
    elif z==3:
        image=inputimage()
        cutoff=int(input("Enter threshold value:"))
        threshold(image,cutoff)
    elif z==4:
        image=inputimage()
        blur(image)
    elif z==5:
        image=inputimage()
        rotate(image)
    elif z==6:
        image=inputimage()
        flip(image)
    z=input("Do you want to terminate?[Y/N]")
    if z=="Y":
        break
    else:
        continue
        