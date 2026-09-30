# CreateClassKnn (Operator)

## Name

`CreateClassKnn` — Create a k-nearest neighbors (k-NN) classifier.

## Signature

`static void HOperatorSet.CreateClassKnn(HTuple numDim, out HTuple KNNHandle)`

`public HClassKnn(HTuple numDim)`

`void HClassKnn.CreateClassKnn(HTuple numDim)`

## Description

`CreateClassKnn` creates a k-nearest neighbors (k-NN) data structure.
This can be either used to classify data or to approximately locate
nearest neighbors in a *`numDim`*-dimensional space.

Most of the operators described in Classification/K-Nearest-Neighbor use
the resulting handle *`KNNHandle`*.

The k-NN classifies by searching approximately the nearest neighbors and
returning their classes as result. With the used
approximation, the search time is logarithmically to the number of samples
and dimensions.

The dimension of the feature vectors is the only parameter that necessarily
has to be set in *`numDim`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`numDim`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long)

Number of dimensions of the feature.

Default:
10

**`KNNHandle`** (output_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator `CreateClassKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`AddSampleClassKnn`,
`TrainClassKnn`

## Alternatives

`CreateClassSvm`,
`CreateClassMlp`

## See also

`SelectFeatureSetKnn`,
`ReadClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
