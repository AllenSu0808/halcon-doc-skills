# GetSampleNumClassSvm (Operator)

## Name

`GetSampleNumClassSvm` — Return the number of training samples stored in the training data of
a support vector machine.

## Signature

`static void HOperatorSet.GetSampleNumClassSvm(HTuple SVMHandle, out HTuple numSamples)`

`int HClassSvm.GetSampleNumClassSvm()`

## Description

`GetSampleNumClassSvm` returns in *`numSamples`* the
number of training samples that are stored in the support vector
machine (SVM) given by *`SVMHandle`*.
`GetSampleNumClassSvm` should be called before the
individual training samples are accessed with
[`GetSampleClassSvm`](get_sample_class_svm.md), e.g., for the purpose of reclassifying
the training data (see [`GetSampleClassSvm`](get_sample_class_svm.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`numSamples`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training samples.

## Result

If *`SVMHandle`* is valid the operator
`GetSampleNumClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassSvm`,
`ReadSamplesClassSvm`

## Possible Successors

`GetSampleClassSvm`

## See also

`CreateClassSvm`

## Module

Foundation
