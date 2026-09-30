# evaluate_class_svm (Operator)

## Name

`evaluate_class_svm` — Evaluate a feature vector by a support vector machine.

## Signature

`evaluate_class_svm( : : SVMHandle, Features : Result)`

## Description

`evaluate_class_svm` calculates for a feature vector
provided in *`Features`* the *`Result`* given
a SVM in *`SVMHandle`*. The operator `evaluate_class_svm`
can only be used if the SVM was created in the `Mode` =
*'novelty-detection'*. If the feature vector lies in the class, a
*`Result`* value bigger *1.0* is returned. If the feature vector
lies outside the class boundary, e.g., is an outlier, a value smaller
*1.0* is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector.

**`Result`** (output_control)  real(-array) `→`  (real)

Result of evaluating the feature vector with the SVM.

## Result

If the parameters are valid the operator `evaluate_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_svm`,
`read_class_svm`

## See also

`create_class_svm`

## Module

Foundation
