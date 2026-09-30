# classify_class_gmm (Operator)

## Name

`classify_class_gmm` — Calculate the class of a feature vector by a Gaussian Mixture
Model.

## Signature

`classify_class_gmm( : : GMMHandle, Features, Num : ClassID, ClassProb, Density, KSigmaProb)`

## Description

`classify_class_gmm` computes the best *`Num`* classes of
the feature vector *`Features`* with the Gaussian Mixture Model
(GMM) *`GMMHandle`* and returns the classes in *`ClassID`*
and the corresponding probabilities of the classes in
*`ClassProb`*. Before calling `classify_class_gmm`, the
GMM must be trained with [`train_class_gmm`](train_class_gmm.md).

`classify_class_gmm` corresponds to a call to
[`evaluate_class_gmm`](evaluate_class_gmm.md) and an additional step that extracts the
best *`Num`* classes. As described with
[`evaluate_class_gmm`](evaluate_class_gmm.md), the output values of the GMM can be
interpreted as probabilities of the occurrence of the respective
classes. However, here the posterior probability *`ClassProb`*
is further normalized as *`ClassProb`* = p(i|x)/p(x)
, where p(i|x)
and p(x) are specified with [`evaluate_class_gmm`](evaluate_class_gmm.md).
In most cases it should be sufficient to use *`Num`* =
*1* in order to decide whether the
probability of the best class is high enough. In some applications
it may be interesting to also take the second best class into
account (*`Num`* = *2*), particularly if it can be
expected that the classes show a significant degree of overlap.

*`Density`* and *`KSigmaProb`* are explained with
[`evaluate_class_gmm`](evaluate_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→`  (handle)

GMM handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector.

**`Num`** (input_control)  integer `→`  (integer)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`ClassID`** (output_control)  integer(-array) `→`  (integer)

Result of classifying the feature vector with
the GMM.

**`ClassProb`** (output_control)  real-array `→`  (real)

A-posteriori probability of the classes.

**`Density`** (output_control)  real-array `→`  (real)

Probability density of the feature vector.

**`KSigmaProb`** (output_control)  real-array `→`  (real)

Normalized k-sigma-probability for the feature
vector.

## Result

If the parameters are valid, the operator `classify_class_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`train_class_gmm`,
`read_class_gmm`

## Alternatives

`evaluate_class_gmm`

## See also

`create_class_gmm`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Mario A.T. Figueiredo: “Unsupervised Learning of Finite Mixture
Models”; IEEE Transactions on Pattern Analysis and Machine
Intelligence, Vol. 24, No. 3; March 2002.

## Module

Foundation
