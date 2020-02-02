


# 1 - An empty Network
weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction

# 2 - Inserting one input datapoint
number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]

# 3 - Multiplying input by weight
pred = neural_network(input, weight)

# Depositing the prediction
print(pred)
