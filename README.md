# Grokking Deep Learning by Andrew W. Trask

## Note - Project Status
This is a personal project. I am reading through the Grokking Deep Learning book by Andrew W. Trask. 

## Description
This repository is set-up as a general place to store my progress as I move through Andrew Trask's Grokking Deep Learning book. 

## Chapter 3 - Introduction to Neural Prediction: Forward Propagation
This chapter is the first chapter in the book to be project based. Objectives included explaining what a simple neural network does/is, creating simple networks, and making predictions with single input/outputs and multiple input/outputs.

Data->Machine->Prediction

Datapoint->Weight->Prediction

Input->Weight->Output

"The interface for a neural network is simple. It accepts an input variable as information and a weight variable as knowledge and outputs a prediction.  Every neural network you'll ever see works this way." - pg. 26

Elementwise addition sums two vectors. Elementwise multiplication multiplies two vectors. A vector is a list of numbers. For examples weights = [0.1, 0.2, 0] and input = [toes[0], wlrec[0], nfans[0]]. In our example you can take two vectors of equal length and multiply them together based on position and the sum the result to get the dot product.

## Chapter 4 - Gradient Descent

Predict -> Compare -> Learn

One of the most important steps in learning how well your prediction is coming up with a good way to evaluate error.

In deep learning one of the ways to measure error is: mean squared error.  (error is always positive)

Once you have a way of evaluating error the next step, Learn, uses the error evaluation to adjust the weights accordingly. Gradient descent is a popular means of "learning"/adjust the weights.  Gradient descent produces a number that is applied to the weight and tells the weight how much higher or lower it should be thus reducing the error. 

Mean squared error does inflate big errors and reduces small errors but this can be used to enhance learning.

Hot and cold learning means moving the the weights in both directions and seeing which direction reduces the error. You repeat until you get error == 0. One problem with hot/cold learning is it requires multiple predictions to make a single weight update.  The second problem is that the step amount is arbitrary which means you may never reach the correct weight value.

"Alpha reduces the weight so it doesn't overshoot." 

"Derivatives are the sensitivity between two variables." 

"It's the relationship between two variables in a function so you can know how much one changes when you change the other."











