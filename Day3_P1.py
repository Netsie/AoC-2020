# Advent of Code: Day 3 Puzzle 1 

f = open("D3_Input.txt", "r")

# Content of Day3_Input.txt is written to (the) map[]:
map = []
n = 0
while True:
  line = f.readline()
  n = n + 1
  if not line:
    n = n - 1
    break;
  map.append(line.strip())
last_line = n

trees = 0
line_index = 0
row_index = 0
last_row = len(map[0])

while not line_index == (last_line-1):
  row_index += 3
  line_index += 1  
  if row_index <= (last_row - 1):
    if map[line_index][row_index] == '#':
      trees += 1
  elif row_index > (last_row - 1):
    row_index = row_index - last_row
    if map[line_index][row_index] == '#':
      trees += 1
  
print(trees)
