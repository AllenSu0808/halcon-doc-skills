# GetSupportVectorClassSvm (Operator)

## Name

`GetSupportVectorClassSvm` — Return the index of a support vector from a trained support vector
machine.

## Signature

`static void HOperatorSet.GetSupportVectorClassSvm(HTuple SVMHandle, HTuple indexSupportVector, out HTuple index)`

`double HClassSvm.GetSupportVectorClassSvm(int indexSupportVector)`

## Description

The operator `GetSupportVectorClassSvm` maps a support
vector of a trained SVM (given in *`SVMHandle`*) to the
original training data set. The index of the SV is specified with
*`indexSupportVector`*. The index is counted from 0, i.e.,
*`indexSupportVector`* must be a number between 0 and
`numSupportVectors` - 1, where
`numSupportVectors` can be determined with
[`GetSupportVectorNumClassSvm`](get_support_vector_num_class_svm.md). The index of this SV in
the training data is returned in *`index`*. This
*`index`* can be used for a query with
[`GetSampleClassSvm`](get_sample_class_svm.md) to obtain the feature vectors that
become support vectors. [`GetSampleClassSvm`](get_sample_class_svm.md) can, for
example, be used to visualize the support vectors.

Note that when using [`TrainClassSvm`](train_class_svm.md) with a mode different from
*"default"* or reducing the SVM with [`ReduceClassSvm`](reduce_class_svm.md), the
returned *`index`* will always be *-1*, i.e., it will be invalid.
The reason for this is that a consistent mapping between SV and
training data becomes impossible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`indexSupportVector`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the stored support vector.

**`index`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Index of the support vector in the training set.

## Result

If the parameters are valid the operator [`GetSampleClassSvm`](get_sample_class_svm.md)
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`TrainClassSvm`,
`GetSupportVectorNumClassSvm`

## Possible Successors

`GetSampleClassSvm`

## See also

`CreateClassSvm`

## Module

Foundation
