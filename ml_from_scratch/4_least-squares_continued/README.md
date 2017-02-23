# Lecture 4: Ordinary Least Squares -- Part 2

During [Lecture 3](../3_least-squares), we saw a basic implementation of the ordinary least squares algorithm (OLS). The goal of lecture 4 is to go deeper into the analysis and understanding of this algorithm, in particular, we will:
- Finsh what hasn't been finished last time.
- Have an implementation of the stochastic gradient descent algorithm and compare it to the batch gradient descent algorithm.
- Plot levelsets of the loss function and see what the optimization algorithms do.
- See how the loss evolves over iterations, talk about convergence and define ways to stop the algorithm when convergence is reached.
Homework for the next session are:
- Normalize the feature corresponding to the size of the house, and see the impact on the loss function.
- Add an outlier to the training set, see what impact it has on the result and think of a way to address this issue.

This folder contains two Jupyter notebooks:
- [`least-squares_empty.ipynb`](least-squares_empty.ipynb) that will guide you though the implementation of the OLS algorithm.
- [`least-squares.ipynb`](least-squares.ipynb) which contains the solution to all the questions and exercises.