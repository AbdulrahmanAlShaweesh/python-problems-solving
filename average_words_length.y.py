

""" . Average Word Length """

total_world = 0
counter = 0
words = ""

while True :
    
    
    word = input('Enter a word or press empty to exit ? ').strip()
    
    if word == "" :
        break 
    
    counter += 1
    words += word 
   
print(f'The average words length is {len(words) / counter:.2f}')
    
    
    
    