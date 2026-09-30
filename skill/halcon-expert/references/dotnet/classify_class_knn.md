# ClassifyClassKnn (Operator)

## Name

`ClassifyClassKnn` — Search for the next neighbors for a given feature vector.

## Signature

`static void HOperatorSet.ClassifyClassKnn(HTuple KNNHandle, HTuple features, out HTuple result, out HTuple rating)`

`HTuple HClassKnn.ClassifyClassKnn(HTuple features, out HTuple rating)`

## Description

`ClassifyClassKnn` searches for the next *"k"*
neighbors of the feature vector given in *`features`*.
The distance which is used to determine the next neighbor is
the L2-norm of the given vector and the training samples.

The value of *"k"* can be set via [`SetParamsClassKnn`](set_params_class_knn.md).
The results can either be the determined class of the feature vector or
the indices of the nearest neighbors. The selection of the result behavior
can be made by [`SetParamsClassKnn`](set_params_class_knn.md) via the generic parameters
*"method"* and *"max_num_classes"*:

- ***"classes_distance"*:** —

  returns the nearest samples
  for each of maximally *"max_num_classes"* different classes,
  if they have a representative in the nearest *"k"* neighbors.
  The results in *`result`* are classes sorted by their minimal
  distance in *`rating`*. There is no efficient way to determine in a
  k-NN-tree the nearest neighbor for exactly *"max_num_classes"*
  classes.
- ***"classes_frequency"*:** —

  counts the occurrences of certain
  classes among the nearest *"k"* neighbors and returns the occurring
  classes in *`result`* sorted by their relative frequency that is
  returned in *`rating`*. Again, maximally *"max_num_classes"*
  values are returned.
- ***"classes_weighted_frequencies"*:** —

  counts the occurrences of certain classes among the
  nearest *"k"* neighbors and returns the occurring classes
  in *`result`* sorted by their relative frequency weighted with the
  average distance that is returned in *`rating`*.
  Again, maximally *"max_num_classes"* values are returned.
- ***"neighbors_distance"*:** —

  returns the indices of the nearest
  *"k"* neighbors in *`result`*
  and the distances in *`rating`*.

The default behavior is *"classes_distance"* and returns the
classes and distances.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`features`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Features that should be classified.

**`result`** (output_control)  number-array `→` [HTuple](HTuple.md) (*int* / long)

The classification result, either class IDs or sample
indices.

**`rating`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

A rating for the results. This value contains either a
distance, a frequency or a weighted frequency.

## Result

If the parameters are valid, the operator `ClassifyClassKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`TrainClassKnn`,
`ReadClassKnn`,
`SetParamsClassKnn`

## Possible Successors

`ClearClassKnn`

## See also

`CreateClassKnn`,
`ReadClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
