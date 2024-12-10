# Lecture 11a: Markov Chain Monte Carlo

So we can now do MC simulations. We understand this really just means simulate many times. So what is MCMC and how is it different?

## Markov Chains

A Markov chain is a sequence of random variables where the probability of each variable depends only on the state of the previous variable. This is called the Markov property.

A Markov chain is defined by a set of states and a transition matrix. The transition matrix gives the probability of moving from one state to another. The probability of moving from state $i$ to state $j$ is given by the element $P_{ij}$ of the transition matrix.

The transition matrix is a square matrix with rows that sum to 1. The matrix is usually denoted by $P$.

## Markov Chain Monte Carlo

MCMC is a method for sampling from a probability distribution. The idea is to construct a Markov chain that has the desired distribution as its stationary distribution. This means that if we run the chain for long enough, the distribution of the states will converge to the desired distribution.

The Metropolis-Hastings algorithm is a popular MCMC algorithm. It works by proposing a new state and then accepting or rejecting the new state based on the ratio of the probabilities of the new state and the current state.

Let's explore this through examples in the notebooks below.


```{tableofcontents}
```

