row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
row, column = input(
    "Where do you want to put the treasure?\nEnter the number of the row and then followed by number of "
    "columns: ")
row = int(row) - 1
column = int(column) - 1
selected_row = map[row]
selected_row[column] ="X"
print(f"{row1}\n{row2}\n{row3}")

