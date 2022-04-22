
a  = input("Triplet for Alice: ")
a = list(a.split(" "))

b = input("Triplet for Bob:")
b = list(b.split(" "))

def compareTriplets(a,b):

    aResult=0
    bResult=0
    result=[] 
      
    for i in range(0,3):
        if(int(a[i]) > int(b[i])):      #a[0] > b[0] , so Alice receives 1 point.
            aResult += 1 
        elif(int(a[i]) < int(b[i])):    #a[0] < b[0], so Bob receives 1 point
            bResult += 1
        elif(int(a[i]) == int(b[i])):   #a[1] = b[1] , so nobody receives a point.
            continue 

    result.append(aResult)
    result.append(bResult)
    print(result)
                         
print(compareTriplets(a,b))
