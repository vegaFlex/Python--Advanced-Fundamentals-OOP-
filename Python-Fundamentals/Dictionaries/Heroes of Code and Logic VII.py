n = int(input())
heroes = {}

for _ in range(n):
    hero_name, hit_points, mana_points = input().split()
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    heroes[hero_name] = [hit_points, mana_points]

command = input()
while not command == 'End':
    if 'CastSpell' in command:
        command1, hero_name1, mana_points_needed, spell_name = command.split(' - ')
        mana_points_needed = int(mana_points_needed)

        if heroes[hero_name1][1] >= mana_points_needed:
            heroes[hero_name1][1] -= mana_points_needed
            print(f"{hero_name1} has successfully cast {spell_name} and now has {heroes[hero_name1][1]} MP!")
        else:
            print(f"{hero_name1} does not have enough MP to cast {spell_name}!")

    elif 'TakeDamage' in command:
        command2, hero_name2, damage, attacker = command.split(' - ')
        damage = int(damage)
        heroes[hero_name2][0] -= damage

        if heroes[hero_name2][0] > 0:
            print(f"{hero_name2} was hit for {damage} HP by {attacker} and now has {heroes[hero_name2][0]} HP left!")
        else:
            print(f"{hero_name2} has been killed by {attacker}!")
            del heroes[hero_name2]

    elif 'Recharge' in command:
        command3, hero_name3, amount = command.split(' - ')
        amount = int(amount)

        if heroes[hero_name3][1] + amount > 200:
            amount = 200 - heroes[hero_name3][1]
            heroes[hero_name3][1] = 200
        else:
            heroes[hero_name3][1] += amount

        print(f"{hero_name3} recharged for {amount} MP!")

    elif 'Heal' in command:
        command4, hero_name4, amount4 = command.split(' - ')
        amount4 = int(amount4)

        if heroes[hero_name4][0] + amount4 > 100:
            amount4 = 100 - heroes[hero_name4][0]
            heroes[hero_name4][0] = 100
        else:
            heroes[hero_name4][0] += amount4

        print(f"{hero_name4} healed for {amount4} HP!")
    command = input()

for name, values in heroes.items():
    print(name)
    hp = values[0]
    mp = values[1]
    print(f' HP: {hp}')
    print(f' MP: {mp}')