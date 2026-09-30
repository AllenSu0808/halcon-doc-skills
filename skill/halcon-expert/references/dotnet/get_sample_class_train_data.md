# GetSampleClassTrainData (Operator)

## Name

`GetSampleClassTrainData` — Return a training sample from training data.

## Signature

`static void HOperatorSet.GetSampleClassTrainData(HTuple classTrainDataHandle, HTuple indexSample, out HTuple features, out HTuple classID)`

`HTuple HClassTrainData.GetSampleClassTrainData(int indexSample, out int classID)`

## Description

`GetSampleClassTrainData` reads a training sample from the
training data given by *`classTrainDataHandle`* that was
added, e.g., with [`AddSampleClassTrainData`](add_sample_class_train_data.md).
The index of the sample is
specified with *`indexSample`*. The index is counted from 0.
That means that *`indexSample`* must be a number between 0 and
`numSamples` - 1, where `numSamples` can be
determined with [`GetSampleNumClassTrainData`](get_sample_num_class_train_data.md). The training
sample is returned in *`features`* and *`classID`*.
*`features`* is a feature vector of length `numDim`
(see [`CreateClassTrainData`](create_class_train_data.md)) and *`classID`* is
the class of the feature vector.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of training data for a classifier.

**`indexSample`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training sample.

**`features`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample.

**`classID`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Class of the training sample.

## Result

If the parameters are valid, the operator
[`GetSampleClassMlp`](get_sample_class_mlp.md) returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`AddSampleClassTrainData`

## See also

`CreateClassTrainData`

## Module

Foundation
