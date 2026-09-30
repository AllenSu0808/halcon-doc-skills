# classify_class_mlp (Operator)

## Name

`classify_class_mlp` — Calculate the class of a feature vector by a multilayer perceptron.

## Signature

`classify_class_mlp( : : MLPHandle, Features, Num : Class, Confidence)`

## Description

`classify_class_mlp` computes the best *`Num`* classes of
the feature vector *`Features`* with the multilayer perceptron
(MLP) *`MLPHandle`* and returns the classes in *`Class`*
and the corresponding confidences (probabilities) of the classes in
*`Confidence`*. Before calling `classify_class_mlp`, the
MLP must be trained with [`train_class_mlp`](train_class_mlp.md).

`classify_class_mlp` can only be called if the MLP is used as
a classifier with `OutputFunction` = *'softmax'*
(see [`create_class_mlp`](create_class_mlp.md)). Otherwise, an error message is
returned. `classify_class_mlp` corresponds to a call to
[`evaluate_class_mlp`](evaluate_class_mlp.md) and an additional step that extracts the
best *`Num`* classes. As described with
[`evaluate_class_mlp`](evaluate_class_mlp.md), the output values of the MLP can be
interpreted as probabilities of the occurrence of the respective
classes. In most cases it should be sufficient
to use *`Num`* = *1* in order to decide whether the
probability of the best class is high enough. In some applications
it may be interesting to also take the second best class into
account (*`Num`* = *2*), particularly if it can be
expected that the classes show a significant degree of overlap.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector.

**`Num`** (input_control)  integer-array `→`  (integer)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`Class`** (output_control)  integer(-array) `→`  (integer)

Result of classifying the feature vector with
the MLP.

**`Confidence`** (output_control)  real(-array) `→`  (real)

Confidence(s) of the class(es) of the feature vector.

## Result

If the parameters are valid, the operator `classify_class_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_mlp`,
`read_class_mlp`

## Alternatives

`apply_dl_model`,
`evaluate_class_mlp`

## See also

`create_class_mlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
