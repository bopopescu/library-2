from Date_Picker.dbconnect import get_user_choice_data


def getUserChoiceData():
    user_data = get_user_choice_data()
    return user_data


#do calculations

data = getUserChoiceData()
label_list = list()
for d in data:
    label = d[1]
    if label == 1:
        label_list.append(d)

for d in label_list:
    print(d)
