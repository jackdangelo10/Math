i = 1
greaterDif = 0
equal = 0
bound = 1000;

#compares Collatz Conjcture height with my algorithm's height for all odd i up to bound
while (i < bound):
    height = 0
    a = i
    stepCount = 0
    original = a
    width = []
    widthCount = 0
    primeCount = 0

    #my algorithm
    while(a > 1):
        if((a-1) % 4 == 0 and ((a-1)/4) % 2 != 0):
            widthCount += 1
            a = (a-1)//4
            stepCount += 1
        elif((a-1) % 4 == 0 and ((a-1)/4) % 2 == 0):
            a = 2 * a + 1
            widthCount += 1
            stepCount += 1
        else:
            width.append(widthCount)
            widthCount = 0
            a = 6*a+3
            height += 1
            stepCount += 1
        width.append(widthCount);
    myCount = stepCount

    #collatz algorithm
    a = i
    heightCollatz = 0
    stepCount = 0
    while(a > 1):
        if(a % 2 == 0):
            a = a/2
            stepCount += 1
        else:
            stepCount += 1
            heightCollatz += 1
            a = 3 * a + 1
    collatzCount = stepCount

    if(myCount > collatzCount):
        greaterDif += 1
    if(height + 1 == heightCollatz):
        equal += 1

    #iterate to next odd
    i += 2
    
print("This many were larger than Collatz: ", greaterDif)
print("This many had same height: ", equal)
print("Remember that only odd numbers count as input despite iterative bounds")

