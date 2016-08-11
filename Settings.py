#########################
class enemy():
	def __init__(self, map, hp):
		self.level = enemy_ability_list[map][5]
		self.name = enemy_ability_list[map][3]
		self.hp = hp
		self.ATK = enemy_ability_list[map][1]
		self.speed = enemy_ability_list[map][2]
		self.max_hp = enemy_ability_list[map][0]
		self.gold = enemy_ability_list[map][6]
		self.exp = enemy_ability_list[map][7]
		self.map = map

	def enemy_attack(self, player):



class player():
	def __init__(self, level, hp, mp, RI, BI, exp, gold):
		self.level = level
		self.hp = hp
		self.mp = mp
		self.DEF = player_ability[level][4]
		self.ATK = player_ability[level][2]
		self.SPD = player_ability[level][3]
		self.RI = item["heal potion"] = RI
		self.BI = item["ether potion"] = BI
		self.exp = exp
		self.gold = gold

	def attack(self, enemy):


enemy_ability_list = [["hp", "atk", "speed", "name", "map", "level", "gold", "exp"], [30,10,4,"Skeleton",1,1,20,20],
					  [60,20,8,"Green Slime",2,2,30,25], [130,50,20,"Zombie",3,4,50,35], [2000,80,64,"Gargoyle",4,7,80,50],
					  [4000,90,80,"Minotaur",5,8,90,55], [12000,100,96,"Water Holege",6,9,100,60], [60,20,8,"Cyclops",7,2,30,25],
					  [100,40,12,"Winter Wolf",8,3,40,30], [130,50,20,"Hag",9,4,50,35], [320,60,32,"Float Eye",10,5,60,40],
					  [4000, 90, 80, "Treant", 11, 8, 90, 55], [60000,120,125,"Balrog",12,10,120,70],
					  [12000,100,96,"Greater Demon",13,9,100,60],
					  [1000,70,48,"Mad Taus",14,6,70,45], [100000,200,150,"Arch Demon Secpter",15,11,200,200],
					  [2000,80,64,"Mad Taus Revenge",16,7,80,50], [2000,80,64,"Mad Taus Revenge2",17,7,80,50],
					  [130, 50, 20, "Hag", 18, 4, 50, 35]]

entrance_and_exit = [['up', 'down', 'left', 'right'], [0,12,9,0], [0,14,9,9], [0,0,9,9], [0,13,9,9], [0,13,9,9], [0,13,9,0], [13,13,0,9],
					  [13,0,9,0], [12,13,0,0], [13,0,9,0], [13,0,0,10], [13,13,10,10],[13,0,10,0], [0,0,0,10],
					  [13,0,0,0], [0,0,10,10],[0,0,0,0], [0,0,0,10]]

player_ability = (("max_hp", "max_mp", "ATK", "Speed", "DEF", "?", "exp"), (100, 10, 10, 5, 5, 10, 100), (200, 20, 15, 10, 10, 20, 200),
				  (200, 40, 20, 15, 15, 30, 300),
				  (300, 40, 20, 15, 15, 30, 300), (400, 60, 25, 25, 20, 20, 40, 400),
				  (500, 80, 35, 40, 25, 50, 500), (600, 100, 50, 60, 30, 60, 600),
				  (700, 150, 70, 80, 35, 70, 700), (800, 200, 90, 100, 40, 80, 800),
				  (1200, 400, 150, 150, 50, 100, 1200))

item = {"heal potion": 0, "ether potion": 0}

##########################
def level_up(EXP, level):
	if EXP > 100:
		level=2
		baseHP=200
		baseMP=20
		baseATK=15
		baseSPD=10
		baseDEF=0.1
	if EXP > 300:
		level=3
		baseHP=300
		baseMP=40
		baseATK=20
		baseSPD=15
		baseDEF=0.15
	if EXP > 500:
		level=4
		baseHP=400
		baseMP=60
		baseATK=25
		baseSPD=25
		baseDEF=0.2
	if EXP > 750:
		level=5
		baseHP=500
		baseMP=80
		baseATK=35
		baseSPD=40
		baseDEF=0.25
	if EXP > 1000:
		level=6
		baseHP=600
		baseMP=100
		baseATK=50
		baseSPD=60
		baseDEF=0.3
	if EXP > 1300:
		level=7
		baseHP=700
		baseMP=120
		baseATK=70
		baseSPD=80
		baseDEF=0.35
	if EXP > 1600:
		level=8
		baseHP=800
		baseMP=140
		baseATK=90
		baseSPD=100
		baseDEF=0.4
	if EXP > 2000:
		level=9
		baseHP=900
		baseMP=160
		baseATK=120
		baseSPD=125
		baseDEF=0.45
	if EXP > 2500:
		level= 10
		baseHP=1200
		baseMP=200
		baseATK=150
		baseSPD=150
		baseDEF=0.5


  
#When I receive Attack:
  
