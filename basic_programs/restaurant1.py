food_menu = {
    1 : 'idly-vada',
    2 : 'benne-dosa',
    3 : 'poha',
    4 : 'vada-pav',
    5 : 'puri-sag'
}

print("Welcome to our hotel Basaveshwara Khanavali")
print('Menu: \n1:Idly-vada 2:Benne-Dosa 3:Pha 4:Vada-Pav 5:Puri-Sag')
food_number = int(input('Enter food number of your choice: '))

food = food_menu.get(food_number, 'invalid_choice')

if food == 'invalid_choice':
    print('Sorry Maam, you have chosen a invalid food item')
else:
    print(f'Maam, here is your tasty {food}')
