# set_params_class_knn (Operator)

## Name

`set_params_class_knn` — Set parameters for k-NN classification.

## Signature

`set_params_class_knn( : : KNNHandle, GenParamName, GenParamValue : )`

## Description

`set_params_class_knn` sets parameters for the classification
of the k-nearest neighbors (k-NN) classifier *`KNNHandle`*.
It controls the behavior of [`classify_class_knn`](classify_class_knn.md).

The value of *'k'* can be set via *`GenParamName`* and
*`GenParamValue`*. Increasing *'k'* also increases the accuracy
of the resulting neighbors and increases the run time.

The results can either be the determined class of the feature vector or
the indices of the nearest neighbors. The result behavior
can be selected with `set_params_class_knn` via the generic parameters
*'method'* and *'max_num_classes'*:

- ***'classes_distance'*:** —

  returns the nearest samples
  for each of maximally *'max_num_classes'* different classes,
  if they have a representative in the nearest *'k'* neighbors.
  The results are classes sorted by their minimal
  distance. There is no efficient way to determine in a
  k-NN-tree the nearest neighbor for exactly *'max_num_classes'*
  classes.
- ***'classes_frequency'*:** —

  counts the occurrences of certain
  classes among the nearest *'k'* neighbors and returns the occurring
  classes sorted by their relative frequency that is
  returned, too. Again, maximally *'max_num_classes'*
  values are returned.
- ***'classes_weighted_frequencies'*:** —

  counts the occurrences of certain classes among the
  nearest *'k'* neighbors and returns the occurring classes sorted
  by their relative frequency weighted with the
  average distance that is returned, too.
  Again, maximally *'max_num_classes'* values are returned.
- ***'neighbors_distance'*:** —

  returns the indices of the nearest
  *'k'* neighbors and the distances.

The default behavior is *'classes_distance'*.

The option *'num_checks'* allows to set the number of maximal runs
through the trees. The parameter has to be positive and the default value is
*32*. The higher this value is, the more accurate the results will be.
As a trade-off, the running time will also be higher. Setting this parameter
to *0* triggers an exact search.

The option *'epsilon'* allows to set a stop criteria if the value
is increased from the default value 0.0.
The higher the value is set, the less accurate results of the
estimated neighbors can be expected, while it might speed up the search.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- KNNHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`KNNHandle`** (input_control, state is modified)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`GenParamName`** (input_control)  string-array `→`  (string)

Names of the generic parameters that can be adjusted
for the k-NN classifier.

Default:
['method','k','max_num_classes']

List of values:
'epsilon', 'k', 'max_num_classes', 'method', 'num_checks'

**`GenParamValue`** (input_control)  number-array `→`  (integer / real / string)

Values of the generic parameters that can be adjusted
for the k-NN classifier.

Default:
['classes_distance',5,1]

Suggested values:
'classes_distance', 'classes_frequency', 'classes_weighted_frequencies', 'neighbors_distance', 32, 0.0, 0.02, 0, 1, 2, 3, 4, 5, 6

## Result

If the parameters are valid, the operator `set_params_class_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## Possible Successors

`classify_class_knn`

## See also

`create_class_knn`,
`read_class_knn`,
`get_params_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
