# Starter Code
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")


# Write your code below!
column = int(position[0])
row = int(position[1])


select_row = map[row - 1]
select_row[column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")