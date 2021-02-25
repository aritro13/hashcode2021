# streetMap = {
#     "streetname1": (LTime, (intersection1, intersection2))
#     "streetname2": (LTime2, (intersection1, intersection2))
# }
# cars = {
#     "a" : [path1, path2, path3]
#     "b" : [path5, path6]
# }
# traffic = []

import os
path = "../Problem Statement"
# path = "Problem Statement"
files = ['a','b','c','d','e','f']

 
for eachFile in files:
    streetMap = {}
    temp = os.path.join(path, "{}.txt".format(eachFile))
    f = open(temp, "r")
    lines = f.readlines()
    simulationTime, numberOfIntersections, numberOfStreets, numberOfCars, score = map(int, lines[0].split(" "))

    for eachLine in lines[1:numberOfStreets+1]:
        t2 = eachLine.split(" ")
        streetMap[t2[2]] = (int(t2[3]), (int(t2[0]), int(t2[1])))
        # print("Streets:", eachLine)
    print(streetMap)

    cars = [None] * numberOfCars
    count = 0
    for eachLine in lines[numberOfStreets+1:]:
        cars[count] = eachLine.replace("\n", "").split(" ")[1:]
        # print("Cars:", eachLine)
        count += 1
    print(cars)

    data = f.read()
    f.close()
    print(data)