

# Performing a weighted sum of inputs

def w_sum(a,b):
    assert(len(a) == len(b))
    output = 0

    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

# Inserting one input datapoint

#datapoints below represent first four games of season
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9] #percent
nfans = [1.2, 1.3, 0.5, 1.0] #in millions

input = [toes[0], wlrec[0], nfans[0]] #input corresponds to every entry for the first game of the season


# Empty network with multiple inputs

weights = [0.1, 0.2, 0]

def neural_network(input, weights):
    pred = w_sum(input, weights)
    return pred

pred = neural_network(input, weights)

print(pred)
