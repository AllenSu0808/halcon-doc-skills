# write_class_mlp (Operator)

## Name

`write_class_mlp` — Write a multilayer perceptron to a file.

## Signature

`write_class_mlp( : : MLPHandle, FileName : )`

## Description

`write_class_mlp` writes the multilayer perceptron (MLP)
*`MLPHandle`* to the file given by *`FileName`*.
The default HALCON file extension for the MLP classifier is 'gmc'.
`write_class_mlp` is typically called after the MLP has been
trained with [`train_class_mlp`](train_class_mlp.md). The MLP can be read with
[`read_class_mlp`](read_class_mlp.md). `write_class_mlp` does *not*
write any training samples that possibly have been stored in the
MLP. For this purpose, [`write_samples_class_mlp`](write_samples_class_mlp.md) should be
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`gmc`

## Result

If the parameters are valid, the operator `write_class_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_mlp`

## Possible Successors

`clear_class_mlp`

## See also

`create_class_mlp`,
`read_class_mlp`,
`write_samples_class_mlp`

## Module

Foundation
