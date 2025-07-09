with open("text data.txt",'r') as file:
    paper=file.read()
print(len(paper.split()),"words are there in file")
