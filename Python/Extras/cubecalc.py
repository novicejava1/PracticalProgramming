def cubeCalc(a):
    listOfValues = ['height', 'width', 'depth']
    listOfNo = []
    if a == 1:
        for i in range(len(listOfValues)):
            listOfNo.append(int(input("Input the "+str(listOfValues[i])+"(cm): ")))
        print("The volume is",listOfNo[0]*listOfNo[1]*listOfNo[2],"cm³")
        print("The total surface area is",(listOfNo[0]*listOfNo[2])*6,"cm²")
    elif a == 2:
        pass
    
    
def pyramidCalc():
    pass

#main

selection = int(input("Input your selection. 1 for cubes. 2 for pyramids: "))

if selection == 1:
    whichDimension = int(input("Calculations for 3d (1) or 2d (2) shape?: "))
    print("\r")
    cubeCalc(whichDimension)
elif selection == 2:
    pyramidCalc()
