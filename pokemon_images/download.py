import os
import csv
import string

with open("../pokemon.csv", 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		break

	for row in reader:
		name = row[30]
		os.system("wget https://img.pokemondb.net/sprites/black-white/anim/normal/%s.gif"%(name.lower()))
