import os



name = input("le nom du scripte :\n    |> ")

dir_path = "script/" + name
os.makedirs(dir_path, exist_ok=True)

extentions = [".blc", ".out"]
extentions += [".inp"] if input("créé un fichier d'in put ? (y/n)")=="y" else []

for ext in extentions:
    with open(dir_path + '/' + name + ext, 'w') as file:
        pass