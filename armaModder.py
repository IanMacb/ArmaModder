import bs4

id_list = []
with open("Anti with the bois.html", "r") as file:
    soup = bs4.BeautifulSoup(file, "html.parser")
    data = soup.find_all('a')
    for i in data:
        id_list.append(i.text.split("id=")[1])
    file.close()

with open("mod-list", "w") as file:
    for i in id_list:
        file.write(f"mods/{i};")
    file.close()
