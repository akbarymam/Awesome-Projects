"""
#Putri mencari org agar diangkat menjadi "saudara/i" asalkan : baik rajin
tamu = input("kamu pria atau wanita? ")
baik = True
rajin = True

if baik & rajin:
	if tamu == "pria":
		print("nikah yuk")
	else:
		print("kita jadi saudari yuk")
else:
	print("Hush pergi sana!1!1")
"""


player1 = {"name":"sonGoku", "power":250}
player2 = {"name":"Vegeta", "power":350}

def train(player):
	player["power"] += 50

def attack(attacker, defender):
	if(attacker['power'] > defender['power']):
		print(defender['name'], ': NANI !1!1 kau terlalu kuat, aku tidak dapat mengalahkanmu', attacker['name'])

	elif(attacker['power'] == defender['power']):
		print(defender['name'], ': fuwaaah! ternyata kau sudah setara denganku ya', attacker['name'])

	else:
		print(defender['name'], ': terlalu lemah! pergilah untuk berlatih kembali', attacker['name'])

#attack(player`, player`)
#train(player`)
#train(player1)
train(player1)
train(player1)
attack(player1, player2)


'''

name = input("nama Monsternya siapa? ")
monster = {'nama': name, 'power': 330}

def startGame():
	choice = input('Mau apa? 1. Makan  2. Lihat Status  3. Keluar  : ')
	if choice == '1':
		goEat()
	elif choice == '2':
		goStatus()
	else:
		goExit()


def goEat():
	print('Nyam.... Nyam...Nyam....')
	monster['power'] += 100
	startGame()
def goStatus():
	print(monster)
	startGame()
def goExit():
	print('Bye... Bye...')

startGame()
'''