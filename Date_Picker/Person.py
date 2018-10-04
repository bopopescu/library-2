import random
from Date_Picker.dbconnect import *

class Female:
    def __init__(self, age, race, hair, eyes, education, body_type, height):
        self.age = age
        self.race = race
        self.hair = hair
        self.eyes = eyes
        self.education = education
        self.body_type = body_type
        self.height = height


def create_age():
    age = random.randint(18, 65)
    return age


def create_ethnic():
    race_list = ['Caucasian','Caucasian','Caucasian','Caucasian','Caucasian',
                 'Caucasian', 'Black', 'Asian', 'Middle East', 'Hispanic']
    race = race_list[random.randint(0, 9)]
    return race


def create_hair(ethnic):
    hair = ['Blonde', 'Red', 'Black', 'Brown']
    if ethnic != 'Caucasian':
        color = hair[random.randint(2, 3)]
        return color
    else:
        color = hair[random.randint(0, 3)]
        return color


def create_eyes(ethnic):
    eyes = ['Blue', 'Green', 'Grey', 'Hazel', 'Brown']
    if ethnic != 'Caucasian':
        eye_color = eyes[random.randint(3, 4)]
        return eye_color
    else:
        eye_color = eyes[random.randint(0,4)]
        return eye_color


def create_education():
    education_list = ['High School',
                      'High School',
                      'High School',
                      'High School',
                      'College',
                      'College',
                      'College',
                      'Bachelor',
                      'Bachelor',
                      'Masters',
                      'PhD']

    education = education_list[random.randint(0,9)]
    return education


def create_body_type():
    body_type_list = ['thin', 'athletic', 'athletic', 'average', 'average',
                      'average', 'average', 'few extra pounds', 'few extra pounds']

    body_type = body_type_list[random.randint(0, 8)]
    return body_type

def create_height():
    height_list = [5.0, 5.2, 5.2,5.2, 5.2, 5.3, 5.3, 5.3, 5.3,5.3, 5.3, 5.3, 5.3, 5.4, 5.4, 5.4, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11]
    height = height_list[random.randint(0, len(height_list)-1)]
    return height

# list to store people
female_list = list()

for x in range(0, 10):
    age = create_age()
    ethnic = create_ethnic()
    eyes = create_eyes(ethnic)
    hair = create_hair(ethnic)
    education = create_education()
    body_type = create_body_type()
    height = create_height()
    person = Female(age, ethnic, hair, eyes, education, body_type, height)

    female_list.append(person)


# truncate_user_choice_table()

for person in female_list:
    print("AGE  |   Race    |   Body Type   |   Hair    |   Eyes    |"
          " Education   |   Height  |")
    print("%3d  %10s    %10s    %8s    %8s    %10s    %5s"
          % (person.age, person.race, person.body_type, person.hair, person.eyes,
             person.education, person.height))

    print('\n')
    label = input("Do you like this profile: ")
    if label == '1':
        result = insert(1, person)
        print(result)
    else:
        result = insert(0, person)
        print(result)


