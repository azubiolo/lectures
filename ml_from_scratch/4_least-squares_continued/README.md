# Lecture 4: Ordinary Least Squares implementation -- Part 2

During Lecture 3, we saw a basic implementation of the ordinary least squares algorithm (OLS). The goal of lecture 4 is to go deeper into the analysis and understanding of this algorithm, in particular, we will:
- Finsh what hasn't been finished last time.
- Have an implementation of the stochastic gradient descent algorithm and compare it to the batch gradient descent algorithm.
- Plot levelsets of the loss function and see what the optimization algorithms do.
- See how the loss evolves over iterations, talk about convergence and define ways to stop the algorithm when convergence is reached.
- Mention outliers: What they are, what impact they might have on the result and how to address this issue.
- Define more sophisticated models (polynomial kernel) in case of non linearity
This folder contains two Jupyter notebooks:
- [`least-squares.ipynb`](least-squares.ipynb) which contains the solution to all the questions and exercises.