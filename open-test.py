import csv
import os
import locale


products = []           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)

def list_products(products):
    for idx, product in enumerate(products, 0):
        print(f"{idx}) {product["name"]} ")


def view_products(idx, products):
    product = products[idx]
    print(f"ID #: {product["id"]} \nNamn: {product["name"]} \n Desc: {product["desc"]} \n price: {product["price"]} kr \n quantity: {product["quantity"]}")

def add_product(products):

    find_max = max(products, key=lambda id: id["id"])
    max_id = find_max["id"]
    print(max_id)

    new_id = max_id + 1

    name = input("namn på product: ")
    desc = input("desc på product: ")
    price = float(input("pris på product: "))
    quantity = int(input("kvantitet: "))


    product = products.append(
        {
            "id": new_id,       
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity 
        }
    )
    return product

def change_products(products):
    name = input("namn på product: ")
    desc = input("desc på product: ")
    price = float(input("pris på product: "))
    quantity = int(input("kvantitet: "))


    product = products[idx](
        {      
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity 
        }
    )
    return product

def load_data(filename): 
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])

            
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )

            "return products"



        

#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

load_data('db_products.csv')
os.system("cls")

while True:
    list_products(products)

    option = int(input("vad vill du göra? [1 = visa, 2 = lägg till, 3 = ta bort]"))

    if option == 1:
        idx = int(input("välj produkt med nummer: "))
        os.system("cls")
        view_products(idx, products)
        

    elif option == 2:
        product = add_product(products)
        # print(f"Lade till: {product["name"]}")

    elif option == 3:
        idx = int(input("välj vilken product med id nummer: "))
        products.pop(idx)

    elif option == 4:
        idx = int(input("välj vilken product med id nummer: "))
        change_products(products)
    input()