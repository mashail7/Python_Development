company = {}
while True:
    command = input()
    if command == "End":
        break

    arguments = command.split(" -> ")
    company_name = arguments[0]
    employee_id = arguments[1]

    if company_name in company:
        if employee_id in company[company_name]:
            continue
        company[company_name].append(employee_id)

    elif company_name not in company:
        company[company_name] = [employee_id]

for company, employees in company.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")