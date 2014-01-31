L = [123, 'hjk', 'dif']
L.append('NI') #Growing: add object at the end of list
print L
L.pop(2) #deleate an item in the middle
print L
del L[2] #deletes an item from a lit too
print (L)
M = ['bb','cc', 'vv']
M.sort()
print M
M.reverse()
print(M)
F = [[1, 2, 3], [4, 5, 6], [7, 8,9]] # A3 x 3 matrix, as nested lists
print F[1] # get row 2
print F[1][2] #get row 2 then get item 3 within the row

col1 = [row[1] + 1 for row in F] # list comprehension expression
print col1
col2 = [row[1] for row in F if row[1] % 2 == 0]
print col2
diag = [F[i][i] for i in [0, 1, 2]]
print diag
doubles = [c * 2 for c in 'hej']
print doubles