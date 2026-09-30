# get_sample_num_class_svm (Operator)

## Name

`get_sample_num_class_svm` — Return the number of training samples stored in the training data of
a support vector machine.

## Signature

`def get_sample_num_class_svm(svmhandle: HHandle) -> int`

## Description

`get_sample_num_class_svm` returns in *`num_samples`* the
number of training samples that are stored in the support vector
machine (SVM) given by *`svmhandle`*.
`get_sample_num_class_svm` should be called before the
individual training samples are accessed with
[`get_sample_class_svm`](get_sample_class_svm.md), e.g., for the purpose of reclassifying
the training data (see [`get_sample_class_svm`](get_sample_class_svm.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`svmhandle`** (input_control)  class_svm `→` HHandle

SVM handle.

**`num_samples`** (output_control)  integer `→` int

Number of stored training samples.

## Result

If *`svmhandle`* is valid the operator
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
