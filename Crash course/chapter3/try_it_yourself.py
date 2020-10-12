# try it yourself 3-4 - 3-7
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

# try it yourself 3-8 - 3-10
print('\n')
vacation = ['Azore', 'Canada', 'USA', 'Norway', 'Austria']
print(vacation)
print(sorted(vacation))
print(vacation)
print(sorted(vacation, reverse=True))
print(vacation)
vacation.reverse()
print(vacation)
vacation.reverse()
print(vacation)
vacation.sort()
print(vacation)
vacation.sort(reverse=True)
print(vacation)

# use len
print(len(vacation))

