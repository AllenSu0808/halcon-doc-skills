# read_samples_class_mlp (Operator)

## Name

`read_samples_class_mlp` — Read the training data of a multilayer perceptron from a file.

## Signature

`def read_samples_class_mlp(mlphandle: HHandle, file_name: str) -> None`

## Description

`read_samples_class_mlp` reads training samples from the file
given by *`file_name`* and adds them to the training samples
that have already been added to the multilayer perceptron (MLP)
given by *`mlphandle`*. The MLP must be created with
[`create_class_mlp`](create_class_mlp.md) before calling
`read_samples_class_mlp`. As described with
[`train_class_mlp`](train_class_mlp.md) and [`write_samples_class_mlp`](write_samples_class_mlp.md), the
operators `read_samples_class_mlp`,
[`add_sample_class_mlp`](add_sample_class_mlp.md), and [`write_samples_class_mlp`](write_samples_class_mlp.md)
can be used to build up a extensive set of training samples, and
hence to improve the performance of the MLP by retraining the MLP
with extended data sets.

It should be noted that the training samples must have the correct
dimensionality. The feature vectors and target vectors stored in
*`file_name`* must have the lengths `num_input` and
`num_output` that were specified with
[`create_class_mlp`](create_class_mlp.md). If this is not the case an error message
is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- mlphandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`mlphandle`** (input_control, state is modified)  class_mlp `→` HHandle

MLP handle.

**`file_name`** (input_control)  filename.read `→` str

File name.

## Result

If the parameters are valid, the operator
`read_samples_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_class_mlp`

## Possible Successors

`train_class_mlp`

## Alternatives

`add_sample_class_mlp`

## See also

`write_samples_class_mlp`,
`clear_samples_class_mlp`

## Module

Foundation
