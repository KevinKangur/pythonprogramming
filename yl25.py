mina = {
    'eesnimi': 'Kevin',
    'perenimi': 'Kangur',
    'sünniaasta': '2005',
    'elukoht': 'Laoküla',
    'lemmik magustoit': 'riisi puder kisseliga'
}

print(mina.get('elukoht'))
print(mina['elukoht'])

mina['lemmik magustoit'] = 'tarretis'

for k, v in mina.items():
    print(k, v)

if 'isikukood' in mina:
    print('isikukood on olemas')
else:
    print('isikukood puudub')

print(len(mina))

mina['pikkus'] = '180 cm'
print(mina)

#print(mina.pop('sünniaasta'))
del mina['sünniaasta']
print(mina)

mina.clear()
print(mina)

del mina
print(mina)