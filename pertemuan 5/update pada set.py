hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimli'}
human = {'boromir'}
maiar = {'gandalf'}

fellowship_2 = hobbits.copy()

fellowship_2.update(dunedain)
fellowship_2.update(elf)
fellowship_2.update(dwarf)
fellowship_2.update(human)
fellowship_2.update(maiar)

print("fellowship_2:", fellowship_2)