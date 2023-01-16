thisdict = {
    'eesnimi': 'Kevin',
    'perenimi': 'Kangur',
    'sünniaasta': '2005',
    'elukoht': 'Laoküla',
    'lemmik magustoit': 'riisi puder kisseliga'
}

print(thisdict.get('elukoht'))
print(thisdict['elukoht'])

thisdict['lemmik magustoit'] = 'tarretis'

for k, v in thisdict.items():
    print(k, v)