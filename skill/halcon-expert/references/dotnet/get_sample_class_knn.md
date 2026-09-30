# GetSampleClassKnn (Operator)

## Name

`GetSampleClassKnn` — Return a training sample from the training data of a k-nearest neighbors
(k-NN) classifier.

## Signature

`static void HOperatorSet.GetSampleClassKnn(HTuple KNNHandle, HTuple indexSample, out HTuple features, out HTuple classID)`

`HTuple HClassKnn.GetSampleClassKnn(int indexSample, out HTuple classID)`

## Description

`GetSampleClassKnn` reads a training sample from the
k-nearest neighbors (k-NN) classifier given by *`KNNHandle`* that was
added with [`AddSampleClassKnn`](add_sample_class_knn.md) or
[`ReadClassKnn`](read_class_knn.md). The index of the sample is
specified with *`indexSample`*. The index is counted from 0,
i.e., *`indexSample`* must be a number between 0 and
`numSamples` - 1, where `numSamples` can be
determined with [`GetSampleNumClassKnn`](get_sample_num_class_knn.md). The training
sample is returned in *`features`* and *`classID`*.
*`features`* is a feature vector of length
`numDim` (see [`CreateClassKnn`](create_class_knn.md)), while *`classID`*
is the class label, which is a number between 0 and the
number of classes.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`indexSample`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the training sample.

**`features`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample.

**`classID`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Class of the training sample.

## Result

If the parameters are valid the operator
`GetSampleClassKnn` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`AddSampleClassTrainData`

## See also

`CreateClassKnn`

## Module

Foundation
