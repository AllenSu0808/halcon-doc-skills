# EvaluateClassGmm (Operator)

## Name

`EvaluateClassGmm` — Evaluate a feature vector by a Gaussian Mixture Model.

## Signature

`static void HOperatorSet.EvaluateClassGmm(HTuple GMMHandle, HTuple features, out HTuple classProb, out HTuple density, out HTuple KSigmaProb)`

`HTuple HClassGmm.EvaluateClassGmm(HTuple features, out double density, out double KSigmaProb)`

## Description

`EvaluateClassGmm` computes three different probability
values for a feature vector *`features`* with the Gaussian
Mixture Model (GMM) *`GMMHandle`*.

The a-posteriori probability of class `i` for the sample
*`features`*(x) is computed as
$$p(i|x) = \sum_{j=1}^{ncomp} P(j)p(x|j)$$ ![figure](../assets/99c20e7618b5e945.svg)
and returned for each class in *`classProb`*. The formulas for
the calculation of the center density function p(x|j) are described with [`CreateClassGmm`](create_class_gmm.md).

The probability density of the feature vector is computed as a sum of
the posterior class probabilities
$$p(x) = \sum_{i=1}^{n_{classes}} P_r(i) p(i|x)$$ ![figure](../assets/8d26ae34b9ff0021.svg)
and is returned in *`density`*. Here, Pr(i) are
the prior classes probabilities as computed by
[`TrainClassGmm`](train_class_gmm.md). *`density`* can be used for novelty
detection, i.e., to reject feature vectors that do not belong to any
of the trained classes. However, since *`density`* depends on
the scaling of the feature vectors and since *`density`* is a
probability density, and consequently does not need to lie between 0
and 1, the novelty detection can typically be performed more easily
with *`KSigmaProb`* (see below).

A *k-sigma error ellipsoid* is defined as a locus of points
for which
$$(\mathbf{x}-\mu)^{T}C^{-1}(\mathbf{x}-\mu)=k^{2}$$
In the one dimensional case this is the interval $[\mu-k\sigma,\mu+k\sigma]$. For any 1D Gaussian
distribution, it is true that approximately 68% of the
occurrences of the random variable are within this range for k=1,
approximately 95% for k=2, approximately 99%
for k=3, etc.
This probability is called k-sigma probability and is denoted by P[k].
P[k] can be computed numerically for univariate as well as for
multivariate Gaussian distributions, where it should be noted that
for the same values of k,
$P^{(N)}[k]>P^{(N+1)}[k]$
(here N and (N+1) denote dimensions). For Gaussian
mixture models the k-sigma probability is computed as:
$$P_{GMM}[x] = \sum_{j=1}^{n_{comp}} P(j) P_j[k_j] %$$ ![figure](../assets/0a00f10b4c779431.svg)
where
$$k_{j}^{2}=(\mathbf{x}-\mu_{j})^{T}C_{j}^{-1}(\mathbf{x}-\mu_{j})$$.
$P_{GMM}[k]$ are weighted with the class priors and then
normalized.
The maximum value of all classes is returned in *`KSigmaProb`*, such
that
$$KSigmaProb = \frac{1}{P_{max}} \max\left( P_r(i) P_{GMM}[\mathbf{x}] \right)$$ ![figure](../assets/2685a4abd7f7dde4.svg)

*`KSigmaProb`* can be used for novelty detection, as it indicates how
well a feature vector fits into the distribution of the class it is assigned
to. Typically, feature vectors having values below 0.0001 should be rejected.
Note that the rejection threshold defined by the parameter
`rejectionThreshold` in [`ClassifyImageClassGmm`](classify_image_class_gmm.md)
refers to the *`KSigmaProb`* values.

Before calling `EvaluateClassGmm`, the GMM must be trained
with [`TrainClassGmm`](train_class_gmm.md).

The position of the maximum value of *`classProb`* is usually
interpreted as the class of the feature vector and the corresponding
value as the probability of the class. In this case,
[`ClassifyClassGmm`](classify_class_gmm.md) should be used instead of
`EvaluateClassGmm`, because [`ClassifyClassGmm`](classify_class_gmm.md)
directly returns the class and corresponding probability.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

**`classProb`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

A-posteriori probability of the classes.

**`density`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Probability density of the feature vector.

**`KSigmaProb`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Normalized k-sigma-probability for the feature
vector.

## Result

If the parameters are valid, the operator `EvaluateClassGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`TrainClassGmm`,
`ReadClassGmm`

## Alternatives

`ClassifyClassGmm`

## See also

`CreateClassGmm`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Mario A.T. Figueiredo: “Unsupervised Learning of Finite Mixture
Models”; IEEE Transactions on Pattern Analysis and Machine
Intelligence, Vol. 24, No. 3; March 2002.

## Module

Foundation
