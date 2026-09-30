# GetParamsClassKnn (Operator)

## Name

`GetParamsClassKnn` — Get parameters of a k-NN classification.

## Signature

`static void HOperatorSet.GetParamsClassKnn(HTuple KNNHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HClassKnn.GetParamsClassKnn(HTuple genParamName)`

## Description

`GetParamsClassKnn` gets parameters of
the k-NN referred by *`KNNHandle`*. The possible entries in
*`genParamName`* are:

- ***"method"*:** —

  Retrieve the currently selected method
  for determining the result of [`ClassifyClassKnn`](classify_class_knn.md).
  The result can be *"classes_distance"*,
  *"classes_frequency"*, *"classes_weighted_frequencies"*
  or *"neighbors_distance"*.
- ***"k"*:** —

  The number of nearest neighbors that is considered
  to determine the results.
- ***"max_num_classes"*:** —

  The maximum number of classes that are
  returned. This parameter is ignored in case the method
  *"neighbors_distance"* is selected.
- ***"num_checks"*:** —

  Defines the maximum number of runs through
  the trees.
- ***"epsilon"*:** —

  A parameter to lower the accuracy in
  the tree to gain speed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the parameters that can be read
from the k-NN classifier.

Default:
["method","k"]

List of values:
"epsilon", "k", "method", "num_checks"

**`genParamValue`** (output_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the selected parameters.

## Result

If the parameters are valid, the operator `GetParamsClassKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`TrainClassKnn`,
`ReadClassKnn`

## Possible Successors

`ClassifyClassKnn`

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
