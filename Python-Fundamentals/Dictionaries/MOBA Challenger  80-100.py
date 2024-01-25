players = {}
line = input()

while not line == 'Season end':
    if '->' in line:
        player, position, skill = line.split(' -> ')
        skill = int(skill)
        if player not in players:
            players[player] = {position: skill}
        else:
            if position in players[player]:
                if skill > players[player][position]:
                    players[player][position] = skill
            else:
                players[player][position] = skill

    elif 'vs' in line:
        player_1, player_2 = line.split(' vs ')
        if player_1 in players and player_2 in players:
            for position in players[player_1]:
                if position in players[player_2]:
                    if players[player_1][position] > players[player_2][position]:
                        del players[player_2]
                    elif players[player_1][position] < players[player_2][position]:
                        del players[player_1]
    line = input()

max_skills = {}
for player in players:
    max_skills[player] = sum(players[player].values())
    sorted_skills = dict(sorted(players[player].items(), key=lambda x: (-x[1])))
    players[player] = sorted_skills
max_skills = dict(sorted(max_skills.items(), key=lambda x: (-x[1])))

for name in max_skills:
    print(f"{name}: {max_skills[name]} skill")
    for skill in players[name]:
        print(f"- {skill} <::> {players[name][skill]}")

