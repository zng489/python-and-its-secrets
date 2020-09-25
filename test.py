class human():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print ('you`re right')

zhang = human('zhang','40')

def object(name,race,age):
    if name == 'zhang' and race == 'chinese' and age == 30:
        print ('True')
    
    else:
        print ('False')
        return


number_1 = int(input('Enter your first number: '))
number_2 = input('Enter your second number: ')

operation = input(''' type in asdas:

 + for add
  - for sub ''')