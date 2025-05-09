import sys

print("Start writing text (enter 'q' to quit):")


sc = 'snakecase'
uc = 'uppercase'

for line in sys.stdin:
    print(line)
    if line.strip() == 'q':  
        break
    text = line.strip()      
    sys.stdout.write(text.upper() + '\n') 
    
print("Exit")
