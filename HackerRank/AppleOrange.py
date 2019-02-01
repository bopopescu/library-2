


def countApplesAndOranges(s, t, a, b, apples, oranges):
    samsHouseStart = s
    samsHouseEnd = t
    appleTreeLocation = a
    orangeTreeLocation = b

    apples_land_on_sams_house = 0

    for apple in apples:
        x_location = appleTreeLocation + apple
        if x_location >= samsHouseStart and x_location <= samsHouseEnd:
            apples_land_on_sams_house += 1

    oranges_land_on_sams_house = 0
    for orange in oranges:
        x_location = orangeTreeLocation + orange
        if x_location >= samsHouseStart and x_location <= samsHouseEnd:
            oranges_land_on_sams_house += 1

    print(apples_land_on_sams_house)
    print(oranges_land_on_sams_house)


s = 2
t = 3
at = 1
ot = 5  # location of apple and orange tree
apples = [2]
oranges = [-2]
countApplesAndOranges(s, t, at, ot, apples, oranges)