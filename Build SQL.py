import sqlite3, csv, os

sql = sqlite3.connect("./epl.sql")
cur = sql.cursor()


file = []
for r, d, f in os.walk("./EPL Data/"):
    file = f


for i in file:
    data = []
    head = []
    with open("./EPL Data/"+i, "r") as csvfile:
        csvReader = csv.reader(csvfile)
        for j in csvReader:
            data.append(j)
        head = data[0]
        data = data[1:]
        csvfile.close()
    head_type = []
    for h in head:
        print(i, h)
        head_type.append(h + " " + input("Type: "))
    cur.execute("CREATE TABLE {0} ({1});".format(i.split(".")[0], ", ".join(head_type)))
    cur.executemany("INSERT INTO {0} VALUES ({1});".format(i.split(".")[0], ", ".join(["?" for i in range(len(head))])),
                    data)
    sql.commit()


sql.close()

print()



