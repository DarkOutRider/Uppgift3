import csv
import os
import locale


products = []           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)

def list_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx}) {product["name"]} ")


def view_products(idx, products):
    product = products[idx - 1]
    print(f"ID #: {product["id"]} \nNamn: {product["name"]} \n Desc: {product["desc"]} \n price: {product["price"]}")

def add_product(products):
    id = int(input("välj id: ")) #ej bra sätt
    name = input("namn på product: ")
    desc = input("desc på product: ")
    price = float(input("pris på product: "))
    quantity = int(input("kvantitet: "))

    product = products.append(
        {
            "id": id,       
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity 
        }
    )
    return products

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

    option = int(input("vad vill du göra? [1 = visa, 2= lägg till]"))

    if option == 1:
        idx = int(input("välj produkt med nummer: "))

        view_products(idx, products)

    elif option == 2:
        product = add_product(products)
        # print(f"Lade till: {product["name"]}")

    input()