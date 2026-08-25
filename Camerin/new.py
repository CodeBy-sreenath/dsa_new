tech_company = {

    "Engineering": {

        "manager": "Priya Sharma",

        "employees": ["Arjun", "Meera", "Rahul", "Sneha"],

        "skills_required": {"Python", "SQL", "Git", "Docker"},

        "budget": (500000, 750000),   # (min_budget, max_budget)

        "team_size": 4

    },

    "Marketing": {

        "manager": "Kabir Nair",

        "employees": ["Divya", "Anil", "Ritu"],

        "skills_required": {"SEO", "Content Writing", "Analytics", "Communication"},

        "budget": (200000, 350000),

        "team_size": 3

    },

    "Sales": {

        "manager": "Fatima Khan",

        "employees": ["Vikram", "Neha", "Rohit", "Pooja", "Sameer"],

        "skills_required": {"Negotiation", "CRM", "Communication"},

        "budget": (300000, 450000),

        "team_size": 5

    },

    "HR": {

        "manager": "Suresh Iyer",

        "employees": ["Anjali", "Karan"],

        "skills_required": {"Recruitment", "Communication", "Excel"},

        "budget": (150000, 200000),

        "team_size": 2

    }

}
for item in sorted(tech_company):
    print(item)
max_size=0
largest_department=''    
for department in tech_company:
    size=tech_company[department]['team_size']
    if size>max_size:
        max_size=size
        largest_department=department
print(max_size,largest_department)
all_employee=set()
for department in tech_company:
    employee=tech_company[department]['employees']
    for emp in employee:
        all_employee.add(emp)
print(all_employee)


engskills=tech_company['Engineering']['skills_required']
print(engskills)
market=tech_company["Marketing"]['skills_required']
print(market)
print(market.intersection(engskills))
min_budget=0
max_budget=0
count=0
for department in tech_company:
    total_min,total_max=tech_company[department]['budget']
    min_budget+=total_min
    max_budget=total_max
    count+=1
average_max=max_budget/count
average_min=min_budget/count
print(average_max,average_min)
print(sorted(tech_company,key=lambda department:tech_company[department]['team_size'],reverse=True))
lst=[]
for department in tech_company:
    skill=tech_company[department]['skills_required']
    if 'Communication' in skill:
        lst.append(department)
print(lst)
Sales=tech_company['Sales']['employees']
Marketing=tech_company["Marketing"]['employees']
Sales_set=set(Sales)
Marketing_set=set(Marketing)
new=Sales_set.union(Marketing_set)
print(list(new)) 
new_dict={}
for department in tech_company:
    man=tech_company[department]['manager']
    new_dict[department]=man
print(new_dict)
managers={dept:tech_company[dept]['manager'] for dept in tech_company}
print(managers)           

                           
   
