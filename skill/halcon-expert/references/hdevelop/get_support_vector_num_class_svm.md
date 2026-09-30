# get_support_vector_num_class_svm (Operator)

## Name

`get_support_vector_num_class_svm` — Return the number of support vectors of a support vector machine.

## Signature

`get_support_vector_num_class_svm( : : SVMHandle : NumSupportVectors, NumSVPerSVM)`

## Description

`get_support_vector_num_class_svm` returns in
*`NumSupportVectors`* the number of support vectors that are
stored in the support vector machine (SVM) given by
*`SVMHandle`*. `get_support_vector_num_class_svm` should
be called before the labels of individual support vectors are read
out with [`get_support_vector_class_svm`](get_support_vector_class_svm.md), e.g., for visualizing
which the training data become a SV (see
[`get_support_vector_class_svm`](get_support_vector_class_svm.md)). The number of SVs in each
classifier is listed in *`NumSVPerSVM`*. The reason that its
sum differs from the Number obtained in *`NumSupportVectors`*
is that SV evaluations are reused throughout different
sub-classifiers. *`NumSVPerSVM`* provides the possibility for
controlling the process of speeding up SVM classification time with
the operator [`reduce_class_svm`](reduce_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`NumSupportVectors`** (output_control)  integer `→`  (integer)

Total number of support vectors.

**`NumSVPerSVM`** (output_control)  integer-array `→`  (integer)

Number of SV of each sub-SVM.

## Result

If *`SVMHandle`* is valid the operator
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
