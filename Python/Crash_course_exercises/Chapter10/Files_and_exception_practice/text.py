#Exercise 10.10

# with open(filename,encoding="utf-8") as f:
#     contents = f.read()
#     x = contents.count("the ")
#     print()

def count_text(filenames):
    for filename in filenames:
        with open(filename,encoding="utf-8") as f:
            contents = f.read()
            count = contents.count("the ")
            print(count)           

texts = ["beowulf.txt","dracula.txt","the_penultimate.txt"]
count_text(texts)    