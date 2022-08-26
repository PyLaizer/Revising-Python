
mylist = [
    "Today is Friday: 26th of August 2022",
    "Currently at NYSC zappas secetariat, Lagos Island",
    "A very weird day today buh I hope I leave soon"
]

filename = "text.txt"
with open(filename,"a") as file_object:
    for content in mylist:
        file_object.write(f"\n{content}")