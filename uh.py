#games is a dictionary
games={1:'soccer',2:'basketball'}
print(games)
print(games[1])

#append to a dictionary?
games[3]="cricket"
print(games)

games[4]="hockey"
print(games)

games[5]="golf"
print (games)

#update a dictionary
games2={0:"football"}
games.update( games2 )
print(games)

#remove the element from dictionary
games.pop(4)
print(games)

#remove all the elements from dictionary
games.clear()
print(games)