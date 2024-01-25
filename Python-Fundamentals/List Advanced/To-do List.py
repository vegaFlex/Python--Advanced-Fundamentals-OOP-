notes = [0] * 10

command = input()

while command != 'End':
    importance, note = command.split('-')
    curr_index = int(importance) - 1
    notes[curr_index] = note
    command = input()

print([el for el in notes if not el == 0])

