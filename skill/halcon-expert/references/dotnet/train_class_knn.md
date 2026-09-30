# TrainClassKnn (Operator)

## Name

`TrainClassKnn` — Creates the search trees for a k-NN classifier.

## Signature

`static void HOperatorSet.TrainClassKnn(HTuple KNNHandle, HTuple genParamName, HTuple genParamValue)`

`void HClassKnn.TrainClassKnn(HTuple genParamName, HTuple genParamValue)`

## Description

`TrainClassKnn` creates the search trees for
a k-NN classifier.

It is possible to set the number of trees via
the parameters *`genParamName`* and *`genParamValue`* by
*"num_trees"*. The default value for the number of search trees
is *4*. A higher number of trees improves the accuracy of
the search, but increases the run time.

It is possible to add more samples after training using the operator
[`AddSampleClassKnn`](add_sample_class_knn.md). The added data affects the classification
only, if `TrainClassKnn` is called again.

Automatic feature normalization can be activated by setting
*"normalization"* in *`genParamName`* and *"true"*
in *`genParamValue`*. The feature vectors are normalized by
normalizing each dimension separately. For each dimension, the mean and
standard deviation is calculated over the training samples. Every feature
vector is normalized by subtracting the mean and dividing by the standard
deviation of the individual dimension.
This results in a normalization, where each dimension has zero mean and
unit variance. If the standard deviation happens to be zero, only the mean
is subtracted. Please note however, that a feature dimension with no
standard deviation does not change the classification result and should be
removed. Automatic feature normalization will change the stored training
data, but the original data can be restored at any time by calling
`TrainClassKnn` with *"normalization"* set to
*"false"*. If normalization is used, the operator
[`ClassifyClassKnn`](classify_class_knn.md) interprets the input data as unnormalized and
performs normalization internally as it has been defined in the last call
to `TrainClassKnn`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- KNNHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`KNNHandle`** (input_control, state is modified)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be adjusted
for the k-NN classifier creation.

Default:
[]

List of values:
"normalization", "num_trees"

**`genParamValue`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / string / double)

Values of the generic parameters that can be adjusted
for the k-NN classifier creation.

Default:
[]

Suggested values:
4, "false", "true"

## Result

If the parameters are valid, the operator `TrainClassKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassKnn`,
`ReadClassKnn`

## Alternatives

`SelectFeatureSetKnn`

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
