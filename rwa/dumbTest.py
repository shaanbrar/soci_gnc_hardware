

myList = [0x7e,0x7e,0x5e,0x7e]

if myList[0:4] == 4*[0x7e]:
    print('all equal 0x7e')

if myList[0:4] != 4*[0x7e]:
    print('not all equal 0x7e')