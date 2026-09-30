# get_support_vector_num_class_svm (Operator)

## Name

`get_support_vector_num_class_svm` — Return the number of support vectors of a support vector machine.

## Signature

`def get_support_vector_num_class_svm(svmhandle: HHandle) -> Tuple[int, Sequence[int]]`

## Description

`get_support_vector_num_class_svm` returns in
*`num_support_vectors`* the number of support vectors that are
stored in the support vector machine (SVM) given by
*`svmhandle`*. `get_support_vector_num_class_svm` should
be called before the labels of individual support vectors are read
out with [`get_support_vector_class_svm`](get_support_vector_class_svm.md), e.g., for visualizing
which the training data become a SV (see
[`get_support_vector_class_svm`](get_support_vector_class_svm.md)). The number of SVs in each
classifier is listed in *`num_svper_svm`*. The reason that its
sum differs from the Number obtained in *`num_support_vectors`*
is that SV evaluations are reused throughout different
sub-classifiers. *`num_svper_svm`* provides the possibility for
controlling the process of speeding up SVM classification time with
the operator [`reduce_class_svm`](reduce_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`svmhandle`** (input_control)  class_svm `→` HHandle

SVM handle.

**`num_support_vectors`** (output_control)  integer `→` int

Total number of support vectors.

**`num_svper_svm`** (output_control)  integer-array `→` Sequence[int]

Number of SV of each sub-SVM.

## Result

If *`svmhandle`* is valid the operator
[`get_sample_num_class_svm`](get_sample_num_class_svm.md) returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_svm`

## Possible Successors

`get_sample_class_svm`

## See also

`create_class_svm`

## Module

Foundation
