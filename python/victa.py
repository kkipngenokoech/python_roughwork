def smallestPositive(array):
    # extract the maximum value in the array and the minimum value too
    maximumValue = max(array)
    minimumValue = min(array)

    # start iterating over the array - set the smallest positive to the minimum value in the array if the number is greater than zero
    if minimumValue > 0:
        smallestPositiveNumber = minimumValue
    else:
        if maximumValue > 0:
            minimumValue = 1
            smallestPositiveNumber = 1
        else:
            smallestPositiveNumber = 1
            print(smallestPositiveNumber)
            return 0
            
    while minimumValue < maximumValue:
        if (smallestPositiveNumber in array):
            smallestPositiveNumber += 1
            minimumValue += 1
    if smallestPositiveNumber == maximumValue:
        smallestPositiveNumber += 1

    # account for situation where smallest positive number is equal to maximum value
    print(smallestPositiveNumber)
array = [1, 3, 6, 4, 1, 5, 2]
negativeArray = [-1,-4,-7]
smallestPositive(array)
smallestPositive(negativeArray)