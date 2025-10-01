# Create a to-do list
todo_list = ["meet friends", "read book", "buy groceries"]

# Print the initial list
print(todo_list)

# Update "meet friends" to "meet fred"
index_meet_friends = todo_list.index("meet friends")
todo_list[index_meet_friends] = "meet fred"
print(todo_list)

# Append "call mum" to the list
todo_list.append("call mum")
print(todo_list)

# Extend the list with more tasks
todo_list.extend(["clean room", "cook dinner"])
print(todo_list)
