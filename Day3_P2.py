# Advent of Code 2020: Day 3 Puzzle 2

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

tree_product = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

def count_trees(right = 3, down = 1):

  line_index = 0
  row_index = 0
  trees = 0
  while not line_index == (last_line-1):
    row_index += right
    line_index += down  
    last_row = len(map[0])
    if row_index <= (last_row - 1):
      if map[line_index][row_index] == '#':
        trees += 1
    elif row_index > (last_row - 1):
      row_index = row_index - last_row
      if map[line_index][row_index] == '#':
        trees += 1
  return trees 

for index in range(0, len(slopes)):
  tree_no = count_trees(slopes[index][0], slopes[index][1])
  index = [slopes[index][0], slopes[index][1]]
  tree_product *= tree_no

print(tree_product)
