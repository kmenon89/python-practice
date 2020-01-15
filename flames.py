def strToList(s):
    strList = []
    for i in s:
        if i != " ":
            strList.append(i)
    return strList


def uniqueLetters(str1, str2):
    n1 = strToList(str1)
    n2 = strToList(str2)
    # remove the leters common in both names
    removeList = []
    for x in n1:
        if x in n2:
            removeList.append(x)
            n2.remove(x)

    for x in removeList:
        n1.remove(x)
    # combine the remaining letters and get the count of letters
    return n1 + n2


def flamesAlphabetMath(count):
    if count < 1:
        return "_"
    STRING = ["F", "L", "A", "M", "E", "S"]
    print(STRING)
    removeIdx = 0
    while len(STRING) > 1:
        strLen = len(STRING)
        removeIdx = (count % strLen) + (removeIdx - 1)
        removeIdx = removeIdx % strLen
        STRING.pop(removeIdx)
        print(STRING)

    return STRING[0]


def flamesAlphabetWhileLoop(count):
    if count < 1:
        return "_"
    STRING = ["F", "L", "A", "M", "E", "S"]
    print(STRING)
    ctr = 0
    idx = 0
    while len(STRING) > 1:
        ctr += 1
        if ctr == count:
            ctr = 0
            STRING.pop(idx)
            print(STRING)
            idx -= 1

        idx += 1
        if idx >= len(STRING):
            idx = 0

    return STRING[0]


def flames(name1, name2):
    unique = uniqueLetters(name1, name2)
    STRING_DIC = {
        "_": "None",
        "F": "Friends",
        "L": "Love",
        "A": "Anger",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sister"
    }
    count = len(unique)
    print(name1, name2)
    print("unique:", unique)
    print("count:", count)
    result = flamesAlphabetMath(count)
    print(STRING_DIC[result])
    print("\n\t ========== \n")

flames("kbn", "km")
flames("kamaleshwar", "kavitha")
flames("kamaleshwar nair", "kavitha menon")
flames("kamaleshwar bn", "kavitha menon")
