# jabber = open("D:\\Programming\\Python\\Python Masterclass\\Sectie_8_IO_in_python\\sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

# with open("D:\\Programming\\Python\\Python Masterclass\\Sectie_8_IO_in_python\\sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("D:\\Programming\\Python\\Python Masterclass\\Sectie_8_IO_in_python\\sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("D:\\Programming\\Python\\Python Masterclass\\Sectie_8_IO_in_python\\sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("D:\\Programming\\Python\\Python Masterclass\\Sectie_8_IO_in_python\\sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

with open("D:\\Programming\\Python\\Python Masterclass\\Sectie_8_IO_in_python\\sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')
