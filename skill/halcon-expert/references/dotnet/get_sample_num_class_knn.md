# GetSampleNumClassKnn (Operator)

## Name

`GetSampleNumClassKnn` — Return the number of training samples stored in the training data of
a k-nearest neighbors (k-NN) classifier.

## Signature

`static void HOperatorSet.GetSampleNumClassKnn(HTuple KNNHandle, out HTuple numSamples)`

`int HClassKnn.GetSampleNumClassKnn()`

## Description

`GetSampleNumClassKnn` returns in *`numSamples`* the
number of training samples that are stored in the k-nearest neighbors
(k-NN) classifier given by *`KNNHandle`*.
`GetSampleNumClassKnn` should be called before the
individual training samples are accessed with
[`GetSampleClassKnn`](get_sample_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`numSamples`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training samples.

## Result

If *`KNNHandle`* is valid, the operator
`GetSampleNumClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassKnn`

## Possible Successors

`GetSampleClassKnn`

## See also

`CreateClassKnn`

## Module

Foundation
