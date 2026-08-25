
online_store = {

    "Electronics": {

        "products": {

            "Laptop": {"price": 55000, "stock": 12, "tags": {"portable", "work", "gaming"}},

            "Smartphone": {"price": 25000, "stock": 30, "tags": {"portable", "communication"}},

            "Headphones": {"price": 2000, "stock": 50, "tags": {"audio", "portable"}}

        },

        "suppliers": ("TechCorp", "GadgetHub", "ElectroWorld"),

        "monthly_sales": [45, 60, 55, 70, 80, 65]

    },

    "Clothing": {

        "products": {

            "T-Shirt": {"price": 500, "stock": 100, "tags": {"casual", "cotton"}},

            "Jeans": {"price": 1500, "stock": 60, "tags": {"casual", "denim"}},

            "Jacket": {"price": 3000, "stock": 25, "tags": {"winter", "formal"}}

        },

        "suppliers": ("FashionHub", "StyleWorld"),

        "monthly_sales": [120, 100, 90, 150, 200, 180]

    },

    "Books": {

        "products": {

            "Python Guide": {"price": 800, "stock": 40, "tags": {"programming", "education"}},

            "Novel": {"price": 400, "stock": 70, "tags": {"fiction", "leisure"}}

        },

        "suppliers": ("BookWorld", "ReadMore", "PagesInc"),

        "monthly_sales": [30, 35, 40, 25, 20, 45]

    }

}
for department in online_store:
    print(department)
for category in online_store:
    cat=online_store[category]['products']
    print(category,len(cat))
count=0    
stk=online_store["Electronics"]['products']
print(stk)
for item in stk:
    count+=stk[item]['stock']
print(count)
 
max_price=0
section=''
dept=''
for item in online_store:
    new=online_store[item]['products']
    for items in new:
        price=new[items]['price']
        if price>max_price:
            max_price=price
            section=items
            dept=item
print(max_price,section,dept)
new_set=set()
for items in online_store:
  new=online_store[items]['products']
  for item in new:
      tag=new[item]['tags']
      for ta in tag:
          new_set.add(ta)
print(new_set)           
elec_supply=set(online_store["Electronics"]['suppliers'])
book_supply=set(online_store["Books"]['suppliers'])
common=elec_supply.intersection(book_supply)
print(common)
#20
max_total=0
sec='' 
for item in online_store:
    total=sum(online_store[item]['monthly_sales'])
    if total>max_total:
        max_total=total
        sec=item
print(max_total,sec)        


new_dic={ category: set(online_store[category]['products'].keys()) for category in online_store}
print(new_dic)


    

