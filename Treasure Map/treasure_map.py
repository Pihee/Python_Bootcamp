line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter = position[0].lower()
abc = ["a", "b", "c"]
column = abc.index(letter)
line = int(position[1])-1
map[line][column] = "X"
'''
if int(position[1]) == 1 :
  if position[0] == "A" :
    line1[0] = "X"
  elif position[0] == "B" :
    line1[1] = "X"
  else :
    line1[2] = "X"
elif int(position[1]) == 2 :
  if position[0] == "A" :
    line2[0] = "X"
  elif position[0] == "B" :
    line2[1] = "X"
  else :
    line2[2] = "X"
else :
  if position[0] == "A" :
    line3[0] = "X"
  elif position[0] == "B" :
    line3[1] = "X"
  else :
    line3[2] = "X"
'''
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")