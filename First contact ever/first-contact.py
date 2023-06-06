#revision: 1.0
#date: 2023-06-05

import random;

train_data = [
    [0,0],
    [1,2],
    [2,4],
    [3,6],
    [4,8],
]

train_count = len(train_data)


def cost(random_entry):
    result = 0
    for i in range(0, train_count):
        train_entry = train_data[i][0]
        expected = train_data[i][1]
        try_result = train_entry * random_entry
        delta_error = try_result - expected
        result += delta_error*delta_error
        print("Cost:", cost(random_entry),"random_entry:", random_entry)
    result /= train_count
    return result

random_entry=random.random() *10.0 #we generate a random value from zero to one            

eps = 1e-3
rate = 1e-3

for i in range(0, 1000):
    dcost = (cost(random_entry+eps) - cost(random_entry))/eps
    random_entry -= rate*dcost

print("Result:", random_entry)

print("for entry value 5, the result is:", random_entry*5)


