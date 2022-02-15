
class Animal:

    def __init__(self, this_is, animal_coloration, weight, feed):
        self.this_is = this_is
        self.animal_coloration = animal_coloration
        self.weight = weight
        self.feed = feed

    def get_coloration(self):
        print(f'My coloration is {self.animal_coloration}')

    def weight_up(self, kg):
        self.weight += kg

    def weight_down(self, kg):
        self.weight -= kg

    def get_current_weight(self):
        return self.weight

    def feed_the_animal(self):
        if self.feed != []:
            print(f'Select food for {self.this_is}:')
            for i in range(len(self.feed)):
                print(f'{i+1}. {self.feed[i]}')
            choice = int(input())
            if choice in [i+1 for i in range(len(self.feed))]:
                print(f'{self.this_is} eats {self.feed[choice-1]}')
                self.weight_up(1)
                print('Current animal weight = ', self.get_current_weight())
            else:
                print('There is no such animal')

class Lion(Animal):

    def __init__(self, animal_coloration, weight, feed):
        super().__init__('Lion', animal_coloration, weight, feed)


class Fish(Animal):

    def __init__(self, animal_coloration, weight, feed):
        super().__init__('Fish', animal_coloration, weight, feed)


lion1 = Lion('biscuit', 220, ['giraffe', 'zebra', 'elephant'])
lion1.get_coloration()
print(lion1.get_current_weight())
lion1.weight_up(5)
print(lion1.get_current_weight())
lion1.weight_down(3)
print(lion1.get_current_weight())
lion1.feed_the_animal()
lion1.feed_the_animal()


fish1 = Fish('grey', 5, ['worm', 'bigger_worm', 'alga', 'other_fish'])
fish1.get_coloration()
print(fish1.get_current_weight())
fish1.weight_up(2)
print(fish1.get_current_weight())
fish1.weight_down(1)
print(fish1.get_current_weight())
fish1.feed_the_animal()
fish1.feed_the_animal()