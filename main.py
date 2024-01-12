import json

file = open("csv_file.txt", "r")
file_content = [item.strip() for item in file.readlines()]
file.close()


splitted_content = [item.split(",") for item in file_content]
dict_item = []

for item in splitted_content:
    dict_item.append({
        "club": item[0],
        "country": item[2],
        "city": item[1]
    })

file_dump = open("dict_json.txt", "w")
json.dump(dict_item, file_dump, indent=2)
file_dump.close()



