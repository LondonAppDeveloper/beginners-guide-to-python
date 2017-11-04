
apples = 10

while apples > 0:
    print('We have apples.')
    apples = apples - 1

print('We have no more apples.')

apples = 10
more_apples = True

while more_apples:
    print('We have apples.')
    apples -= 3
    if apples <= 0:
        more_apples = False

print('We have no more apples.')
