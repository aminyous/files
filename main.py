friends_list = []

for i in range(3):
    name = input("Enter your friend's name: ")
    friends_list.append(name)

my_file = open("people.txt", "r")
file_content = [item.strip() for item in my_file.readlines()]
my_file.close()

friends_list_set = set(friends_list)
file_content_set = set(file_content)

nearby_friends = friends_list_set.intersection(file_content_set)
nearby_friends_list = list(nearby_friends)

nearby_friends_list = [item + "\n" for item in nearby_friends_list]

my_file_writing = open("nearby_friends.txt", "w")
my_file_writing.writelines(nearby_friends_list)
my_file_writing.close()








