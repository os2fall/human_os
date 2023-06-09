import time
from random import randint

class cardivascularSystem():
    def __init__(self):
        self.beating = False
        self.pulse = 60
        
class digestiveSystem():
    def __init__(self):
        self.daily_calories = 0
        self.daily_carbs = 0
        self.daily_fats = 0
        self.daily_protein = 0
        
class urinarySystem():
    def _init_(self):
        self.go_toilet = False
        
class reproductiveSystem():
    def __init__(self) :
        self.have_sex = False
        
class endocrineSystem():
    def __init__(self):
        self.teststerone_level = 1
        self.estrogen_level = 1
        self.cortisol_level = 1
        self.dophamine_level = 1
        self.vitamine_d = 1
        
class respirotorySystem():
    def __init__(self):
        self.breathing = False
        
class muscularSystem():
    def init(self):
        self.muscular_soreness = False
        
class humanBody():
    def __init__(self):
        self.cardivascular = cardivascularSystem()
        self.digestive = digestiveSystem()
        self.urinary = urinarySystem()
        self.reproductive = reproductiveSystem()
        self.endocrine = endocrineSystem()
        self.muscular = muscularSystem()
        self.respirotory = respirotorySystem()
        
        self.bodyfat_percentafe = 15
        self.apetite = False
        self.max_daily_calories = None 
        self.sex = None
        self.height = None
        self.weight = None
        self.age = None
        
    def sport_activity(self):
        answer = input('Виберіть чим ви хочете зайнятись сьогодні: walk/cardio/weightlifting')
        if answer == 'walk':
            self.endocrine.cortisol_level +=1
            self.endocrine.teststerone_level +=1
            self.cardivascular.pulse = randint(60,76)
            self.max_daily_calories += 100
            self.endocrine.dophamine_level += 5
            self.endocrine.vitamine_d += 1
        elif answer == 'cardio':
            self.endocrine.cortisol_level += 5
            self.endocrine.teststerone_level +=2
            self.cardivascular.pulse = randint(125, 150)
            self.apetite =True
            self.bodyfat_percentafe -=2
            self.max_daily_calories += 250
            self.muscular.muscular_soreness = True
        elif answer == 'weightlifting':
            self.endocrine.cortisol_level +=2
            self.endocrine.teststerone_level +=4
            self.cardivascular.pulse = randint(76, 125)
            self.apetite = True
            self.bodyfat_percentafe -=1
            self.max_daily_calories += 500
            self.muscular.muscular_soreness = True
            
    def eat_food(self):
            food_dict = {
                "apple": {
                    "calories": 52,
                    "carbs": 14,
                    "protein": 0.3,
                    "fats": 0.2
                },
                "banana": {
                    "calories": 96,
                    "carbs": 25,
                    "protein": 1.2,
                    "fats": 0.4
                },
                "chicken breast": {
                    "calories": 165,
                    "carbs": 0,
                    "protein": 31,
                    "fats": 3.6
                },
                "rice": {
                    "calories": 130,
                    "carbs": 28,
                    "protein": 2.7,
                    "fats": 0.3
                },
                "burger": {
                    "calories": 250,
                    "carbs": 30,
                    "protein": 15,
                    "fats": 12
                },
                "french fries": {
                    "calories": 365,
                    "carbs": 63,
                    "protein": 3.4,
                    "fats": 14
                },
                "pizza": {
                    "calories": 285,
                    "carbs": 36,
                    "protein": 12,
                    "fats": 10
                },
                "salmon": {
                    "calories": 206,
                    "carbs": 0,
                    "protein": 22,
                    "fats": 13
                },
                "broccoli": {
                    "calories": 55,
                    "carbs": 11,
                    "protein": 3.7,
                    "fats": 0.6
                },
                "pasta": {
                    "calories": 158,
                    "carbs": 31,
                    "protein": 5.8,
                    "fats": 0.6
                },
                "yogurt": {
                    "calories": 150,
                    "carbs": 17,
                    "protein": 5,
                    "fats": 8
                },
                "ice cream": {
                    "calories": 207,
                    "carbs": 24,
                    "protein": 4,
                    "fats": 11
                },
                "steak": {
                    "calories": 250,
                    "carbs": 0,
                    "protein": 26,
                    "fats": 17
                },
                "spinach": {
                    "calories": 23,
                    "carbs": 3.6,
                    "protein": 2.9,
                    "fats": 0.4
                },
                "orange": {
                    "calories": 62,
                    "carbs": 15,
                    "protein": 1.2,
                    "fats": 0.2
                },
                "cheese": {
                    "calories": 113,
                    "carbs": 1.4,
                    "protein": 7,
                    "fats": 9
                },
                "hamburger": {
                    "calories": 250,
                    "carbs": 32,
                    "protein": 12,
                    "fats": 9
                },
                "fried chicken": {
                    "calories": 280,
                    "carbs": 12,
                    "protein": 17,
                    "fats": 18
                },
                "mashed potatoes": {
                    "calories": 237,
                    "carbs": 35,
                    "protein": 3.4,
                    "fats": 9.8
                },
                "chocolate cake": {
                    "calories": 352,
                    "carbs": 50,
                    "protein": 4.4,
                    "fats": 16
                },
                "avocado": {
                    "calories": 160,
                    "carbs": 9,
                    "protein": 2,
                    "fats": 15
                }
            }
            print("What would you like to eat?")
            food_options = list(food_dict.keys())
            for i, food in enumerate(food_options):
                print(f"{i+1}. {food}")

            choice = int(input("Enter the number corresponding to your choice: "))
            selected_food = food_options[choice - 1]

            if selected_food in food_dict:
                food_info = food_dict[selected_food]
                self.digestive.daily_calories += food_info['calories']
                self.digestive.daily_protein += food_info["protein"]
                self.digestive.daily_carbs += food_info["carbs"]
                self.digestive.daily_fats += food_info["fats"]
                print("Enjoy your meal!")
            else:
                print("Invalid choice. Please try again.")
                self.eat_food()

    def update_sex(self):
        self.sex = input('Вкажіть вашу стать - Чоловік/Жінка:')
        
    def update_height(self):
        self.height = abs(float(input('Введіть ваш зріст у см: ')))
    
    def update_weight(self):
        self.weight = abs(float(input('Введіть вашу вагу у кг: ')))
    
    def update_age(self):
        self.age = abs(int(input('Введіть ваш вік: ')))
        
    def calc_max_calories(self):
        if self.sex == 'Чоловік':
            self.max_daily_calories = 10*self.weight + 6.25*self.height - 5*self.age + 5
        elif self.sex == 'Жінка':
            self.max_daily_calories = 10*self.weight + 6.25*self.height - 5*self.age - 161
        else: 
            print('Ви ввели неправильну стать. спробуйте ще раз')
            
    def initialise_human(self):
        print('Давайте ініціалізуємо людину')
        self.update_sex()
        self.update_height()
        self.update_weight()
        self.update_age()
        self.calc_max_calories()
        self.cardivascular.beating = True
        self.respirotory.breathing = True
        print(f'Вітаю. ваша стать: {self.sex}, ваш зріст{self.height} см, ваша вага {self.weight} кг і ваш вік {self.age} років ')
        
    def choose_hobby(self):
        hobby_dict = {
            "running": {
                "dopamine_increase": 7,
                "calories_burned": 500
            },
            "painting": {
                "dopamine_increase": 5,
                "calories_burned": 150
            },
            "reading": {
                "dopamine_increase": 3,
                "calories_burned": 50
            },
            "gardening": {
                "dopamine_increase": 4,
                "calories_burned": 200
            },
            "cooking": {
                "dopamine_increase": 6,
                "calories_burned": 300
            },
            "dancing": {
                "dopamine_increase": 8,
                "calories_burned": 400
            },
            "photography": {
                "dopamine_increase": 4,
                "calories_burned": 100
            },
            "playing an instrument": {
                "dopamine_increase": 6,
                "calories_burned": 100
            },
            "hiking": {
                "dopamine_increase": 7,
                "calories_burned": 400
            },
            "knitting": {
                "dopamine_increase": 3,
                "calories_burned": 50
            },
            "yoga": {
                "dopamine_increase": 5,
                "calories_burned": 200
            }
        }
        print("What hobby would you like to do?")
        hobby_options = list(hobby_dict.keys())
        for i, hobby in enumerate(hobby_options):
            print(f"{i+1}. {hobby}")
        choice = int(input("Enter the number corresponding to your choice: "))
        selected_hobby = hobby_options[choice - 1]
        if selected_hobby in hobby_dict:
            hobby_info = hobby_dict[selected_hobby]
            self.endocrine += hobby_info["dopamine_increase"]
            self.digestive.daily_calories += hobby_info["calories_burned"]
            print("Enjoy your hobby!")
        else:
            print("Invalid choice. Please try again.")
        