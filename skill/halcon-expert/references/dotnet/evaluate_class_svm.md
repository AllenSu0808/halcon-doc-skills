# EvaluateClassSvm (Operator)

## Name

`EvaluateClassSvm` — Evaluate a feature vector by a support vector machine.

## Signature

`static void HOperatorSet.EvaluateClassSvm(HTuple SVMHandle, HTuple features, out HTuple result)`

`HTuple HClassSvm.EvaluateClassSvm(HTuple features)`

## Description

`EvaluateClassSvm` calculates for a feature vector
provided in *`features`* the *`result`* given
a SVM in *`SVMHandle`*. The operator `EvaluateClassSvm`
can only be used if the SVM was created in the `mode` =
*"novelty-detection"*. If the feature vector lies in the class, a
*`result`* value bigger *1.0* is returned. If the feature vector
lies outside the class boundary, e.g., is an outlier, a value smaller
*1.0* is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

**`result`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Result of evaluating the feature vector with the SVM.

## Result

If the parameters are valid the operator `EvaluateClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainClassSvm`,
`ReadClassSvm`

## See also

`CreateClassSvm`

## Module

Foundation
