# add_sample_class_knn (Operator)

## Name

`add_sample_class_knn` — Add a sample to a k-nearest neighbors (k-NN) classifier.

## Signature

`def add_sample_class_knn(knnhandle: HHandle, features: MaybeSequence[float], class_id: MaybeSequence[int]) -> None`

## Description

`add_sample_class_knn` adds a feature vector to a k-nearest neighbors
(k-NN) data structure. The length of a feature vector was
specified in [`create_class_knn`](create_class_knn.md) by `num_dim`.
A handle to a k-NN data structure has to be specified in *`knnhandle`*.

The feature vectors are collected in *`features`*. The length of the
input vector must be a multiple of `num_dim`.
Each feature vector needs a class which can be given by *`class_id`*,
if only one was specified, the class is used for all vectors. The class is a
natural number greater or equal to 0. If only one class is used, the
class has to be 0. In case the operator
[`classify_image_class_knn`](classify_image_class_knn.md) will be used, all numbers starting from
0 to the number of classes-1 should be used, since otherwise an empty
region will be generated for each unused number.

It is allowed to add samples to an already trained k-NN classificator.
The new data is only integrated after another call to
[`train_class_knn`](train_class_knn.md).

If the k-NN classifier has been trained with automatic feature normalization
enabled, the supplied features *`features`* are interpreted as
unnormalized and are normalized as it was defined by the last call to
[`train_class_knn`](train_class_knn.md). Please see [`train_class_knn`](train_class_knn.md) for more
information on normalization.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- knnhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`knnhandle`** (input_control, state is modified)  class_knn `→` HHandle

Handle of the k-NN classifier.

**`features`** (input_control)  number(-array) `→` MaybeSequence[float]

List of features to add.

**`class_id`** (input_control)  integer(-array) `→` MaybeSequence[int]

Class IDs of the features.

## Result

If the parameters are valid, the operator `add_sample_class_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## See also

`create_class_knn`,
`read_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
