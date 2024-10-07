from pyMaze import maze,COLOR,agent,textLabel
m=maze()
# m=maze(15,20)
# m.CreateMaze(saveMaze=True)
# m.CreateMaze(loadMaze='maze--2024-10-07--22-13-04.csv', theme=COLOR.light)
m.CreateMaze(loopPercent=100)

a=agent(m, footprints=True,filled=True)
b=agent(m,5,5, footprints=True,color='red')
c=agent(m,4,1, footprints=True,color='red',shape='arrow')

m.enableArrowKey(a)
# m.enableWASD(b)

# path2=[(5,4),(5,3),(4,3),(3,3),(3,4),(4,4)]
# path3='WWWNES'

# l1=textLabel(m,'Total Cells',m.rows*m.cols)

# m.markCells=[(5,5),(6,5),(4,5),(2,1)]
# a=agent(m,5,4, filled=True,shape='arrow')
# a=agent(m,5,4, footprints=True,shape='arrow',color='red')
# a.position=(5,5)
# a.position=(5,6)
# a.position=(5,7)
# print(a.x)
# print(a.y)
# print(a.position)

# print(m.maze_map)  # prints the keys
# print(m.path)

#m.tracePath({a:m.path,b:path2,c:path3},delay=200)
# m.tracePath({a:m.path},delay=200,kill=True)
# m.tracePath({b:path2},delay=300)
# m.tracePath({c:path3},delay=300)
# m.tracePath({a:m.path},delay=100,showMarked=True)
# m.tracePath({a:m.path},delay=100,kill=True,showMarked=True)

m.run()
