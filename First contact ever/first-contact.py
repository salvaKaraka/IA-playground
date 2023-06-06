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


def cost(training_value):
    cost_result = 0
    for i in range(0, train_count):
        train_entry = train_data[i][0]
        expected = train_data[i][1]
        try_result = train_entry * training_value
        delta_error = try_result - expected
        cost_result += delta_error*delta_error
    cost_result /= train_count
    return cost_result

training_value=random.random() *10.0 #we generate a random value from zero to one            

eps = 1e-3
rate = 1e-3

for i in range(0, 1000):
    dcost = (cost(training_value+eps) - cost(training_value))/eps
    training_value -= rate*dcost
    print("Cost:", cost(training_value),"trained_value:", training_value)

print("enter a number:")
user_entry = int(input())

print("for entry value ",user_entry,", the result is (aprox):", training_value*user_entry)


