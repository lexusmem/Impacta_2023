import pprint


dic = {
    "musicas": [
        {"nome": "Hey Jude", "banda": "Beatles"},
        {"nome": "November Rain", "banda": "Guns N' Roses"},
        {"nome": "How Deep Is Your Love", "banda": "Bee Gees"},
    ],
    "filmes": {"X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira", "Magneto", "Ciclope", "Gambit"],
               "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão America", "Thor", "Capitā Marvel", "Homem-Aranha"],
               "Star Wars": ["Luke", "Leia", "C-3PO", "Darth Vader", "Obi-Wan", "Yoda", "R2-D2", "Han Solo", "Chewbacca"]
               }
}


def func1(a, b, c, d):
    for x in a:
        if x[b] == d:
            return x[c]
    return "naosei"


pprint.pprint(dic['musicas'])

pprint.pprint(dic['filmes'])

# print("Hey Jude" in dic["musicas"]["Beatles"])
# print("Hey Jude" in dic["musicas"][0]['nome'])

# print(dic["musicas"]["Bee Gees"] == "How Deep Is Your Love")
# print(dic["musicas"][2]['nome'] == "How Deep Is Your Love")

# print("November Rain" == dic["musicas"][1]["banda"])
# print("November Rain" == dic["musicas"][1]["nome"])


# print(func1(dic["musicas"], "banda", "nome",
#       "Guns N' Roses") == "November Rain")


# print(func1(dic["filmes"], 1, 2, "Homem de Ferro"))


# print("Chewbacca" in dic.filmes.Star Wars)


# print("Han Solo" in dic["filmes"]["Star Wars"])

# print("Han Solo" in dic["jogos"]["Star Wars"])

# print(func1(dic["musicas"], "banda", "nome", "Hey Jude") == "Beatles")

# print("Super-homem" in dic["filmes"]["Avengers"])

# print(dic["filmes"]["X-men"][3] == "Vampira")

# print(dic["filmes"]["Star Wars"][2] == "Leia")

# print(dic["musicas"][2]["nome"] == "How Deep Is Your Love")

# print("Hey Jude" == dic["musicas"][0])

# print(dic["musicas"][0]["banda"] == "Beatles")

# print(func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América"))

# print("Han Solo" in dic["jogos"]["Mortal Kombat II"])

# print("Thor" in dic["filmes"]["Avengers"])

# print("Homem de Ferro" in dic["musicas"][2])

# print(dic[dic] + dic[dic[dic]]])
