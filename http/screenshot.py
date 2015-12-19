from ghost import Ghost
g = Ghost()
with open('rangeIP.txt') as f:
	line = f.readline().rstrip('\n')
	while line:
		print(line)
		with g.start() as session:
			page, resources = session.open(line)
			name = line.replace('://','_') + ".png"
			print('Enregistrement de '+name)
			session.capture_to(name)
		line = f.readline().rstrip('\n')

