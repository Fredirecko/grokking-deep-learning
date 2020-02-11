#The author recommends that I memorize and be able to reproduce the code in this chapter. That's an interesting challenge. Not to many instructors require memorization and I find it an underutilized skill in modern society.

#Example of mean squared error-----------------------------
knob_weight = 0.5
input = 0.5
goal_pred = 0.8

pred = input * knob_weight

error = (pred - goal_pred) ** 2 #Forces the error to be positive by multiplying it by itself

print(error) #raw error

#-----------------------------------------------------------

#Hot and Cold Learning Example
weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.001

for iteration in range(1101):

    prediction = input * weight
    error = (prediction - goal_prediction) ** 2

    print("Error:" + str(error) + " Prediction:" + str(prediction))

    up_prediction = input * (weight + step_amount) #try up
    up_error = (goal_prediction - up_prediction) ** 2

    down_prediction = input * (weight - step_amount) #try down
    down_error = (goal_prediction - down_prediction) ** 2

    if(down_error < up_error):
        weight = weight - step_amount #if down is better, go down

    if(down_error > up_error):
        weight = weight + step_amount #if up is better, go up

#-----------------------------------------------------------

#Gradient Descent
weight = 0.5
goal_pred = 0.8
input = 0.5

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * input #(pred - goal_pred) = pure error and multiplying it by input scales, reverses the negative, and stopping
    weight = weight - direction_and_amount

    print("Error:" + str(error) +" Prediction:" + str(pred))

#-----------------------------------------------------------

#using delta
weight, goal_pred, input = (0.0, 0.8, 0.5)

for iteration in range(4):

    #pred = input * weight
    error = ((input * weight) - goal_pred)
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))


#-----------------------------------------------------------

#using delta over several iterations
weight, goal_pred, input = (0.0, 0.8, 1.1)

for iteration in range(4):
    print("-----\nWeight:" + str(weight))
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight = weight - weight_delta
    print("Error:" + str(error) + " Prediction:" + str(pred))
    print("Delta:" + str(delta) + " Weight Delta:" + str(weight_delta))
