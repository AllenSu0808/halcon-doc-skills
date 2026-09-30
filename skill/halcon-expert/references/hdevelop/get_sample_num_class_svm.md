# get_sample_num_class_svm (Operator)

## Name

`get_sample_num_class_svm` — Return the number of training samples stored in the training data of
a support vector machine.

## Signature

`get_sample_num_class_svm( : : SVMHandle : NumSamples)`

## Description

`get_sample_num_class_svm` returns in *`NumSamples`* the
number of training samples that are stored in the support vector
machine (SVM) given by *`SVMHandle`*.
`get_sample_num_class_svm` should be called before the
individual training samples are accessed with
[`get_sample_class_svm`](get_sample_class_svm.md), e.g., for the purpose of reclassifying
the training data (see [`get_sample_class_svm`](get_sample_class_svm.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`NumSamples`** (output_control)  integer `→`  (integer)

Number of stored training samples.

## Result

If *`SVMHandle`* is valid the operator
`get_sample_num_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`add_sample_class_svm`,
`read_samples_class_svm`

## Possible Successors

`get_sample_class_svm`

## See also

`create_class_svm`

## Module

Foundation
