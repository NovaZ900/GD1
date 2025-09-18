quests = []

with open("Uno\quqq.txt","r") as file:
    data = file.readlines()
    for line in data:
        quest_data = line.split(",")
        quest_dict = {
            "question": quest_data[0],
            "options": quest_data[1:5],
            "answer": int(quest_data[5])
        }
        quests.append(quest_dict)
print(quests)