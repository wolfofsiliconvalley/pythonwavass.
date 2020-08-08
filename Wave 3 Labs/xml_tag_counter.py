tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if (token.startswith('<') and token.endswith('>')):
        count += 1
 


print(count) 
