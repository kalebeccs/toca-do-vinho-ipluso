import random

USERS = [
    {
        "name": "Alice Martins",
        "email": "alice.martins@example.com",
        "password": "hashed_password_1",
        "dob": "1990-05-15",
        "vat_number": "123456789",
        "address_1": "Rua das Flores, 123",
        "role": "user",
    },
    {
        "name": "Carlos Souza",
        "email": "carlos.souza@example.com",
        "password": "hashed_password_2",
        "dob": "1985-10-23",
        "vat_number": "987654321",
        "address_1": "Avenida Central, 456",
        "role": "user",
    },
    {
        "name": "Bruno Lima",
        "email": "bruno.lima@example.com",
        "password": "hashed_password_3",
        "dob": "1992-07-21",
        "vat_number": "123123123",
        "address_1": "Rua do Sol, 789",
        "role": "user",
    },
    {
        "name": "Daniela Costa",
        "email": "daniela.costa@example.com",
        "password": "hashed_password_4",
        "dob": "1988-11-30",
        "vat_number": "321321321",
        "address_1": "Avenida das Américas, 101",
        "role": "user",
    },
    {
        "name": "Eduardo Silva",
        "email": "eduardo.silva@example.com",
        "password": "hashed_password_5",
        "dob": "1995-03-12",
        "vat_number": "456456456",
        "address_1": "Rua das Palmeiras, 202",
        "role": "user",
    },
    {
        "name": "Fernanda Oliveira",
        "email": "fernanda.oliveira@example.com",
        "password": "hashed_password_6",
        "dob": "1991-09-17",
        "vat_number": "654654654",
        "address_1": "Avenida Paulista, 303",
        "role": "user",
    },
    {
        "name": "Gabriel Santos",
        "email": "gabriel.santos@example.com",
        "password": "hashed_password_7",
        "dob": "1987-12-25",
        "vat_number": "789789789",
        "address_1": "Rua das Laranjeiras, 404",
        "role": "user",
    },
    {
        "name": "Helena Ferreira",
        "email": "helena.ferreira@example.com",
        "password": "hashed_password_8",
        "dob": "1993-06-05",
        "vat_number": "987987987",
        "address_1": "Avenida Brasil, 505",
        "role": "user",
    },
    {
        "name": "Igor Almeida",
        "email": "igor.almeida@example.com",
        "password": "hashed_password_9",
        "dob": "1990-01-15",
        "vat_number": "111222333",
        "address_1": "Rua das Acácias, 606",
        "role": "user",
    },
    {
        "name": "Juliana Rocha",
        "email": "juliana.rocha@example.com",
        "password": "hashed_password_10",
        "dob": "1989-04-22",
        "vat_number": "444555666",
        "address_1": "Avenida Independência, 707",
        "role": "user",
    },
    {
        "name": "Lucas Pereira",
        "email": "lucas.pereira@example.com",
        "password": "hashed_password_11",
        "dob": "1994-08-30",
        "vat_number": "777888999",
        "address_1": "Rua das Magnólias, 808",
        "role": "user",
    },
    {
        "name": "Mariana Gomes",
        "email": "mariana.gomes@example.com",
        "password": "hashed_password_12",
        "dob": "1991-02-14",
        "vat_number": "000111222",
        "address_1": "Avenida Central, 909",
        "role": "user",
    },
    {
        "name": "Nicolas Ribeiro",
        "email": "nicolas.ribeiro@example.com",
        "password": "hashed_password_13",
        "dob": "1986-05-19",
        "vat_number": "333444555",
        "address_1": "Rua das Hortênsias, 1010",
        "role": "user",
    },
    {
        "name": "Olivia Carvalho",
        "email": "olivia.carvalho@example.com",
        "password": "hashed_password_14",
        "dob": "1992-11-11",
        "vat_number": "666777888",
        "address_1": "Avenida das Nações, 1111",
        "role": "user",
    },
    {
        "name": "Pedro Azevedo",
        "email": "pedro.azevedo@example.com",
        "password": "hashed_password_15",
        "dob": "1988-03-03",
        "vat_number": "999000111",
        "address_1": "Rua das Rosas, 1212",
        "role": "user",
    },
    {
        "name": "Quintino Mendes",
        "email": "quintino.mendes@example.com",
        "password": "hashed_password_16",
        "dob": "1995-07-07",
        "vat_number": "222333444",
        "address_1": "Avenida do Contorno, 1313",
        "role": "user",
    },
    {
        "name": "Rafaela Teixeira",
        "email": "rafaela.teixeira@example.com",
        "password": "hashed_password_17",
        "dob": "1990-10-10",
        "vat_number": "555666777",
        "address_1": "Rua das Amendoeiras, 1414",
        "role": "user",
    },
    {
        "name": "Samuel Nunes",
        "email": "samuel.nunes@example.com",
        "password": "hashed_password_18",
        "dob": "1987-01-01",
        "vat_number": "888999000",
        "address_1": "Avenida dos Estados, 1515",
        "role": "user",
    },
    {
        "name": "Tatiana Barbosa",
        "email": "tatiana.barbosa@example.com",
        "password": "hashed_password_19",
        "dob": "1993-09-09",
        "vat_number": "111222333",
        "address_1": "Rua das Oliveiras, 1616",
        "role": "user",
    },
    {
        "name": "Ubirajara Lopes",
        "email": "ubirajara.lopes@example.com",
        "password": "hashed_password_20",
        "dob": "1989-12-12",
        "vat_number": "444555666",
        "address_1": "Avenida das Palmeiras, 1717",
        "role": "user",
    },
    {
        "name": "Vanessa Martins",
        "email": "vanessa.martins@example.com",
        "password": "hashed_password_21",
        "dob": "1994-06-06",
        "vat_number": "777888999",
        "address_1": "Rua das Camélias, 1818",
        "role": "admin",
    },
    {
        "name": "Wagner Costa",
        "email": "wagner.costa@example.com",
        "password": "hashed_password_22",
        "dob": "1991-04-04",
        "vat_number": "000111222",
        "address_1": "Avenida das Flores, 1919",
        "role": "admin",
    },
    {
        "name": "Xavier Silva",
        "email": "",
        "password": "hashed_password_23",
        "dob": "1986-08-08",
        "vat_number": "333444555",
        "address_1": "Rua das Orquídeas, 2020",
        "role": "admin",
    }
]

WINES = [
    {
        "brand": "Vinhas do Sul",
        "name": "Cabernet Sauvignon Reserva",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2018,
        "country_of_origin": "Brasil",
        "region": "Serra Gaúcha",
        "description": "Vinho encorpado com notas de frutas vermelhas e especiarias.",
    },
    {
        "brand": "Monte Claro",
        "name": "Chardonnay Vintage",
        "type": "Branco",
        "alcohol": 12.5,
        "year": 2020,
        "country_of_origin": "Chile",
        "region": "Vale do Maule",
        "description": "Aromas de pêssego e toques de baunilha.",
    },
    {
        "brand": "Quinta do Vale",
        "name": "Merlot Reserva",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2019,
        "country_of_origin": "Portugal",
        "region": "Douro",
        "description": "Notas de ameixa e chocolate com taninos suaves.",
    },
    {
        "brand": "Bodega del Sol",
        "name": "Malbec Gran Reserva",
        "type": "Tinto",
        "alcohol": 14.5,
        "year": 2017,
        "country_of_origin": "Argentina",
        "region": "Mendoza",
        "description": "Aromas de frutas negras e especiarias com final persistente.",
    },
    {
        "brand": "Château de la Loire",
        "name": "Sauvignon Blanc",
        "type": "Branco",
        "alcohol": 12.0,
        "year": 2021,
        "country_of_origin": "França",
        "region": "Loire",
        "description": "Fresco e cítrico com notas de maçã verde.",
    },
    {
        "brand": "Vinha da Serra",
        "name": "Syrah",
        "type": "Tinto",
        "alcohol": 13.8,
        "year": 2018,
        "country_of_origin": "Brasil",
        "region": "Vale dos Vinhedos",
        "description": "Aromas de frutas vermelhas maduras e pimenta preta.",
    },
    {
        "brand": "Cantina del Vino",
        "name": "Pinot Grigio",
        "type": "Branco",
        "alcohol": 12.5,
        "year": 2020,
        "country_of_origin": "Itália",
        "region": "Vêneto",
        "description": "Leve e refrescante com notas de pera e limão.",
    },
    {
        "brand": "Vignoble du Rhône",
        "name": "Grenache",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2019,
        "country_of_origin": "França",
        "region": "Rhône",
        "description": "Frutado com notas de morango e especiarias.",
    },
    {
        "brand": "Bodega Andina",
        "name": "Torrontés",
        "type": "Branco",
        "alcohol": 13.0,
        "year": 2021,
        "country_of_origin": "Argentina",
        "region": "Salta",
        "description": "Aromas florais e cítricos com acidez equilibrada.",
    },
    {
        "brand": "Quinta da Boa Vista",
        "name": "Touriga Nacional",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2018,
        "country_of_origin": "Portugal",
        "region": "Dão",
        "description": "Complexo com notas de frutas escuras e violetas.",
    },
    {
        "brand": "Vinha do Mar",
        "name": "Verdejo",
        "type": "Branco",
        "alcohol": 12.0,
        "year": 2020,
        "country_of_origin": "Espanha",
        "region": "Rueda",
        "description": "Fresco e frutado com notas de melão e ervas.",
    },
    {
        "brand": "Château de Bordeaux",
        "name": "Cabernet Franc",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2019,
        "country_of_origin": "França",
        "region": "Bordeaux",
        "description": "Elegante com notas de framboesa e pimenta verde.",
    },
    {
        "brand": "Vinha do Norte",
        "name": "Tempranillo",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2018,
        "country_of_origin": "Espanha",
        "region": "Rioja",
        "description": "Aromas de cereja e baunilha com taninos suaves.",
    },
    {
        "brand": "Cantina Toscana",
        "name": "Chianti Classico",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2019,
        "country_of_origin": "Itália",
        "region": "Toscana",
        "description": "Notas de cereja e especiarias com acidez equilibrada.",
    },
    {
        "brand": "Vignoble de Provence",
        "name": "Rosé",
        "type": "Rosé",
        "alcohol": 12.5,
        "year": 2021,
        "country_of_origin": "França",
        "region": "Provence",
        "description": "Fresco e frutado com notas de morango e melancia.",
    },
    {
        "brand": "Bodega del Norte",
        "name": "Carmenere",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2018,
        "country_of_origin": "Chile",
        "region": "Colchagua",
        "description": "Aromas de frutas negras e pimenta com taninos macios.",
    },
    {
        "brand": "Quinta do Douro",
        "name": "Vinho Verde",
        "type": "Branco",
        "alcohol": 11.5,
        "year": 2021,
        "country_of_origin": "Portugal",
        "region": "Minho",
        "description": "Leve e refrescante com notas de limão e maçã verde.",
    },
    {
        "brand": "Château de Bourgogne",
        "name": "Pinot Noir",
        "type": "Tinto",
        "alcohol": 13.0,
        "year": 2019,
        "country_of_origin": "França",
        "region": "Bourgogne",
        "description": "Elegante com notas de cereja e terra úmida.",
    },
    {
        "brand": "Vinha do Sul",
        "name": "Cabernet Sauvignon",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2018,
        "country_of_origin": "Brasil",
        "region": "Serra Gaúcha",
        "description": "Vinho encorpado com notas de frutas vermelhas e especiarias.",
    },
    {
        "brand": "Monte Claro",
        "name": "Chardonnay",
        "type": "Branco",
        "alcohol": 12.5,
        "year": 2020,
        "country_of_origin": "Chile",
        "region": "Vale do Maule",
        "description": "Aromas de pêssego e toques de baunilha.",
    },
    {
        "brand": "Quinta do Vale",
        "name": "Merlot",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2019,
        "country_of_origin": "Portugal",
        "region": "Douro",
        "description": "Notas de ameixa e chocolate com taninos suaves.",
    },
    {
        "brand": "Bodega del Sol",
        "name": "Malbec",
        "type": "Tinto",
        "alcohol": 14.5,
        "year": 2017,
        "country_of_origin": "Argentina",
        "region": "Mendoza",
        "description": "Aromas de frutas negras e especiarias com final persistente.",
    },
    {
        "brand": "Château de la Loire",
        "name": "Sauvignon Blanc",
        "type": "Branco",
        "alcohol": 12.0,
        "year": 2021,
        "country_of_origin": "França",
        "region": "Loire",
        "description": "Fresco e cítrico com notas de maçã verde.",
    },
    {
        "brand": "Vinha da Serra",
        "name": "Syrah",
        "type": "Tinto",
        "alcohol": 13.8,
        "year": 2018,
        "country_of_origin": "Brasil",
        "region": "Vale dos Vinhedos",
        "description": "Aromas de frutas vermelhas maduras e pimenta preta.",
    },
    {
        "brand": "Cantina del Vino",
        "name": "Pinot Grigio",
        "type": "Branco",
        "alcohol": 12.5,
        "year": 2020,
        "country_of_origin": "Itália",
        "region": "Vêneto",
        "description": "Leve e refrescante com notas de pera e limão.",
    },
    {
        "brand": "Vignoble du Rhône",
        "name": "Grenache",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2019,
        "country_of_origin": "França",
        "region": "Rhône",
        "description": "Frutado com notas de morango e especiarias.",
    },
    {
        "brand": "Bodega Andina",
        "name": "Torrontés",
        "type": "Branco",
        "alcohol": 13.0,
        "year": 2021,
        "country_of_origin": "Argentina",
        "region": "Salta",
        "description": "Aromas florais e cítricos com acidez equilibrada.",
    },
    {
        "brand": "Quinta da Boa Vista",
        "name": "Touriga Nacional",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2018,
        "country_of_origin": "Portugal",
        "region": "Dão",
        "description": "Complexo com notas de frutas escuras e violetas.",
    },
    {
        "brand": "Vinha do Mar",
        "name": "Verdejo",
        "type": "Branco",
        "alcohol": 12.0,
        "year": 2020,
        "country_of_origin": "Espanha",
        "region": "Rueda",
        "description": "Fresco e frutado com notas de melão e ervas.",
    },
    {
        "brand": "Château de Bordeaux",
        "name": "Cabernet Franc",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2019,
        "country_of_origin": "França",
        "region": "Bordeaux",
        "description": "Elegante com notas de framboesa e pimenta verde.",
    },
    {
        "brand": "Vinha do Norte",
        "name": "Tempranillo",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2018,
        "country_of_origin": "Espanha",
        "region": "Rioja",
        "description": "Aromas de cereja e baunilha com taninos suaves.",
    },
    {
        "brand": "Cantina Toscana",
        "name": "Chianti Classico",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2019,
        "country_of_origin": "Itália",
        "region": "Toscana",
        "description": "Notas de cereja e especiarias com acidez equilibrada.",
    },
    {
        "brand": "Vignoble de Provence",
        "name": "Rosé",
        "type": "Rosé",
        "alcohol": 12.5,
        "year": 2021,
        "country_of_origin": "França",
        "region": "Provence",
        "description": "Fresco e frutado com notas de morango e melancia.",
    },
    {
        "brand": "Bodega del Norte",
        "name": "Carmenere",
        "type": "Tinto",
        "alcohol": 14.0,
        "year": 2018,
        "country_of_origin": "Chile",
        "region": "Colchagua",
        "description": "Aromas de frutas negras e pimenta com taninos macios.",
    },
    {
        "brand": "Quinta do Douro",
        "name": "Vinho Verde",
        "type": "Branco",
        "alcohol": 11.5,
        "year": 2021,
        "country_of_origin": "Portugal",
        "region": "Minho",
        "description": "Leve e refrescante com notas de limão e maçã verde.",
    },
    {
        "brand": "Château de Bourgogne",
        "name": "Pinot Noir",
        "type": "Tinto",
        "alcohol": 13.0,
        "year": 2019,
        "country_of_origin": "França",
        "region": "Bourgogne",
        "description": "Elegante com notas de cereja e terra úmida.",
    },
    {
        "brand": "Vinha do Sul",
        "name": "Cabernet Sauvignon",
        "type": "Tinto",
        "alcohol": 13.5,
        "year": 2018,
        "country_of_origin": "Brasil",
        "region": "Serra Gaúcha",
        "description": "Vinho encorpado com notas de frutas vermelhas e especiarias.",
    },
    {
        "brand": "Monte Claro",
        "name": "Chardonnay",
        "type": "Branco",
        "alcohol": 12.5,
        "year": 2020,
        "country_of_origin": "Chile",
        "region": "Vale do Maule",
        "description": "Aromas de pêssego e toques de baunilha.",
    }
]

STOCK = []
for i in range(1, 41):
    quantity = random.choice([10, 15, 20, 25, 30, 35, 40, 45, 50])
    STOCK.append({
        "fk_wine": i,
        "movement_type": "purchase",
        "quantity": quantity,
        "reason": "Inicialização de estoque"
    })
    
PRICES = []
for i in range(1, 41):
    purchase_price = random.uniform(10.0, 30.0)
    sale_price = purchase_price * 1.25
    PRICES.append({"fk_wine": i, "price_type": "purchase", "price": round(purchase_price, 2)})
    PRICES.append({"fk_wine": i, "price_type": "sale", "price": round(sale_price, 2)})

PURCHASES = [
    {"fk_user": 1, "total_value": 120.0},
    {"fk_user": 1, "total_value": 70.0}
]

PURCHASE_ITEMS = [
    {"fk_purchase": 1, "fk_wine": 1, "quantity": 2, "unit_price": 70.0},
    {"fk_purchase": 2, "fk_wine": 2, "quantity": 1, "unit_price": 50.0}
]
