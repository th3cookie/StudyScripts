# reference -> https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python
def path_finder(maze):
    new_maze = maze.splitlines()
    print(new_maze)
    print("next\n")
    solved = False
    target = new_maze[-1][-1]
    print(target)


    
    # for i in maze:
    #     for q in i:
            
    return





a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

path_finder(a) # -> True
path_finder(b) # -> False
path_finder(c) # -> True
path_finder(d) # -> False