month = int(input('Enter DOB month: '))

# if else
if month == 1:
    print('Garnet')
    print('People born in January are bold and alert.')
elif month == 2:
    print('Amethyst')
    print('People born in February are lucky and loyal.')
elif month == 3:
    print('Aquamarine')
    print('People born in March are naughty and genius.')
elif month == 4:
    print('Diamond')
    print('People born in April are caring and strong.')
elif month == 5:
    print('Emrald')
    print('People born in May are loving and pratical.')
elif month == 6:
    print('Alexandrite')
    print('People born in June are romantic and curious.')
elif month == 7:
    print('Ruby')
    print('People born in July are adventurous and honest.')
elif month == 8:
    print('Peridot')
    print('People born in August are active and hardworking.')
elif month == 9:
    print('Sapphire')
    print('People born in September are sensitive and pretty.')
elif month == 10:
    print('Tourmaline')
    print('People born in October are stylish and friendly.')
elif month == 11:
    print('Citrine')
    print('People born in November are nice and creative.')
elif month == 12:
    print('Zircon')
    print('People born in December are confident and freedom loving.')
else:
    print('month not in 1 to 12')


# match case
match month:
    case 1:
        print('Garnet')
        print('People born in January are bold and alert.')
    case 2:
        print('Amethyst')
        print('People born in February are lucky and loyal.')
    case 3:
        print('Aquamarine')
        print('People born in March are naughty and genius.')
    case 4:
        print('Diamond')
        print('People born in April are caring and strong.')
    case 5:
        print('Emrald')
        print('People born in May are loving and pratical.')
    case 6:
        print('Alexandrite')
        print('People born in June are romantic and curious.')
    case 7:
        print('Ruby')
        print('People born in July are adventurous and honest.')
    case 8:
        print('Peridot')
        print('People born in August are active and hardworking.')
    case 9:
        print('Sapphire')
        print('People born in September are sensitive and pretty.')
    case 10:
        print('Tourmaline')
        print('People born in October are stylish and friendly.')
    case 11:
        print('Citrine')
        print('People born in November are nice and creative.')
    case 12:
        print('Zircon')
        print('People born in December are confident and freedom loving.')
    case _:
        print('month not in 1 to 12')