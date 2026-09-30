# ClassifyClassMlp (Operator)

## Name

`ClassifyClassMlp` — Calculate the class of a feature vector by a multilayer perceptron.

## Signature

`static void HOperatorSet.ClassifyClassMlp(HTuple MLPHandle, HTuple features, HTuple num, out HTuple classVal, out HTuple confidence)`

`HTuple HClassMlp.ClassifyClassMlp(HTuple features, HTuple num, out HTuple confidence)`

`int HClassMlp.ClassifyClassMlp(HTuple features, HTuple num, out double confidence)`

## Description

`ClassifyClassMlp` computes the best *`num`* classes of
the feature vector *`features`* with the multilayer perceptron
(MLP) *`MLPHandle`* and returns the classes in *`classVal`*
and the corresponding confidences (probabilities) of the classes in
*`confidence`*. Before calling `ClassifyClassMlp`, the
MLP must be trained with [`TrainClassMlp`](train_class_mlp.md).

`ClassifyClassMlp` can only be called if the MLP is used as
a classifier with `outputFunction` = *"softmax"*
(see [`CreateClassMlp`](create_class_mlp.md)). Otherwise, an error message is
returned. `ClassifyClassMlp` corresponds to a call to
[`EvaluateClassMlp`](evaluate_class_mlp.md) and an additional step that extracts the
best *`num`* classes. As described with
[`EvaluateClassMlp`](evaluate_class_mlp.md), the output values of the MLP can be
interpreted as probabilities of the occurrence of the respective
classes. In most cases it should be sufficient
to use *`num`* = *1* in order to decide whether the
probability of the best class is high enough. In some applications
it may be interesting to also take the second best class into
account (*`num`* = *2*), particularly if it can be
expected that the classes show a significant degree of overlap.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector.

**`num`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classVal`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Result of classifying the feature vector with
the MLP.

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence(s) of the class(es) of the feature vector.

## Result

If the parameters are valid, the operator `ClassifyClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainClassMlp`,
`ReadClassMlp`

## Alternatives

`ApplyDlModel`,
`EvaluateClassMlp`

## See also

`CreateClassMlp`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Andrew Webb: “Statistical Pattern Recognition”; Arnold, London;
1999.

## Module

Foundation
