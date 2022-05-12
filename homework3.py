ballEnergy = int(input("The ball energy:"))

arr = []
for index in input("The heights of the legos:").split():
    arr.append(int(index))
#print(arr)


def calculateEnergy(ballEnergy, arr):
    i = 0
    for i in range(ballEnergy + 1):
        j = 0
        delta = 0
        deltaValues = []
        if( ballEnergy > arr[i] ):
            for j in range(ballEnergy):
                delta = ballEnergy - arr[j]
                deltaValues.append(delta)
                #print(f"delta values: {deltaValues}")   
                ballEnergy = ballEnergy + delta
                #print(f"ball energy: {ballEnergy}")
                #print(f"new delta value: {delta}")
            return deltaValues[-1]   
        
        else:
            for j in range(ballEnergy): 
                delta = ballEnergy - arr[j]
                deltaValues.append(delta)
                #print(f"delta values: {deltaValues}")
                ballEnergy = ballEnergy + delta
                #print(f"ball energy: {ballEnergy}")
                #print(f"new delta value: {delta}")
            return int(deltaValues[-1]) 
        
        
print(calculateEnergy(ballEnergy, arr))


if(calculateEnergy(ballEnergy, arr) < 0):
    print(f"The minumum starting ball energy: {ballEnergy + 1}")
elif(calculateEnergy(ballEnergy, arr) > 0):
    print(f"The minumum starting ball energy: {ballEnergy - 1}")
else:
    print(f"The minumum starting ball energy: {ballEnergy}")