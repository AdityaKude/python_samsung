import sys

states = []
capitals = []

for i in range(1, len(sys.argv)):
	index_of_space = sys.argv[i].find(' ')
	states.append(sys.argv[i][:index_of_space])
	capitals.append(sys.argv[i][index_of_space+1:])
	
print('\n%-15s | %-15s |'%('STATE', 'CAPITAL'))
print('-' * 34 + '|')
for i in range(len(sys.argv)-1):
	print('%-15s | %-15s |'%(states[i].capitalize(), capitals[i].capitalize()))