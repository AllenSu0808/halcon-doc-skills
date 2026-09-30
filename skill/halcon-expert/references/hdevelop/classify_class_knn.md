# classify_class_knn (Operator)

## Name

`classify_class_knn` — Search for the next neighbors for a given feature vector.

## Signature

`classify_class_knn( : : KNNHandle, Features : Result, Rating)`

## Description

`classify_class_knn` searches for the next *'k'*
neighbors of the feature vector given in *`Features`*.
The distance which is used to determine the next neighbor is
the L2-norm of the given vector and the training samples.

The value of *'k'* can be set via [`set_params_class_knn`](set_params_class_knn.md).
The results can either be the determined class of the feature vector or
the indices of the nearest neighbors. The selection of the result behavior
can be made by [`set_params_class_knn`](set_params_class_knn.md) via the generic parameters
*'method'* and *'max_num_classes'*:

- ***'classes_distance'*:** —

  returns the nearest samples
  for each of maximally *'max_num_classes'* different classes,
  if they have a representative in the nearest *'k'* neighbors.
  The results in *`Result`* are classes sorted by their minimal
  distance in *`Rating`*. There is no efficient way to determine in a
  k-NN-tree the nearest neighbor for exactly *'max_num_classes'*
  classes.
- ***'classes_frequency'*:** —

  counts the occurrences of certain
  classes among the nearest *'k'* neighbors and returns the occurring
  classes in *`Result`* sorted by their relative frequency that is
  returned in *`Rating`*. Again, maximally *'max_num_classes'*
  values are returned.
- ***'classes_weighted_frequencies'*:** —

  counts the occurrences of certain classes among the
  nearest *'k'* neighbors and returns the occurring classes
  in *`Result`* sorted by their relative frequency weighted with the
  average distance that is returned in *`Rating`*.
  Again, maximally *'max_num_classes'* values are returned.
- ***'neighbors_distance'*:** —

  returns the indices of the nearest
  *'k'* neighbors in *`Result`*
  and the distances in *`Rating`*.

The default behavior is *'classes_distance'* and returns the
classes and distances.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`Features`** (input_control)  number-array `→`  (real)

Features that should be classified.

**`Result`** (output_control)  number-array `→`  (integer)

The classification result, either class IDs or sample
indices.

**`Rating`** (output_control)  number-array `→`  (real)

A rating for the results. This value contains either a
distance, a frequency or a weighted frequency.

## Result

If the parameters are valid, the operator `classify_class_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`,
`set_params_class_knn`

## Possible Successors

`clear_class_knn`

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
