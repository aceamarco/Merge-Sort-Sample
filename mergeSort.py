#Author: Marco Acea

#Sorts any list, lst, containing comparable elements. 
def mergeSort(lst):
    #Base Case - If our list has 1 item or is empty -> return the list
    if len(lst) < 2:
        return lst
    else:
        #Continue splitting the list in half until it reaches the base case
        mid = len(lst) // 2
        left = mergeSort(lst[ : mid])
        right = mergeSort(lst[mid : len(lst)])

        #Assuming our halves are now sorted we begin merging them
        left_pointer = 0
        right_pointer = 0
        result = []

        while (left_pointer != len(left)) and (right_pointer != len(right)):
            left_value = left[left_pointer]
            right_value = right[right_pointer]

            #Adds the lower value to our result list and moves its pointer up
            if left_value < right_value:
                result = result + [left_value]
                left_pointer += 1
            else:
                #If they're equal it defaults to adding right_value
                result = result + [right_value]
                right_pointer += 1

        #Add what remains from either list to the result list
        if right_pointer == len(right): 
            result = result + left[left_pointer : len(left)]
        else:
            result = result + right[right_pointer : len(right)]
        
        return result

'''
Tests mergeSort(lst) using:
- A unsorted list (including negative elements)
- Empty list
- Characters (To test different data types)
- List containing duplicates
- Already sorted list
- Reverse sorted list
'''
def testMergeSort():
    print("Testing mergeSort ...", end = "")
    assert(mergeSort([3,-1,9,6]) == [-1,3,6,9])
    assert(mergeSort([]) == [])
    assert(mergeSort(["a", "c", "b"]) == ["a", "b", "c"])
    assert(mergeSort([9,1,1,1,7]) == [1,1,1,7,9])
    assert(mergeSort([1,2,3]) == [1,2,3])
    assert(mergeSort([3,2,1]) == [1,2,3])
    print("Passed!")

testMergeSort()