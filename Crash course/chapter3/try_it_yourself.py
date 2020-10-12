party_list = ['Elmira', 'Ryuken', 'Mira', 'Sofie']
print(party_list)

party_list[1] = 'Ma'
print(party_list)

party_list.insert(0, 'Ryuken')
party_list.insert(2, 'Piet')
party_list.append('Jan')
print(party_list)

party_list.pop()
party_list.pop()
party_list.pop()
party_list.pop()
party_list.pop()
print(party_list)

del party_list[1]
del party_list[0]
print(party_list)
