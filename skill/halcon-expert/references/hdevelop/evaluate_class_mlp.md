# evaluate_class_mlp (Operator)

## Name

`evaluate_class_mlp` — Calculate the evaluation of a feature vector by a multilayer
perceptron.

## Signature

`evaluate_class_mlp( : : MLPHandle, Features : Result)`

## Description

`evaluate_class_mlp` computes the result *`Result`* of
evaluating the feature vector *`Features`* with the multilayer
perceptron (MLP) *`MLPHandle`*. The formulas used for the
evaluation are described with [`create_class_mlp`](create_class_mlp.md). Before
calling `evaluate_class_mlp`, the MLP must be trained with
[`train_class_mlp`](train_class_mlp.md).

If the MLP is used for regression (function approximation), i.e., if
(`OutputFunction` = *'linear'*), *`Result`* is
the value of the function at the coordinate *`Features`*. For
`OutputFunction` = *'logistic'* and
*'softmax'*, the values in *`Result`* can be interpreted
as probabilities. Hence, for `OutputFunction` =
*'logistic'* the elements of *`Result`* represent the
probabilities of the presence of the respective independent
attributes. Typically, a threshold of 0.5 is used to decide whether
the attribute is present or not. Depending on the application,
other thresholds may be used as well. For `OutputFunction`
= *'softmax'* usually the position of the maximum value of
*`Result`* is interpreted as the class of the feature vector,
and the corresponding value as the probability of the class. In
this case, [`classify_class_mlp`](classify_class_mlp.md) should be used instead of
`evaluate_class_mlp` because [`classify_class_mlp`](classify_class_mlp.md)
directly returns the class and corresponding probability.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector.

**`Result`** (output_control)  real-array `→`  (real)

Result of evaluating the feature vector with
the MLP.

## Result

If the parameters are valid, the operator `evaluate_class_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_mlp`,
`read_class_mlp`

## Alternatives

`classify_class_mlp`

## See also

`create_class_mlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
