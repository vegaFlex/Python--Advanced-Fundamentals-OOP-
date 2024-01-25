command = input()
company_info = {}

while not command == 'End':
    companyName, employeeId = command.split(' -> ')
    if companyName not in company_info:
        company_info[companyName] = []

    if employeeId not in company_info[companyName]:
        company_info[companyName].append(employeeId)

    command = input()

sorted_company_info = sorted(company_info.items(), key=lambda x: x[0])

for company, id in sorted_company_info:
    print(f'{company}')

    for info in id:
        print(f'-- {info}')

