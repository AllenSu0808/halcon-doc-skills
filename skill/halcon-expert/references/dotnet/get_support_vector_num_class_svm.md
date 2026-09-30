# GetSupportVectorNumClassSvm (Operator)

## Name

`GetSupportVectorNumClassSvm` — Return the number of support vectors of a support vector machine.

## Signature

`static void HOperatorSet.GetSupportVectorNumClassSvm(HTuple SVMHandle, out HTuple numSupportVectors, out HTuple numSVPerSVM)`

`int HClassSvm.GetSupportVectorNumClassSvm(out HTuple numSVPerSVM)`

## Description

`GetSupportVectorNumClassSvm` returns in
*`numSupportVectors`* the number of support vectors that are
stored in the support vector machine (SVM) given by
*`SVMHandle`*. `GetSupportVectorNumClassSvm` should
be called before the labels of individual support vectors are read
out with [`GetSupportVectorClassSvm`](get_support_vector_class_svm.md), e.g., for visualizing
which the training data become a SV (see
[`GetSupportVectorClassSvm`](get_support_vector_class_svm.md)). The number of SVs in each
classifier is listed in *`numSVPerSVM`*. The reason that its
sum differs from the Number obtained in *`numSupportVectors`*
is that SV evaluations are reused throughout different
sub-classifiers. *`numSVPerSVM`* provides the possibility for
controlling the process of speeding up SVM classification time with
the operator [`ReduceClassSvm`](reduce_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`numSupportVectors`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Total number of support vectors.

**`numSVPerSVM`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of SV of each sub-SVM.

## Result

If *`SVMHandle`* is valid the operator
[`GetSampleNumClassSvm`](get_sample_num_class_svm.md) returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassSvm`

## Possible Successors

`GetSampleClassSvm`

## See also

`CreateClassSvm`

## Module

Foundation
