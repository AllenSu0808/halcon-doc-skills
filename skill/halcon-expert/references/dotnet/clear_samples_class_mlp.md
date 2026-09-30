# ClearSamplesClassMlp (Operator)

## Name

`ClearSamplesClassMlp` — Clear the training data of a multilayer perceptron.

## Signature

`static void HOperatorSet.ClearSamplesClassMlp(HTuple MLPHandle)`

`static void HClassMlp.ClearSamplesClassMlp(HClassMlp[] MLPHandle)`

`void HClassMlp.ClearSamplesClassMlp()`

## Description

`ClearSamplesClassMlp` clears all training samples that
have been added to the multilayer perceptron (MLP)
*`MLPHandle`* with [`AddSampleClassMlp`](add_sample_class_mlp.md) or
[`ReadSamplesClassMlp`](read_samples_class_mlp.md). `ClearSamplesClassMlp`
should only be used if the MLP is trained in the same process that
uses the MLP for evaluation with [`EvaluateClassMlp`](evaluate_class_mlp.md) or for
classification with [`ClassifyClassMlp`](classify_class_mlp.md). In this case, the
memory required for the training samples can be freed with
`ClearSamplesClassMlp`, and hence memory can be saved. In
the normal usage, in which the MLP is trained offline and written to
a file with [`WriteClassMlp`](write_class_mlp.md), it is typically unnecessary to
call `ClearSamplesClassMlp` because [`WriteClassMlp`](write_class_mlp.md)
does not save the training samples, and hence the online process,
which reads the MLP with [`ReadClassMlp`](read_class_mlp.md), requires no memory
for the training samples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp(-array) `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

## Result

If the parameters are valid, the operator
`ClearSamplesClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`TrainClassMlp`,
`WriteSamplesClassMlp`

## See also

`CreateClassMlp`,
`ClearClassMlp`,
`AddSampleClassMlp`,
`ReadSamplesClassMlp`

## Module

Foundation
