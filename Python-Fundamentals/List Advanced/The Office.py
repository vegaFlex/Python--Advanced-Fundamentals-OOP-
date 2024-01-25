happiness_list = [int(el) for el in input().split()]
factor = int(input())

total_happiness = [el*factor for el in happiness_list]
happiness_border = sum(total_happiness) / len(total_happiness)

happy_people = [el for el in total_happiness if el >= happiness_border]
sad_people = [el for el in total_happiness if el < happiness_border]

if len(happy_people) >= len(sad_people):
    print(f'Score: {len(happy_people)}/{len(happiness_list)}. Employees are happy!')
else:
    print(f'Score: {len(happy_people)}/{len(happiness_list)}. Employees are not happy!')

