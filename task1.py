class animals:
    def __init__(self,name,age,weight,habitat,diet):
        if isinstance(name,str):
            self.name = name
        else:
            raise ValueError('Must be string')
        if isinstance(age,int):
            self.age = age
        else:
            raise ValueError('Must be integer')
        if isinstance(weight,float):
            self.weight = weight
        else:
            raise ValueError('Must be float')
        if isinstance(habitat,str):
            self.habitat = habitat
        else:
            raise ValueError('Must be string')
        if isinstance(diet,str):
            self.diet = diet
        else:
            raise ValueError('Must be string')
    
    def eat(self,eat):
        return f'animal eats {eat}'
    def sleep(self,sleep):
        return f'animal sleeps {sleep}'
    def make_sound(self,sound):
        return f'animal makes {sound}'
    def move(self,move):
        return f'animal moves {move}'
    
    def __str__(self):
        return (f'name = {self.name}\n'
                f'age = {self.age}\n'
                f'weight = {self.weight} kg\n'
                f'habitat = {self.habitat}\n'
                f'diet = {self.diet}\n')
    


class reptiles(animals):
    def __init__(self,name,age,weight,habitat,diet,color,speed):
        super().__init__(name,age,weight,habitat,diet)
        if isinstance(color,str):
            self.color = color
        else:
            raise ValueError('Must be string')
        if isinstance(speed,int):
            self.speed = speed
        else:
            raise ValueError('Must be integer')
    def crawl(self,crawl):
        return f'{self.name} crawlling {crawl}'
    def shed_skin(self,shed_skin):
        return f'{self.name} shed skin {shed_skin}'
    def bask_in_sun(self,bask_in_sun):
        return f'{self.name} basking in the sun {bask_in_sun}'
    def lay_eggs(self,lay_eggs):
        return f'{self.name} laying eggs {lay_eggs}'
    
    def __str__(self):
        return super ().__str__() + f'\n color = {self.color}\n speed = {self.speed} km/h'
    



    
class mammals(animals):
    def __init__(self,name,age,weight,habitat,diet,strengh,child):
        super().__init__(name,age,weight,habitat,diet)
        if isinstance(strengh,float):
            self.streingh = strengh
        else:
            raise ValueError('Must be float')
        if isinstance(child,bool):
            self.child = child
        else:
            raise ValueError('Must be bool')
        
    def run(self,run):
        return f'{self.name} running {run}'
    def hunt(self,hunt):
        return f'{self.name} hunting {hunt}'
    def nurture_young(self,nurture_youngn):
        return f'{self.name} grow up generation{nurture_youngn}'
    def communicate(self,communicate):
        return f'{self.name} communicate with others {communicate}'
    
    def __str__(self):
        return super ().__str__() + f'\n streingh = {self.streingh}lb\n child = {self.child}'

class zooshow:
    def __init__(self,show_name,ticket,performer):
        if isinstance(show_name,str):
            self.show_name = show_name
        else:
            raise ValueError('Must be string')
        if isinstance(ticket,int):
            self.ticket = ticket
        else:
            raise ValueError('Must be integer')
        if isinstance(performer,str):
            self.performer = performer
        else:
            raise ValueError('Must be string')
    
    def perform(self,perform):
        return f'Animal is performing{perform}'
    def info(self,info):
        return f'About animal and show - {info}'
    def sell_ticket(self,sell_ticket):
        return f'Sold tickets - {sell_ticket}'
    def calculate(self,calculate):
        return f'Money from show - {calculate}'

    def __str__(self):
        return f"Show Name: {self.show_name}, Ticket Price: {self.ticket}, Animal Performer: {self.performer}"




mammals_1 = mammals('lion',5,50.5,'desert','Carnivorous',100.10,True)
mammals_2 = mammals('elephant',10,200.50,'desert','Omnivorous',300.5,False)
mammals_3 = mammals('kenguroo', 11,80.6,'desert','Herbivorous',100.0,True)

    
reptiles_1 = reptiles('snake',4,4.6,'ground','carnivorous','green',15)
reptiles_2 = reptiles('lizer',3,1.0,'ground','predatour','red',40)
reptiles_3 = reptiles('turtle',100,10.5,'water','omnivorous','dark green',5)


show = zooshow('ZooShow',50,'lion')
show_2 = zooshow('ZooShow',50,'elephant')
show_3 = zooshow('ZooShow',50,'kenguroo')
print(f'------------\n'
      f'{reptiles_1}\n'
      f'------------\n'
      f'{reptiles_2}\n'
      f'------------\n'
      f'{reptiles_3}\n')
print(reptiles_1.crawl(''))
print(reptiles_2.bask_in_sun(''))
print(reptiles_3.lay_eggs(''))

print(f'-------------------------------------------------------------------\n'
      f'{mammals_1}\n'
      f'------------\n'
      f'{mammals_2}\n'
      f'------------\n'
      f'{mammals_3}\n')
print(mammals_1.hunt('animal'))
print(mammals_2.run(''))
print(mammals_3.communicate(''))

print(f'-------------------------------------------------------------------\n')
print(f'{show}\n'
      f'------------\n'
      f'{show_2}\n'
      f'------------\n'
      f'{show_3}\n')
print(show.perform(''))
print(show.info('Its a zooshow with lion, elephant and kenguroo'))
print(show.sell_ticket('100'))
print(show.calculate('500$'))

