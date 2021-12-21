# kmeans-noise
Expirements on how attribute noise affects K-Means clustering

This repo examines the effect of attribute noise when clustering with K-Means,
compared to other algorithms. The performance of the algorithms is tested under three cases: unnormalized features,
features with added gaussian noise and dataset containing random, uniformly distributed points. We conclude that K-Means is more sensitive than other density-based algorithms, in the presence of such noise.

You may find the full paper discussing the results in pdf form.

The experiments are available to run in Jupiter notebook (paper.ipynb)
