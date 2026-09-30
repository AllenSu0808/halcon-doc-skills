# get_params_class_knn (Operator)

## Name

`get_params_class_knn` — Get parameters of a k-NN classification.

## Signature

`get_params_class_knn( : : KNNHandle, GenParamName : GenParamValue)`

## Description

`get_params_class_knn` gets parameters of
the k-NN referred by *`KNNHandle`*. The possible entries in
*`GenParamName`* are:

- ***'method'*:** —

  Retrieve the currently selected method
  for determining the result of [`classify_class_knn`](classify_class_knn.md).
  The result can be *'classes_distance'*,
  *'classes_frequency'*, *'classes_weighted_frequencies'*
  or *'neighbors_distance'*.
- ***'k'*:** —

  The number of nearest neighbors that is considered
  to determine the results.
- ***'max_num_classes'*:** —

  The maximum number of classes that are
  returned. This parameter is ignored in case the method
  *'neighbors_distance'* is selected.
- ***'num_checks'*:** —

  Defines the maximum number of runs through
  the trees.
- ***'epsilon'*:** —

  A parameter to lower the accuracy in
  the tree to gain speed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`GenParamName`** (input_control)  string-array `→`  (string)

Names of the parameters that can be read
from the k-NN classifier.

Default:
['method','k']

List of values:
'epsilon', 'k', 'method', 'num_checks'

**`GenParamValue`** (output_control)  number-array `→`  (integer / real / string)

Values of the selected parameters.

## Result

If the parameters are valid, the operator `get_params_class_knn`
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
`read_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
