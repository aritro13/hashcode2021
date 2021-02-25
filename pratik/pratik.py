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
    output = "<count>\n"
    streetMap = {}
    
    temp = os.path.join(path, "{}.txt".format(eachFile))
    f = open(temp, "r")
    lines = f.readlines()
    simulationTime, numberOfIntersections, numberOfStreets, numberOfCars, score = map(int, lines[0].split(" "))

    intersections = [0] * numberOfIntersections

    for eachLine in lines[1:numberOfStreets+1]:
        t2 = eachLine.split(" ")
        streetMap[t2[2]] = [int(t2[3]), (int(t2[0]), int(t2[1])), 0]
        intersections[int(t2[1])] += 1

        # print("Streets:", eachLine)

    cars = [None] * numberOfCars
    count = 0
    for eachLine in lines[numberOfStreets+1:]:
        cars[count] = eachLine.replace("\n", "").split(" ")[1:]
        for eachCarStreet in cars[count]:
            streetMap[eachCarStreet][2] += 1
        # print("Cars:", eachLine)
        count += 1
        
    # print(streetMap)
    # print(intersections)
    # print(cars)

    count = numberOfIntersections
    for i in range(numberOfIntersections):
        if intersections[i] > 1:
            output += "{}\n{}\n".format(i, intersections[i])
            for eachStreet in streetMap.keys():
                if streetMap[eachStreet][1][1] == i:
                    output += "{} {}\n".format(eachStreet, streetMap[eachStreet][2] or 1)
        else:
            output += "{}\n{}\n".format(i, intersections[i])
            for eachStreet in streetMap.keys():
                if streetMap[eachStreet][1][1] == i:
                    output += "{} {}\n".format(eachStreet, streetMap[eachStreet][2] or 1)
    
    output = output.replace("<count>", str(count))
    # print(output)

    temp = os.path.join(path, "{}-out.txt".format(eachFile))
    f = open(temp, "w")
    f.write(output.strip())
    f.close()
    # break