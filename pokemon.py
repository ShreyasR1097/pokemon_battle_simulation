import random

class Pokemon():
	
	def __init__(self, name, hp, type):
		self.hp=hp;
		self.type=type
		self.name=name
		
	def getHp(self):
		return self.hp
	
	def getType(self):
		return self.type
		
	def changeHp(self,value):
		self.hp=value
	
	def getName(self):
		return self.name
		
class FirePokemon(Pokemon):
	
	def __init__(self,name,hp):
		Pokemon.__init__(self,name,hp,"fire")
		
	def flamethrower(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-40)
		
	def ember(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-10)
		
	def blastburn(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-50)
		
	def firefang(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-30)
		
class WaterPokemon(Pokemon):
	
	def __init__(self,name,hp):
		Pokemon.__init__(self,name,hp,"water")
		
	def surf(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-40)
		
	def bubble(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-10)
		
	def hydrocannon(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-50)
		
	def waterfall(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-30)
		
class GrassPokemon(Pokemon):
	
	def __init__(self,name,hp):
		Pokemon.__init__(self,name,hp,"grass")
		
	def gigadrain(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-40)
		
	def vinewhip(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-10)
		
	def frenzyplant(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-50)
		
	def razorleaf(self,Pokemon):
		Pokemon.changeHp(Pokemon.getHp()-30)
		
		
pokemonList= []
pokemonList.append(FirePokemon("Charizard",200))
pokemonList.append(WaterPokemon("Lapras",200))
pokemonList.append(GrassPokemon("Tropius",200))
pokemonList.append(FirePokemon("Ninetails",200))	
pokemonList.append(WaterPokemon("Empoleon",200))
pokemonList.append(GrassPokemon("Leafeon",200))
		
x=random.randint(0,2)
y=random.randint(3,5)		
moveNo=random.randint(1,4)

a=x
b=y

#charizard= FirePokemon("charizard",200)
#ninetails= FirePokemon("ninetails",200)
pokeno1=3
pokeno2=3

print "Trainer1 has ", pokeno1," pokemon and has sent out " , pokemonList[x].getName(),"with HP: ",pokemonList[x].getHp()
print "Trainer2 has ",pokeno2," pokemon and has sent out " ,pokemonList[y].getName(),"with HP ",pokemonList[y].getHp(),"\n"

while(pokeno1>0 and pokeno2>0):

	while (pokemonList[y].getHp()>0 and pokemonList[0].getHp()>0 ):
	
		
		
		moveNo=random.randint(1,4)
		if(x==0):
			if(moveNo==1):
				pokemonList[x].flamethrower(pokemonList[y])
				print pokemonList[x].getName(), "used flamethrower~"
		
			elif(moveNo==2):
				pokemonList[x].ember(pokemonList[y])
				print pokemonList[x].getName(), "used ember~"
			
			elif(moveNo==3):
				pokemonList[x].blastburn(pokemonList[y])
				print pokemonList[x].getName(), "used blastburn~"
			
			elif(moveNo==4):
				pokemonList[x].firefang(pokemonList[y])
				print pokemonList[x].getName(), "used firefang~"
			
		if(x==1):
			if(moveNo==1):
				pokemonList[x].surf(pokemonList[y])
				print pokemonList[x].getName(), "used surf~"
		
			elif(moveNo==2):
				pokemonList[x].bubble(pokemonList[y])
				print pokemonList[x].getName(), "used bubble~"
			
			elif(moveNo==3):
				pokemonList[x].hydrocannon(pokemonList[y])
				print pokemonList[x].getName(), "used hydrocannon~"
			
			elif(moveNo==4):
				pokemonList[x].waterfall(pokemonList[y])
				print pokemonList[x].getName(), "used waterfall~"
			
		if(x==2):
			if(moveNo==1):
				pokemonList[x].gigadrain(pokemonList[y])
				print pokemonList[x].getName(), "used gigadrain~"
			
			elif(moveNo==2):
				pokemonList[x].vinewhip(pokemonList[y])
				print pokemonList[x].getName(), "used vinewhip~"
			
			elif(moveNo==3):
				pokemonList[x].frenzyplant(pokemonList[y])
				print pokemonList[x].getName(), "used frenzyplant~"
			
			elif(moveNo==4):
				pokemonList[x].razorleaf(pokemonList[y])
				print pokemonList[x].getName(), "used razorleaf~"	
	
		
		if(pokemonList[y].getHp()<=0):
			pokemonList[y].changeHp(0)
		print "HP of " ,pokemonList[y].getName()," has fallen to:", pokemonList[y].getHp()
		if(pokemonList[y].getHp()<=0):
			print "Trainer2's pokemon ", pokemonList[y].getName(), " has fainted!"
			pokeno2=pokeno2-1
			print "Trainer2 has ", pokeno2, " pokemon left."
			if(pokeno2==0):
				print "\nAll of Trainer2's pokemon have fainted! Trainer1 wins the battle!!\n"
				break
			else:
				if(pokeno2==1):
					y=12-y-b
				
				else:
					y=random.randint(3,5)
					while(y==b):
						y=random.randint(3,5)
				print "Trainer2 has sent out " , pokemonList[y].getName(),"with HP: ",pokemonList[y].getHp(),"\n"
				break
	
	
		
		
		
		moveNo=random.randint(1,4)
		if(y==3):
			if(moveNo==1):
				pokemonList[y].flamethrower(pokemonList[x])
				print pokemonList[y].getName(), "used flamethrower~"
		
			elif(moveNo==2):
				pokemonList[y].ember(pokemonList[x])
				print pokemonList[y].getName(), "used ember~"
			
			elif(moveNo==3):
				pokemonList[y].blastburn(pokemonList[x])
				print pokemonList[y].getName(), "used blastburn~"
			
			elif(moveNo==4):
				pokemonList[y].firefang(pokemonList[x])
				print pokemonList[y].getName(), "used firefang~"
			
		if(y==4):
			if(moveNo==1):
				pokemonList[y].surf(pokemonList[x])
				print pokemonList[y].getName(), "used surf~"
		
			elif(moveNo==2):
				pokemonList[y].bubble(pokemonList[x])
				print pokemonList[y].getName(), "used bubble~"
			
			elif(moveNo==3):
				pokemonList[y].hydrocannon(pokemonList[x])
				print pokemonList[y].getName(), "used hydrocannon~"
		
			elif(moveNo==4):
				pokemonList[y].waterfall(pokemonList[x])
				print pokemonList[y].getName(), "used waterfall~"
			
		if(y==5):
			if(moveNo==1):
				pokemonList[y].gigadrain(pokemonList[x])
				print pokemonList[y].getName(), "used gigadrain~"
		
			elif(moveNo==2):
				pokemonList[y].vinewhip(pokemonList[x])
				print pokemonList[y].getName(), "used vinewhip~"
			
			elif(moveNo==3):
				pokemonList[y].frenzyplant(pokemonList[x])
				print pokemonList[y].getName(), "used frenzyplant~"
			
			elif(moveNo==4):
				pokemonList[y].razorleaf(pokemonList[x])
				print pokemonList[y].getName(), "used razorleaf~"	
	
		if(pokemonList[x].getHp()<=0):
			pokemonList[x].changeHp(0)
		print "HP of " ,pokemonList[x].getName()," has fallen to:", pokemonList[x].getHp()
		if(pokemonList[x].getHp()<=0):
			print "\n Trainer1's pokemon ", pokemonList[x].getName(), " has fainted!"
			pokeno1=pokeno1-1
			print "Trainer1 has ", pokeno1, " pokemon left."
			if(pokeno1==0):
				print "\nAll of Trainer1's pokemon have fainted! Trainer2 wins the battle!!\n"
				break
			else:
			
				if(pokeno1==1):
					x=3-x-a
				else:
					x=random.randint(0,2)
					while(x==a):
						x=random.randint(0,2)
				print "Trainer1 has sent out " , pokemonList[x].getName(),"with HP: ",pokemonList[x].getHp(), "\n"
				
		
		
		

	


	
		