# Skip all numbers divisible by 3 between 1 to 10. 
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)