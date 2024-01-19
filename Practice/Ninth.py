file = open('/Python/.vscode/poems.txt','r')
data = file.read()
print(data)
try: 
    data.find('twinkle')
    print('The peom contains the word twinkle')
except: 
    print("The peom doesn't contain the word twinkle")
line_count = 0 
for line in file: 
    print(line)
    line_count += 1
print(line_count)
