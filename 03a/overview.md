# Lecture 3a - Statistics II

This is the second of a two-part series introducing statistics in Python. 

In this notebook we will use the distributions we learned about in notebook 2b to gnerate mock data and we'll go further and fit an analytical solution to that data. 

Additionally we'll introduce Monte Carlo methods and use them to calculate the value of pi.

## From stats I you should be familiar with:

1. Generating 'random' data from an analytical distibution using both `numpy.random` and `scipy.stats` packages
2. Finding 'summary statistics' such as 'moments' of a distribution of data using for example
    * `np.mean`
    * `np.std`
    * `scipy.stats.kurtosis`
    * `scipy.stats.skew`
3. Generating a model distribution using scipy.stats.pdf (a probability density function) - for example this is a function that our random data could be drawn from
4. Understanding that we could compare 'summary statistics' or 'moments' of a distribution to give us an idea as to whether our data is adequately represented by that distribution.
5. Plotting using `matplotlib.hist`
6. Additionally you should be familiar with reading help pages and finding useful information on them, e.g. 'inputs', 'outputs', 'functions' within a 'class', and examples on how to use that function/class. 

## If you are not familiar with anything above please ask for a brief explanation in class!


## Learning objectives for today:

Today we will be using random-ness to solve problems.
1. Using `numpy.histogram` to save histogram data to an array
2. Use a PDF (probability density function) to draw random data 
    * creating mock data is a useful tool to test out a scientific hypothesis
3. Fit a model to this random data
4. Use multiple random draws to estimate the value of $\pi$.
    * using multiple draws in this way is called 'monte-carlo' - it is a very useful technique in many situations including fitting data and finding uncertainties on results - we WILL come back to this later in term so become familiar with it now!
5. Understanding what 'noise' is


## Weekly tasks

```{tableofcontents}
```

