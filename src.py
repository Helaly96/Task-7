import csv


"... we are going to create an array of dictionaries and print them all..."

st_dic = []

true = 1

while true:
    dummy = input("Please Enter name, email, mobile, university, major")
    x = dummy.split(",")

    if "Stop" in x:
        break

    dict ={"Name":x[0],"Email":x[1],"Mobile":x[2],"University":x[3],"Major":x[4]}
    st_dic.append(dict)

f2 = open("data3.csv" , "w")

with open("data3.csv", "r+") as f:
    fieldnames=["Name","Email","Mobile","University","Major"]
    writer = csv.DictWriter(f , fieldnames=fieldnames)
    writer.writeheader()
    for item in st_dic:
        writer.writerow({  "Name":item["Name"], "Email":item["Email"], "Mobile":item["Mobile"], "University":item["University"], "Major":item["Major"]    })
    f.close()







