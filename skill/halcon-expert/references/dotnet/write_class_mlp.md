# WriteClassMlp (Operator)

## Name

`WriteClassMlp` — Write a multilayer perceptron to a file.

## Signature

`static void HOperatorSet.WriteClassMlp(HTuple MLPHandle, HTuple fileName)`

`void HClassMlp.WriteClassMlp(string fileName)`

## Description

`WriteClassMlp` writes the multilayer perceptron (MLP)
*`MLPHandle`* to the file given by *`fileName`*.
The default HALCON file extension for the MLP classifier is 'gmc'.
`WriteClassMlp` is typically called after the MLP has been
trained with [`TrainClassMlp`](train_class_mlp.md). The MLP can be read with
[`ReadClassMlp`](read_class_mlp.md). `WriteClassMlp` does *not*
write any training samples that possibly have been stored in the
MLP. For this purpose, [`WriteSamplesClassMlp`](write_samples_class_mlp.md) should be
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`gmc`

## Result

If the parameters are valid, the operator `WriteClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainClassMlp`

## Possible Successors

`ClearClassMlp`

## See also

`CreateClassMlp`,
`ReadClassMlp`,
`WriteSamplesClassMlp`

## Module

Foundation
