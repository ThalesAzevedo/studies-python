import os

print("Renomeando Arquivos")

path = "/Users/thales/desktop/python/script/desafios"

files = os.listdir(os.fspath(path))
count = 0
for file in files:
    if file[0] == 'e' :
        content = []
        print("Nome Antigo: {}".format(file))
        with open(path+"/"+file, 'r', encoding="utf8") as f:
            count += 1
            for line in f:
                content.append(f.readline())
            data = content[0].split("'")
            title = ""
            if "tema" in data[0]:
                title = data[1]
            else:
                title = data[3]
            title = "{}{}_{}.py".format("ex", count, title.strip().lower().replace(" ", "_").replace(",", "").replace(".", "").replace("!", ""))
            print("Nome Atual :{}".format(title))
        os.rename(path + "/" + file, path + "/" + title)


