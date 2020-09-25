#OPening IDLE
print ("testing")

#Math Python
1 + 1

20 + 80

6 - 5

5 * 2

5 ** 2

print ('1 + 1 is a additio in math')

print ('one kilobyte is 2^10 bytes', 2**10,'bytes')

#Division, note that in python ignores remainders/decimals.
21/3

23.0/3.0

#Remainders %
10 % 2

#Order of Operations
(1+ 2) * 3

#Comments Please
#Estrutura de repeticao
a = [1,2,3,4,5,6,5,4,3,2,1]
b = ['' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
print(line)

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

for item in range (10):
    print(item)

#Variables, Scripts

#Simple Program
print('Mary had a little lamb,')
print('this lamb grew up with time')
print('end story')

#Variabels
v = 1 #int
print('the value of v is now', v)

#Strings
word1 = 'Good'
word2 = 'morning'
print(word1, word2)

#Loops, Condionals

#The while loop
a = 0
while a < 10:
a = a + 1
print(a)

#Functions

def x(name1, name2):
    x(name1 = 'zhang', name2 = 'yuan')
    print ('zhang ', name1)
    print ('yuan', name2)
    return;

def hello(meu_nome,idade):
    print('Ola', meu_nome ,idade)