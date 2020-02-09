
def elementwise_multiplication(vec_a, vec_b):

    assert(len(vec_a) == len(vec_b))
    output = []
    for i in range(len(vec_a)):
        output.append(vec_a[i] * vec_b[i])
    print(output)



def elementwise_addition(vec_a, vec_b):

    assert(len(vec_a) == len(vec_b))
    output = []
    for i in range(len(vec_a)):
        output.append(vec_a[i] + vec_b[i])
    print(output)












ls1 = [9,2]
ls2 = [2,3]

print(elementwise_addition(ls1, ls2))
print(elementwise_multiplication(ls1, ls2))
