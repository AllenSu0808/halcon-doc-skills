# get_support_vector_class_svm (Operator)

## Name

`get_support_vector_class_svm` — Return the index of a support vector from a trained support vector
machine.

## Signature

`def get_support_vector_class_svm(svmhandle: HHandle, index_support_vector: int) -> float`

## Description

The operator `get_support_vector_class_svm` maps a support
vector of a trained SVM (given in *`svmhandle`*) to the
original training data set. The index of the SV is specified with
*`index_support_vector`*. The index is counted from 0, i.e.,
*`index_support_vector`* must be a number between 0 and
`num_support_vectors` - 1, where
`num_support_vectors` can be determined with
[`get_support_vector_num_class_svm`](get_support_vector_num_class_svm.md). The index of this SV in
the training data is returned in *`index`*. This
*`index`* can be used for a query with
[`get_sample_class_svm`](get_sample_class_svm.md) to obtain the feature vectors that
become support vectors. [`get_sample_class_svm`](get_sample_class_svm.md) can, for
example, be used to visualize the support vectors.

Note that when using [`train_class_svm`](train_class_svm.md) with a mode different from
*"default"* or reducing the SVM with [`reduce_class_svm`](reduce_class_svm.md), the
returned *`index`* will always be *-1*, i.e., it will be invalid.
The reason for this is that a consistent mapping between SV and
training data becomes impossible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`svmhandle`** (input_control)  class_svm `→` HHandle

SVM handle.

**`index_support_vector`** (input_control)  integer `→` int

Index of the stored support vector.

**`index`** (output_control)  real `→` float

Index of the support vector in the training set.

## Result

If the parameters are valid the operator [`get_sample_class_svm`](get_sample_class_svm.md)
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_class_svm`,
`get_support_vector_num_class_svm`

## Possible Successors

`get_sample_class_svm`

## See also

`create_class_svm`

## Module

Foundation
