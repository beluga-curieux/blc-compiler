import os
import pretraitement

print("choisit le scripte parmis cette liste :")
scripts = dict(enumerate(os.listdir('script')))
print("  | "+"\n  | ".join([f"({i}) {t}" for i, t in scripts.items()]))
script = scripts[int(input("donner votre choix :\n"))]
print(script)

print("prétraitement :")
pretraitement.pretretement(script)
print("_"*30)
with open("script/"+script+'/'+script+".pre", "r") as file:
    print(file.read())
print("_"*30)
