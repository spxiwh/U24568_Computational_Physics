# Lecture 10b: Significance

In 10a we looked at using repeated draws of a probability distibruion to find the value of something and to quantify uncertainty. 

Here we will use those same techniques to find the significance of a signal when it is burried in noisy data.

Previously, we've cross-correlated data with a known signal shape. We observe spikes in the cross-correlation function, which seem to indicate the presence of a signal in the noisy data. But how can we be sure that this wasn't just some particularly unlucky noise? In reality, we never can be. We can only ask: how unlikely would it have been to see something like this in noise alone.

So let's try to quantify that. We'll create a dataset with our `signal_2` added to it, but the noise will be louder than the data we used previously.

```{tableofcontents}
```

