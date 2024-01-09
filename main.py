import json

file = open("friends_json.txt", "r")
file_content = json.load(file)  # file_content is a dict now
file.close()

print(file_content["friends"])

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

file_dump = open("dict_json.txt", "w")
json.dump(data, file_dump, indent=2)
file_dump.close()





