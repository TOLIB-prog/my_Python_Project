for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j:<2} * {i:>2} = {j * i:<4}', end="\t")
    print(" ")
    
for y in range(1, 10):
    for g  in range(1, 10):
        print(f'{y * g:^15}', end="\t")
    print(" ")
