# Skip all even numbers from 0 to 9. 
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)