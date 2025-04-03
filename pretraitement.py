import re
def pretretement(src):
    with open('script/'+src+'/'+src+".blc", "r") as f:
        text = f.read()

    text = sup_comentaire(text)
    text = sup_lignes_vides(text)

    save(src, text)


def save(src, text):
    with open(f"script/{src}/{src}.pre", "w") as f:
        f.write(text)

def sup_comentaire(text):
    return re.sub(r'\/\/.*$', '', text, flags=re.MULTILINE)

def sup_lignes_vides(text):
    return re.sub(r'^\s*\n|\n$', '', text, flags=re.MULTILINE)