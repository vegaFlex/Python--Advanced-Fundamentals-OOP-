n = int(input())
pieces = {}
for _ in range(n):
    cur_piece, cur_composer, cur_key = input().split('|')

    pieces[cur_piece] = [cur_composer, cur_key]

command = input()
while command != 'Stop':
    if 'Add' in command:
        command1, piece, composer, key = command.split('|')
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif 'Remove' in command:
        command2, piece2 = command.split('|')
        if piece2 not in pieces:
            print(f"Invalid operation! {piece2} does not exist in the collection.")
        else:
            del pieces[piece2]
            print(f"Successfully removed {piece2}!")

    elif 'ChangeKey' in command:
        command3, piece3, new_key = command.split('|')
        if piece3 not in pieces:
            print(f"Invalid operation! {piece3} does not exist in the collection.")
        else:
            pieces[piece3][1] = new_key
            print(f"Changed the key of {piece3} to {new_key}!")

    command = input()

sorted_pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1])))
for PIECE, VALUES in sorted_pieces.items():
    COMPOSER = VALUES[0]
    KEY = VALUES[1]
    print(f"{PIECE} -> Composer: {COMPOSER}, Key: {KEY}")
