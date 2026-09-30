# create_class_knn (Operator)

## Name

`create_class_knn` — Create a k-nearest neighbors (k-NN) classifier.

## Signature

`def create_class_knn(num_dim: Sequence[int]) -> HHandle`

## Description

`create_class_knn` creates a k-nearest neighbors (k-NN) data structure.
This can be either used to classify data or to approximately locate
nearest neighbors in a *`num_dim`*-dimensional space.

Most of the operators described in Classification/K-Nearest-Neighbor use
the resulting handle *`knnhandle`*.

The k-NN classifies by searching approximately the nearest neighbors and
returning their classes as result. With the used
approximation, the search time is logarithmically to the number of samples
and dimensions.

The dimension of the feature vectors is the only parameter that necessarily
has to be set in *`num_dim`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`num_dim`** (input_control)  number-array `→` Sequence[int]

Number of dimensions of the feature.

Default:
10

**`knnhandle`** (output_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator `create_class_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`add_sample_class_knn`,
`train_class_knn`

## Alternatives

`create_class_svm`,
`create_class_mlp`

## See also

`select_feature_set_knn`,
`read_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
