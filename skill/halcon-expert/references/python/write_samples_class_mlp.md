# write_samples_class_mlp (Operator)

## Name

`write_samples_class_mlp` — Write the training data of a multilayer perceptron to a file.

## Signature

`def write_samples_class_mlp(mlphandle: HHandle, file_name: str) -> None`

## Description

`write_samples_class_mlp` writes the training samples stored
in the multilayer perceptron (MLP) *`mlphandle`* to the file
given by *`file_name`*. `write_samples_class_mlp` can be
used to build up a database of training samples, and hence to
improve the performance of the MLP by training it with an extended
data set (see [`train_class_mlp`](train_class_mlp.md)). For other possible uses of
`write_samples_class_mlp` see [`get_prep_info_class_mlp`](get_prep_info_class_mlp.md).

The file *`file_name`* is overwritten by
`write_samples_class_mlp`. Nevertheless, extending the
database of training samples is easy to do because
[`read_samples_class_mlp`](read_samples_class_mlp.md) and [`add_sample_class_mlp`](add_sample_class_mlp.md) add
the training samples to the training samples that are already stored
in memory with the MLP.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`file_name`** (input_control)  filename.write `→` str

File name.

## Result

If the parameters are valid, the operator
`write_samples_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`add_sample_class_mlp`

## Possible Successors

`clear_samples_class_mlp`

## See also

`create_class_mlp`,
`get_prep_info_class_mlp`,
`read_samples_class_mlp`

## Module

Foundation
