##############
# Computer Project pet game
# Algorithm
#     defintion some functions, and each of them operate a program
#     create a pet class which contains all of the importanat data and functions
#     create two species of animals, recall the functions from the pet class
#     print the the data in a format form
#     use the main function to recall each function and confirm whether 
#the conditions valid.
#################
from random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
        '''a skeleton of the Pet class with all attributes in the __init__ methodg'''
        # modify the following code
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items= []
        
        
        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy =randint(5,10)

        self._reply_to_master('newborn')

    def _time_pass_by(self, t=1):
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
        '''class methods: simply return the value of self._hunger'''
        return self._hunger

    def get_thirst_level(self):
        '''class methods: simply return the value of self._thirst'''
        return self._thirst

    def get_energy_level(self):
        '''class methods: simply return the value of self._energy'''
        return self._energy
    
    def drink(self, liquid):
        '''class methods: simply return the value of self._drink
         this method represents the action of ‘feeding water’.
         this method takes an input parameter called liquid, which is an instance that
belongs to a certain class type. '''
        if isinstance(liquid, tuple(self._drinkable_items)):
            #Call the _time_pass_by method with the default time
            self._time_pass_by(1)
            liquid= float(liquid.get_quantity())
            #If the liquid is valid, you will decrease the thirsty value of your pet, based on the
#quantity of this liquid.
            if liquid <= self._thirst:
                self._thirst = self._thirst -  liquid
#                if self._thirst <2:
#                    print("Your pet is satisfied, no desire for sustenance now.")
            elif self._thirst ==0:
                print("Too much drink to finish. I will leave some for you")
            else:  
                self._thirst = 0
        else:
            print ("Not drinkable")     
        # replace with your code
        
        self._update_status()
        #call the _reply_to_master()
#method (which is also complete, but you need to figure out the input argument to
#this method). 
        self._reply_to_master(event='drink' )
        
    def feed(self, food):
        
        '''the logic of this method is very similar to drink. The
difference is that in this method, you will update the value of _hunger. \
You will also
call the _reply_to_master() method with a different input argument than used
with drink.'''
        if isinstance(food, tuple(self._edible_items)):
             #get value of the food
             self._time_pass_by(t=1)
             food= float(food.get_quantity())
             #whether the food is valid
             if food >=0:
                 if self._hunger >= 2:
                     if self._hunger - food > 0:
                         self._hunger -= food
                     else:
                         self._hunger = 0
                     self._reply_to_master(event='feed')
                 else:
                     print("Your pet is satisfied, no desire for sustenance now.")
        #if the string is invalid print the error message
        else:
            print("Not edible")
        self._update_status()
#                     

    def shower(self):
        '''call the _time_pass_by() method. The shower takes a time=4. this \
        method changes two attributes of your pet: the _smell and the
_loneliness . The smell level will always drop to zero. The loneliness level
of your pet will be decreased depending on how long the shower takes'''
        #fet value of the smell
        self._time_pass_by(t=4)
        self._smell =0
        #judge the value and calculate 
        if  self._loneliness >= 4:
            self._loneliness = self._loneliness - 4
        else:
            self._loneliness = 0
        #update the value
        self._reply_to_master(event='shower')   
        self._update_status()

    def sleep(self):
        '''Similar to the shower method, but sleeping takes a time=7, \
        and the attribute
modified by this method is self._energy which will increase. '''
        self._time_pass_by(t=7)
        #get the max or the min of the value
        self._energy = min(MAX, self._energy + 7)
        self._reply_to_master(event='sleep')   
        self._update_status()

    def play_with(self):
        '''Similar to the shower method, but play_with takes a time=4, and this
method changes three attributes of your pet: self._loneliness,
self._smell, and self._energy. The loneliness and energy level will
decrease, and the smell level will increase, depending the time you have spent
playing with your pet. '''
        self._time_pass_by(t=4)
        smell_value = self._smell + 4
        lone_value = self._loneliness - 4
        energy_value = self._energy - 4
#        if smell_value in range(0,11):
#            value_smell = smell_value
        smell_value = min(MAX, smell_value)
#        if lone_value in range(0,11):
#            value_lone = lone_value 
        lone_value = max(MIN, lone_value)
#        if energy_value in range(0,11): 
#            value_energy = energy_value
        energy_value = max(MIN, energy_value)
        
        self._energy = energy_value
        self._smell = smell_value
        self._loneliness= lone_value
        self._reply_to_master(event='play')   
        self._update_status()

    def _reply_to_master(self, event='newborn'):
	# insert docstring
        # this function is complete #
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
        '''this method will display the hunger, thirst, smell, loneliness, and energy
attributes of your pet as a table. Attribute values will be sorted in alphabetical
order. '''
        # partially formatted string for your guidance
        #s = "{:<12s}: [{:<20s}]".format() + "{:5.2f}/{:2d}".format()
        print("{:<12s}: [{:<20s}]".format("Energy",round(self._energy)*2*"#") + "{:5.2f}/{:2d}".format(self._energy,10))
        print("{:<12s}: [{:<20s}]".format("Hunger",round(self._hunger)*2*"#") + "{:5.2f}/{:2d}".format(self._hunger,10))
        print("{:<12s}: [{:<20s}]".format("Loneliness",round(self._loneliness)*2*"#") + "{:5.2f}/{:2d}".format(self._loneliness,10))
        print("{:<12s}: [{:<20s}]".format("Smell",round(self._smell)*2*"#") + "{:5.2f}/{:2d}".format(self._smell,10))
        print("{:<12s}: [{:<20s}]".format("Thirst",round(self._thirst)*2*"#") + "{:5.2f}/{:2d}".format(self._thirst,10))
       
    def _update_status(self):
	# insert docstring
        # this function is complete #
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):
    '''this class inherits the Pet class. The init method of this class will inherit
most of the features from the Pet class (by calling Pet’s __init__ method which is
also a good place to set the species to 'cat'). Besides that, the cat class will update two
attributes (all within __init__):'''
    def __init__(self, name='fluffy',gender='male', color='white',species='cat'):
        Pet.__init__(self,name,species, gender, color )
        #it will be a list that contains elements from the
#'cat_edible_items' list (which is at the beginning of the template code.)
        self._edible_items= cat_edible_items
        #it will be a list that contains elements from the
#'cat_drinkable_items'.
        self._drinkable_items= cat_drinkable_items
class Dog(Pet):
    '''this class inherits the Pet class. The init method of this class will inherit
most of the features from the Pet class (by calling Pet’s __init__ method which is
also a good place to set the species to 'cat'). Besides that, the cat class will update two
attributes (all within __init__):'''
    def __init__(self, name='fluffy',gender='male', color='white',species='dog'):
        Pet.__init__(self,name,species, gender, color )
         #it will be a list that contains elements from the
#'cat_edible_items' list (which is at the beginning of the template code.)
        self._edible_items = dog_edible_items
        #it will be a list that contains elements from the
#'cat_drinkable_items'.
        self._drinkable_items=dog_drinkable_items
	# insert docstring
    	# your code goes here #
        
def main():
    print("Welcome to this virtual pet game!")
    prompt = input("Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
    # error checking for user input
    while True:
        prompt_list= prompt.split()
        if prompt == "":
            prompt_list = ['dog', 'fluffy', 'male','white']
            break
        elif prompt_list[0] == "dog" or prompt_list[0] == "cat":
            if prompt_list[2] == "male" or prompt_list[2] == "female":
                prompt_list= prompt_list
                break
       
        else:
            prompt = input("Please input the species (dog or cat), name, gender (male / female), fur color of your pet,seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): ")
            continue
    #if the species id the dog
    if prompt_list[0] == "dog":
        pet_dog = Dog(prompt_list[1],prompt_list[2],prompt_list[3],prompt_list[0])
        intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
        print(intro)
        #check the input command whether is vaild
        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
        list_command = ["feed","drink","shower", "sleep", "play","status"]
        while prompt != "q":
            if prompt in list_command:
                #check the input command whether is status
                if prompt != "status":    
                    if prompt == "feed":
                        #judge the input whether is valid
                        while True:
                            num_food = input("How much food ? 1 - 10 scale: ")
                            if num_food.isdigit():
                                num_food = int(num_food)
                                if num_food in range(0,11):
                                    if pet_dog.get_hunger_level()  >=2:
                                        pet_dog.feed(DogFood(num_food))
                                        break
                                    else:
                                        
                                        print("Your pet is satisfied, no desire for sustenance now.")
                                        break
                                else:
                                    print("Invalid input")
                            else:
                               print("Invaild input") 
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "drink":
                        #judge the input whether is valid
                        while True:
                            num_food = input("How much drink ? 1 - 10 scale: ")
                            if num_food.isdigit():
                                num_food = int(num_food)
                                if num_food in range(0,11):
                                    pet_dog.drink(Water(num_food))
                                    break
                                else:
                                    print("Invalid input")
                            else:
                                print("Invalid input")
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "shower":
                        pet_dog.shower()
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "sleep":
                        pet_dog.sleep()
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "play":
                        pet_dog.play_with()
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                        
                elif prompt == "status":
                    pet_dog.show_status()
                    prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                    continue
            else:
                print("Invalid command.")
                prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                list_command = ["feed","drink","shower", "sleep", "play","status"]
                continue
    #if the species is cat
    elif prompt_list[0] == "cat":
        cat_pet = Cat(prompt_list[1],prompt_list[2],prompt_list[3],prompt_list[0])
        intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
        print(intro)
        #check the input command whether is vaild
        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
        list_command = ["feed","drink","shower", "sleep", "play","status"]
        while prompt != "q":
            if prompt in list_command:
                #check the input command whether is status
                if prompt != "status":    
                    if prompt == "feed":
                        #judge the input whether is valid 
                        while True:
                            #check the input vaule of food whether is valid
                            num_food = input("How much food ? 1 - 10 scale: ")
                            if num_food.isdigit():
                                num_food = int(num_food)
                                if num_food in range(1,11):
##                                    if cat_pet.get_hunger_level()  >=2:
#                                        cat_pet.feed(CatFood(num_food))
#                                
#                                        break
#                                    else:
#                                        print("Your pet is satisfied, no desire for sustenance now.")
#                                        break
                                    cat_pet.feed(CatFood(num_food))
                                    break
                                else:
                                    print("Invalid input.")
                            else:
                                print("Invalid input.")
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "drink":
                        #judge the input whether is valid
                        while True:
                            num_food = input("How much drink ? 1 - 10 scale: ")
                            if num_food.isdigit():
                                num_food = int(num_food)
                                if num_food in range(1,11):
                                    cat_pet.drink(Water(num_food))
                                    break
                                else:
                                    print("Invalid input.")
                            else:
                                print("Invalid input.")
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                        
                        
                    if prompt == "shower":
                        cat_pet.shower()
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "sleep":
                        cat_pet.sleep()
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                    if prompt == "play":
                        cat_pet.play_with()
                        prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                        continue
                elif prompt == "status":
                    cat_pet.show_status()
                    prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                    continue
                
            else: 
                print("Invalid command.")
                prompt = input("\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): ")
                list_command = ["feed","drink","shower", "sleep", "play","status"]
                continue
    print("Bye ~")

if __name__ == "__main__":
    main()
