import bs4

id_list = []
with open("arma-mods.html", "r") as file:
    soup = bs4.BeautifulSoup(file, "html.parser")
    data = soup.find_all('a')
    for i in data:
        id_list.append(i.text.split("id=")[1])
    file.close()

mod_id_string = ""
for i in id_list:
    mod_id_string = mod_id_string + f"mods/{i};"

with open("mod-list", "w") as file:
    file.write(mod_id_string)
    file.close()

with open("ref-docker-compose.yaml", "r") as ref_file:
    with open("docker-compose.yaml", "w") as file:
        for i in ref_file:
            if "MODS:" in i:
                file.write(f"      MODS: \"{mod_id_string}\"\n")
            else:
                file.write(i)
    file.close()