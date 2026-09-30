# WriteSamplesClassMlp (Operator)

## Name

`WriteSamplesClassMlp` — Write the training data of a multilayer perceptron to a file.

## Signature

`static void HOperatorSet.WriteSamplesClassMlp(HTuple MLPHandle, HTuple fileName)`

`void HClassMlp.WriteSamplesClassMlp(string fileName)`

## Description

`WriteSamplesClassMlp` writes the training samples stored
in the multilayer perceptron (MLP) *`MLPHandle`* to the file
given by *`fileName`*. `WriteSamplesClassMlp` can be
used to build up a database of training samples, and hence to
improve the performance of the MLP by training it with an extended
data set (see [`TrainClassMlp`](train_class_mlp.md)). For other possible uses of
`WriteSamplesClassMlp` see [`GetPrepInfoClassMlp`](get_prep_info_class_mlp.md).

The file *`fileName`* is overwritten by
`WriteSamplesClassMlp`. Nevertheless, extending the
database of training samples is easy to do because
[`ReadSamplesClassMlp`](read_samples_class_mlp.md) and [`AddSampleClassMlp`](add_sample_class_mlp.md) add
the training samples to the training samples that are already stored
in memory with the MLP.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

## Result

If the parameters are valid, the operator
`WriteSamplesClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`AddSampleClassMlp`

## Possible Successors

`ClearSamplesClassMlp`

## See also

`CreateClassMlp`,
`GetPrepInfoClassMlp`,
`ReadSamplesClassMlp`

## Module

Foundation
