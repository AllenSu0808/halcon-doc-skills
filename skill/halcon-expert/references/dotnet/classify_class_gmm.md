# ClassifyClassGmm (Operator)

## Name

`ClassifyClassGmm` — Calculate the class of a feature vector by a Gaussian Mixture
Model.

## Signature

`static void HOperatorSet.ClassifyClassGmm(HTuple GMMHandle, HTuple features, HTuple num, out HTuple classID, out HTuple classProb, out HTuple density, out HTuple KSigmaProb)`

`HTuple HClassGmm.ClassifyClassGmm(HTuple features, int num, out HTuple classProb, out HTuple density, out HTuple KSigmaProb)`

## Description

`ClassifyClassGmm` computes the best *`num`* classes of
the feature vector *`features`* with the Gaussian Mixture Model
(GMM) *`GMMHandle`* and returns the classes in *`classID`*
and the corresponding probabilities of the classes in
*`classProb`*. Before calling `ClassifyClassGmm`, the
GMM must be trained with [`TrainClassGmm`](train_class_gmm.md).

`ClassifyClassGmm` corresponds to a call to
[`EvaluateClassGmm`](evaluate_class_gmm.md) and an additional step that extracts the
best *`num`* classes. As described with
[`EvaluateClassGmm`](evaluate_class_gmm.md), the output values of the GMM can be
interpreted as probabilities of the occurrence of the respective
classes. However, here the posterior probability *`classProb`*
is further normalized as *`classProb`* = p(i|x)/p(x)
, where p(i|x)
and p(x) are specified with [`EvaluateClassGmm`](evaluate_class_gmm.md).
In most cases it should be sufficient to use *`num`* =
*1* in order to decide whether the
probability of the best class is high enough. In some applications
it may be interesting to also take the second best class into
account (*`num`* = *2*), particularly if it can be
expected that the classes show a significant degree of overlap.

*`density`* and *`KSigmaProb`* are explained with
[`EvaluateClassGmm`](evaluate_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

**`num`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classID`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of classifying the feature vector with
the GMM.

**`classProb`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

A-posteriori probability of the classes.

**`density`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Probability density of the feature vector.

**`KSigmaProb`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Normalized k-sigma-probability for the feature
vector.

## Result

If the parameters are valid, the operator `ClassifyClassGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`TrainClassGmm`,
`ReadClassGmm`

## Alternatives

`EvaluateClassGmm`

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
