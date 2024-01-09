import json

file = open("friends_json.txt", "r")
file_content = json.load(file)  # file_content is a dict now
file.close()

print(file_content["friends"])







