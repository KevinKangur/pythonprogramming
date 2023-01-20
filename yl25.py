about_me = {
    'first_name': 'Kevin',
    'last_name': 'Kangur',
    'date_of_birth': '2005',
    'home': 'Laoküla',
    'favorite_dessert': 'riisi puder kisseliga'
}

print(about_me.get('home'))
print(about_me['home'])

about_me['favorite_dessert'] = 'tarretis'

for k, v in about_me.items():
    print(k, v)

if 'id_code' in about_me:
    print('isikukood on olemas')
else:
    print('isikukood puudub')

print(len(about_me))

about_me['height'] = '180 cm'
print(about_me)

#print(mina.pop('date_of_birth'))
del about_me['date_of_birth']
print(about_me)

about_me.clear()
print(about_me)

del about_me
print(about_me)