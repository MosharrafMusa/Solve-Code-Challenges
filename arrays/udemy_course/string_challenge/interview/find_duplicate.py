def find_dup(list1):
    l1 = []
    for i in list1:
        if i not in l1:
            l1.append(i)

        else:
            print(i, end=' ')


find_dup([1, 3, 5, 6, 5, 6])

# use set O(nlogn) and O(1)


def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']

print(checkIfDuplicates_1(listOfElems))


def checkIfDuplicates_2(listOfElems1):
    ''' Check if given list contains any duplicates '''
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)
    return False


listOfElems1 = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']

print(checkIfDuplicates_2(listOfElems1))
