# classify_class_gmm (Operator)

## Name

`classify_class_gmm` — Calculate the class of a feature vector by a Gaussian Mixture
Model.

## Signature

`def classify_class_gmm(gmmhandle: HHandle, features: Sequence[float], num: int) -> Tuple[Sequence[int], Sequence[float], Sequence[float], Sequence[float]]`

`def classify_class_gmm_s(gmmhandle: HHandle, features: Sequence[float], num: int) -> Tuple[int, Sequence[float], Sequence[float], Sequence[float]]`

## Description

`classify_class_gmm` computes the best *`num`* classes of
the feature vector *`features`* with the Gaussian Mixture Model
(GMM) *`gmmhandle`* and returns the classes in *`class_id`*
and the corresponding probabilities of the classes in
*`class_prob`*. Before calling `classify_class_gmm`, the
GMM must be trained with [`train_class_gmm`](train_class_gmm.md).

`classify_class_gmm` corresponds to a call to
[`evaluate_class_gmm`](evaluate_class_gmm.md) and an additional step that extracts the
best *`num`* classes. As described with
[`evaluate_class_gmm`](evaluate_class_gmm.md), the output values of the GMM can be
interpreted as probabilities of the occurrence of the respective
classes. However, here the posterior probability *`class_prob`*
is further normalized as *`class_prob`* = p(i|x)/p(x)
, where p(i|x)
and p(x) are specified with [`evaluate_class_gmm`](evaluate_class_gmm.md).
In most cases it should be sufficient to use *`num`* =
*1* in order to decide whether the
probability of the best class is high enough. In some applications
it may be interesting to also take the second best class into
account (*`num`* = *2*), particularly if it can be
expected that the classes show a significant degree of overlap.

*`density`* and *`ksigma_prob`* are explained with
[`evaluate_class_gmm`](evaluate_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gmmhandle`** (input_control)  class_gmm `→` HHandle

GMM handle.

**`features`** (input_control)  real-array `→` Sequence[float]

Feature vector.

**`num`** (input_control)  integer `→` int

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`class_id`** (output_control)  integer(-array) `→` Sequence[int]

Result of classifying the feature vector with
the GMM.

**`class_prob`** (output_control)  real-array `→` Sequence[float]

A-posteriori probability of the classes.

**`density`** (output_control)  real-array `→` Sequence[float]

Probability density of the feature vector.

**`ksigma_prob`** (output_control)  real-array `→` Sequence[float]

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
