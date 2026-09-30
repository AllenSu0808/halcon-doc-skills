# add_sample_class_train_data (Operator)

## Name

`add_sample_class_train_data` — Add a training sample to training data.

## Signature

`add_sample_class_train_data( : : ClassTrainDataHandle, Order, Features, ClassID : )`

## Description

`add_sample_class_train_data` adds a training sample to the
training data given by *`ClassTrainDataHandle`*. The
training sample is given by *`Features`* and *`ClassID`*.
*`Features`* is the feature vector of the sample, and
consequently must be a real vector of length `NumDim`, as
specified in [`create_class_train_data`](create_class_train_data.md). *`ClassID`* is the
class of the sample. More than one training sample can be added at once.
In this case the parameter *`Order`* defines in which order
the elements of the feature vectors are passed in *`Features`*.
If it is set to *'row'*,
the first training sample comes first, the second comes second, and so on.
If it is set to *'column'*, the first dimension of all feature vectors
comes first, and then the second dimension of all feature vectors,
and so on. The third possible mode for *`Order`* is
*'feature_column'*. This mode expects features which were grouped
before with [`set_feature_lengths_class_train_data`](set_feature_lengths_class_train_data.md)
to come completely and row-wise before the second feature, and so on.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ClassTrainDataHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ClassTrainDataHandle`** (input_control, state is modified)  class_train_data `→`  (handle)

Handle of the training data.

**`Order`** (input_control)  string `→`  (string)

The order of the feature vector.

Default:
'row'

List of values:
'column', 'feature_column', 'row'

**`Features`** (input_control)  number-array `→`  (real)

Feature vector of the training sample.

**`ClassID`** (input_control)  integer-array `→`  (integer)

Class of the training sample.

## Result

If the parameters are valid, the operator
`add_sample_class_train_data` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_class_train_data`

## Possible Successors

`add_class_train_data_svm`,
`add_class_train_data_knn`,
`add_class_train_data_gmm`,
`add_class_train_data_mlp`

## See also

`create_class_train_data`

## Module

Foundation
