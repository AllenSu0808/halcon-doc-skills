# AddSampleClassTrainData (Operator)

## Name

`AddSampleClassTrainData` — Add a training sample to training data.

## Signature

`static void HOperatorSet.AddSampleClassTrainData(HTuple classTrainDataHandle, HTuple order, HTuple features, HTuple classID)`

`void HClassTrainData.AddSampleClassTrainData(string order, HTuple features, HTuple classID)`

## Description

`AddSampleClassTrainData` adds a training sample to the
training data given by *`classTrainDataHandle`*. The
training sample is given by *`features`* and *`classID`*.
*`features`* is the feature vector of the sample, and
consequently must be a real vector of length `numDim`, as
specified in [`CreateClassTrainData`](create_class_train_data.md). *`classID`* is the
class of the sample. More than one training sample can be added at once.
In this case the parameter *`order`* defines in which order
the elements of the feature vectors are passed in *`features`*.
If it is set to *"row"*,
the first training sample comes first, the second comes second, and so on.
If it is set to *"column"*, the first dimension of all feature vectors
comes first, and then the second dimension of all feature vectors,
and so on. The third possible mode for *`order`* is
*"feature_column"*. This mode expects features which were grouped
before with [`SetFeatureLengthsClassTrainData`](set_feature_lengths_class_train_data.md)
to come completely and row-wise before the second feature, and so on.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- classTrainDataHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`classTrainDataHandle`** (input_control, state is modified)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data.

**`order`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The order of the feature vector.

Default:
"row"

List of values:
"column", "feature_column", "row"

**`features`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample.

**`classID`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Class of the training sample.

## Result

If the parameters are valid, the operator
`AddSampleClassTrainData` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateClassTrainData`

## Possible Successors

`AddClassTrainDataSvm`,
`AddClassTrainDataKnn`,
`AddClassTrainDataGmm`,
`AddClassTrainDataMlp`

## See also

`CreateClassTrainData`

## Module

Foundation
