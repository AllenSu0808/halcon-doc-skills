# EvaluateClassMlp (Operator)

## Name

`EvaluateClassMlp` — Calculate the evaluation of a feature vector by a multilayer
perceptron.

## Signature

`static void HOperatorSet.EvaluateClassMlp(HTuple MLPHandle, HTuple features, out HTuple result)`

`HTuple HClassMlp.EvaluateClassMlp(HTuple features)`

## Description

`EvaluateClassMlp` computes the result *`result`* of
evaluating the feature vector *`features`* with the multilayer
perceptron (MLP) *`MLPHandle`*. The formulas used for the
evaluation are described with [`CreateClassMlp`](create_class_mlp.md). Before
calling `EvaluateClassMlp`, the MLP must be trained with
[`TrainClassMlp`](train_class_mlp.md).

If the MLP is used for regression (function approximation), i.e., if
(`outputFunction` = *"linear"*), *`result`* is
the value of the function at the coordinate *`features`*. For
`outputFunction` = *"logistic"* and
*"softmax"*, the values in *`result`* can be interpreted
as probabilities. Hence, for `outputFunction` =
*"logistic"* the elements of *`result`* represent the
probabilities of the presence of the respective independent
attributes. Typically, a threshold of 0.5 is used to decide whether
the attribute is present or not. Depending on the application,
other thresholds may be used as well. For `outputFunction`
= *"softmax"* usually the position of the maximum value of
*`result`* is interpreted as the class of the feature vector,
and the corresponding value as the probability of the class. In
this case, [`ClassifyClassMlp`](classify_class_mlp.md) should be used instead of
`EvaluateClassMlp` because [`ClassifyClassMlp`](classify_class_mlp.md)
directly returns the class and corresponding probability.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

**`result`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Result of evaluating the feature vector with
the MLP.

## Result

If the parameters are valid, the operator `EvaluateClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainClassMlp`,
`ReadClassMlp`

## Alternatives

`ClassifyClassMlp`

## See also

`CreateClassMlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
