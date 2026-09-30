# classify_class_svm (Operator)

## Name

`classify_class_svm` — Classify a feature vector by a support vector machine.

## Signature

`classify_class_svm( : : SVMHandle, Features, Num : Class)`

## Description

`classify_class_svm` computes the best *`Num`* classes of
the feature vector *`Features`* with the SVM *`SVMHandle`*
and returns them in *`Class`*. If the classifier was
created in the `Mode` = *'one-versus-one'*, the
classes are ordered by the number of votes of the sub-classifiers. If
`Mode` = *'one-versus-all'* was used, the classes are ordered
by the value of each sub-classifier (see [`create_class_svm`](create_class_svm.md) for more
details). If the classifier was created in the `Mode` =
*'novelty-detection'*, it determines whether the feature vector
belongs to the same class as the training data (*`Class`* = 1) or is
regarded as outlier (*`Class`* = 0). In this case *`Num`* must be
set to 1 as the classifier only determines membership.

Before calling `classify_class_svm`, the SVM must be trained
with [`train_class_svm`](train_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector.

**`Num`** (input_control)  integer-array `→`  (integer)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`Class`** (output_control)  integer(-array) `→`  (integer)

Result of classifying the feature vector with
the SVM.

## Result

If the parameters are valid the operator `classify_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_svm`,
`read_class_svm`

## Alternatives

`apply_dl_model`

## See also

`create_class_svm`

## References

John Shawe-Taylor, Nello Cristianini: “Kernel Methods for Pattern
Analysis”; Cambridge University Press, Cambridge; 2004.
  
Bernhard Schölkopf, Alexander J.Smola: “Learning with Kernels”;
MIT Press, London; 1999.

## Module

Foundation
