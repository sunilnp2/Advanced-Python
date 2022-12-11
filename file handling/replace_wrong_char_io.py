words = ['donkey', 'universe',  'nepal']

with open ('paragraph.txt', 'r') as f:
    para = f.read()
    for word in words: 
        correct = para.replace(word, "#####")

with open( 'paragraph.txt', 'w') as f:
    f.write(correct)
