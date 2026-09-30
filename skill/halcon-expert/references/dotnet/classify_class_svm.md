# ClassifyClassSvm (Operator)

## Name

`ClassifyClassSvm` — Classify a feature vector by a support vector machine.

## Signature

`static void HOperatorSet.ClassifyClassSvm(HTuple SVMHandle, HTuple features, HTuple num, out HTuple classVal)`

`HTuple HClassSvm.ClassifyClassSvm(HTuple features, HTuple num)`

## Description

`ClassifyClassSvm` computes the best *`num`* classes of
the feature vector *`features`* with the SVM *`SVMHandle`*
and returns them in *`classVal`*. If the classifier was
created in the `mode` = *"one-versus-one"*, the
classes are ordered by the number of votes of the sub-classifiers. If
`mode` = *"one-versus-all"* was used, the classes are ordered
by the value of each sub-classifier (see [`CreateClassSvm`](create_class_svm.md) for more
details). If the classifier was created in the `mode` =
*"novelty-detection"*, it determines whether the feature vector
belongs to the same class as the training data (*`classVal`* = 1) or is
regarded as outlier (*`classVal`* = 0). In this case *`num`* must be
set to 1 as the classifier only determines membership.

Before calling `ClassifyClassSvm`, the SVM must be trained
with [`TrainClassSvm`](train_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

**`num`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classVal`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of classifying the feature vector with
the SVM.

## Result

If the parameters are valid the operator `ClassifyClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainClassSvm`,
`ReadClassSvm`

## Alternatives

`ApplyDlModel`

## See also

`CreateClassSvm`

## References

John Shawe-Taylor, Nello Cristianini: “Kernel Methods for Pattern
Analysis”; Cambridge University Press, Cambridge; 2004.
  
Bernhard Schölkopf, Alexander J.Smola: “Learning with Kernels”;
MIT Press, London; 1999.

## Module

Foundation
