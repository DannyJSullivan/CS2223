#djsullivan-proj1
#Danny Sullivan
#This program is used to find the minimum and maximum value
#in a randomly generated array using a brute force method and
#a recursive method , along with the total time the function
#took to execute. There is an extra option to compare the
#final execution times of each method.

import random
import time
import sys
sys.setrecursionlimit(1000000)

#create an array
def createArray(x):
    arr = [random.randint(1,999999999) for i in range(0,x)] #array of x length with random numbers from 1 to 999999999
    return arr

#brute force method
def bruteForce(arr):
    nuMax = arr[0]                                          #set max to first element in arr automatically
    nuMin = arr[0]                                          #set min to first element in arr automatically
    if len(arr)==1:                                         #if array is only 1 in length, min and max are arr[0]
        print("The minimum value is: ", nuMin)
        print("The maximum value is: ", nuMax)
        return ""
    for i in range(1,len(arr)):                             #else, run linearly through rest of list
        if arr[i]>nuMax:                                    #if element is greater than max,
            nuMax=arr[i]                                    #set max to that number.
        elif arr[i]<nuMin:                                  #if element is less than min,
            nuMin=arr[i]                                    #set min to that number
    print("The minimum value is: ",nuMin)
    print("The maximum value is: ",nuMax)
    return ""

#time efficiency for brute force method
def effBF(x):
    print("Generating random array...")
    arr=createArray(x)                                                  #create rand arr
    #print(arr)
    print("Starting algorithm.")
    start=time.time()                                                   #start time
    bruteForce(arr)                                                     #run brute force
    end=time.time()                                                     #end time
    final=end-start                                                     #calculate total time
    print("Total time to execute algorithm: ", final, " seconds.")      #return total time
    return ""

#global vars
min1=999999999
max1=0

#divide and conquer
def minMax(arr,beg,end):                                    #param - array, beginning (0), end of array (len(arr)-1
    global min1                                             #declare global vars
    global max1
    if end-beg>2:                                           #if list is longer than 2
        minMax(arr,beg,(beg+end)//2)                        #recur down different params
        minMax(arr,(beg+end)//2,end)
    else:
        arr=arr[beg:end]                                    #slice out from sublist
        if end-beg==1:                                      #if only one index left
            arr.append(arr[0])                              #add back index 0
        max1=isBigger(max1,isBigger(arr[0],arr[1]))       #compare vals
        min1=isSmaller(min1,isSmaller(arr[0],arr[1]))     #compare vals
    return ""

#get larger
def isBigger(x,y):                     #compares two numbers, returns the larger of the two
    if x<y:
        return y
    else:
        return x

#get smaller
def isSmaller(x,y):                    #compares two numbers, returns the smaller of the two
    if x>y:
        return y
    else:
        return x

#print min and max for
def printMinMax():
    print("The minimum value is: ",min1)     #print global min
    print("The maximum value is: ",max1)     #print global max

#time efficiency for divide and conquer
def effDC(x):
    global min1,max1                                                    #get min and max
    print("Generating random array...")
    arr=createArray(x)                                                  #create random array with size of x
    #print(arr)
    print("Starting algorithm.")
    start=time.time()                                                   #start timer
    minMax(arr,0,len(arr)-1)                                            #runs div and conq on random array, index 0, and random pivot point
    end=time.time()                                                     #end timer
    final=end-start                                                     #get total time
    printMinMax()
    print("Total time to execute algorithm: ", final, " seconds.")      #return total time
    min1=999999999                                                      #reset min
    max1=0                                                              #reset max
    return ""

#time efficiency only returning time (bf)
def bf4Time(arr):
    nuMax = arr[0]                              #set max to first value
    nuMin = arr[0]                              #set min to first value
    if len(arr)==1:                             #case for array length of 1
        return ""
    for i in range(1,len(arr)):                 #run through array
        if arr[i]>nuMax:                        #compare arr[i] and max
            nuMax=arr[i]
        elif arr[i]<nuMin:                      #compare arr[i] and min
            nuMin=arr[i]
    return ""

#total time for brute force
def timeBF(arr):
    start=time.time()                                               #start timer
    bf4Time(arr)                                                    #run bruteForce
    end=time.time()                                                 #end timer
    final=end-start                                                 #get total time
    print("Brute force took: ", final, " seconds to execute.")      #print final time
    return final

#total time for divide and conquer
def timeDC(arr):
    global min1,max1                                                #declare global vars
    start=time.time()                                               #start timer
    minMax(arr,0,len(arr)-1)                                        #run quick sort on arr, index 0, and random pivot point
    end=time.time()                                                 #end timer
    final=end-start                                                 #get total time
    printMinMax()                                                   #print min and max of div and conq
    min1=999999999                                                  #reset global min
    max1=0                                                          #reset global max
    print("")
    print("Divide and conquer took: ",final," seconds to execute.") #print total time
    return final

#main functions
#exit
def exitLoop():
    z = input("Exit program? (y/n or yes/no): ")                        #get input
    if z == 'y' or z == 'yes':                                          #compare input
        print("Exiting program.")
        exit()                                                          #exit program
    elif z == 'n' or z == 'no':                                         #compare input
        print("Continuing program.")
        main()                                                          #go back to main
    else:                                                               #compare input
        print("Invalid input. Try again.")
        exitLoop()                                                      #recur
    return

#sample sizes
def sizeLoopBF():
    y = input("What sample size? (s/m/l, sm/med/lg, or small/medium/large): ")          #get input
    if y == 'sm' or y == 's' or y == 'small':                                           #compare input
        print(effBF(100000))                                                            #print result
        exitLoop()                                                                      #run exitLoop
    elif y == 'med' or y == 'm' or y == 'medium':                                       #compare input
        print(effBF(500000))                                                            #print result
        exitLoop()                                                                      #run exitLoop
    elif y == 'lg' or y == 'l' or y == 'large':                                         #compare input
        print(effBF(1000000))                                                           #print result
        exitLoop()                                                                      #run exitLoop
    elif y == 'quit' or y == 'exit' or y == 'q' or y == 'e':                            #compare input
        exitLoop()                                                                      #run exitLoop
    else:                                                                               #all other cases:
        print("Invalid input. Try again.")
        sizeLoopBF()                                                                    #recur
    return

def sizeLoopDC():
    y = input("What sample size? (s/m/l, sm/med/lg, or small/medium/large): ")          #get input
    if y == 'sm' or y == 's' or y == 'small':                                           #compare input
        print(effDC(100000))                                                            #print result
        exitLoop()                                                                      #run exitLoop
    elif y == 'med' or y == 'm' or y == 'medium':                                       #compare input
        print(effDC(500000))                                                            #print result
        exitLoop()                                                                      #run exitLoop
    elif y == 'lg' or y == 'l' or y == 'large':                                         #compare input
        print(effDC(1000000))                                                           #print result
        exitLoop()                                                                      #run exitLoop
    elif y == 'quit' or y == 'exit' or y == 'q' or y == 'e':                            #compare input
        exitLoop()                                                                      #run exitLoop
    else:                                                                               #all other cases:
        print("Invalid input. Try again.")
        sizeLoopDC()                                                                    #recur
    return

#compare fnc
def cmpLoop():
    y = input("What sample size? (s/m/l, sm/med/lg, or small/medium/large): ")          #get input
    if y == 'sm' or y == 's' or y == 'small':                                           #compare
        print("Generating a random array...")
        print("")
        a=createArray(100000)
        print("Brute Force: ")                                                          #print
        print("")
        print(bruteForce(a))
        bfTime=timeBF(a)
        #print(bfTime)
        print("")
        print("Divide and Conquer: ")
        print(minMax(a,0,len(a)-1))
        dcTime=timeDC(a)
        #print(dcTime)
        print("")
        if dcTime<bfTime:
            final = bfTime - dcTime
            print("Divide and conquer is faster than brute force by ", final, " seconds.")
        elif dcTime>bfTime:
            final=dcTime-bfTime
            print("Divide and conquer is faster than brute force by ", final, " seconds.")
        else:
            print("The times for brute force and divide and conquer are equal")
        #cmp(100000)
        exitLoop()                                                                      #exitLoop
    elif y == 'med' or y == 'm' or y == 'medium':                                       #compare
        print("Generating a random array...")
        print("")
        a = createArray(500000)
        print("Brute Force: ")  # print
        print("")
        print(bruteForce(a))
        bfTime = timeBF(a)
        #print(bfTime)
        print("")
        print("Divide and Conquer: ")
        print(minMax(a, 0, len(a) - 1))
        dcTime = timeDC(a)
        #print(dcTime)
        print("")
        if dcTime < bfTime:
            final = bfTime - dcTime
            print("Divide and conquer is faster than brute force by ", final, " seconds.")
        elif dcTime > bfTime:
            final = dcTime - bfTime
            print("Divide and conquer is faster than brute force by ", final, " seconds.")
        else:
            print("The times for brute force and divide and conquer are equal")
        # cmp(100000)
        exitLoop()  # exitLoop
    elif y == 'lg' or y == 'l' or y == 'large':                                         #compare
        print("Generating a random array...")
        print("")
        a = createArray(1000000)
        print("Brute Force: ")  # print
        print("")
        print(bruteForce(a))
        bfTime = timeBF(a)
        #print(bfTime)
        print("")
        print("Divide and Conquer: ")
        print(minMax(a, 0, len(a) - 1))
        dcTime = timeDC(a)
        #print(dcTime)
        print("")
        if dcTime < bfTime:
            final = bfTime - dcTime
            print("Divide and conquer is faster than brute force by ", final, " seconds.")
        elif dcTime > bfTime:
            final = dcTime - bfTime
            print("Divide and conquer is faster than brute force by ", final, " seconds.")
        else:
            print("The times for brute force and divide and conquer are equal")
        # cmp(100000)
        exitLoop()  # exitLoop
    elif y == 'quit' or y == 'exit' or y == 'q' or y == 'e':                            #compare
        exitLoop()                                                                      #exitLoop
    else:                                                                               #all other cases:
        print("Invalid input. Try again.")
        cmpLoop()                                                                       #recur
    return

#choose type
def mainFunc():
    x = input("Brute Force, Divide and Conquer, or Compare? (b, bf, or brute force || d, dc or divide and conquer || c, cmp, or compare): ")            #get input
    if x == 'bf' or x == 'b' or x == 'brute force':                                                                                                     #compare
        sizeLoopBF()                                                                                                                                    #sizeLoop
    if x == 'dc' or x == 'd' or x == 'divide and conquer':                                                                                              #compare
        sizeLoopDC()                                                                                                                                    #sizeLoop
    if x == 'quit' or x == 'exit' or x == 'q' or x == 'e':                                                                                              #compare
        exitLoop()                                                                                                                                      #sizeLoop
    if x=='c' or x=='cmp' or x=='compare':                                                                                                              #compare
        cmpLoop()                                                                                                                                       #cmpLoop
    else:                                                                                                                                               #all other cases
        print("Not a valid input. Try again.")
        mainFunc()                                                                                                                                      #recur
    return

#main
def main():
    mainFunc()                          #run mainFunc

#run main on run
if __name__=="__main__":
    main()                              #run main