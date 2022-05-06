PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt", mode="r") as file:
    name_list = file.readlines()
with open("Input/Letters/starting_letter.txt", mode="r") as file:
    default_message = file.read()
for name in name_list:
    stripped_name = name.strip()
    message = default_message.replace("[name]", f"{stripped_name}")
    with open(f"Output/ReadyToSend/{stripped_name}", mode="w") as file:
        file.write(message)
