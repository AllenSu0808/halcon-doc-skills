# clear_samples_class_mlp (Operator)

## Name

`clear_samples_class_mlp` — Clear the training data of a multilayer perceptron.

## Signature

`def clear_samples_class_mlp(mlphandle: MaybeSequence[HHandle]) -> None`

## Description

`clear_samples_class_mlp` clears all training samples that
have been added to the multilayer perceptron (MLP)
*`mlphandle`* with [`add_sample_class_mlp`](add_sample_class_mlp.md) or
[`read_samples_class_mlp`](read_samples_class_mlp.md). `clear_samples_class_mlp`
should only be used if the MLP is trained in the same process that
uses the MLP for evaluation with [`evaluate_class_mlp`](evaluate_class_mlp.md) or for
classification with [`classify_class_mlp`](classify_class_mlp.md). In this case, the
memory required for the training samples can be freed with
`clear_samples_class_mlp`, and hence memory can be saved. In
the normal usage, in which the MLP is trained offline and written to
a file with [`write_class_mlp`](write_class_mlp.md), it is typically unnecessary to
call `clear_samples_class_mlp` because [`write_class_mlp`](write_class_mlp.md)
does not save the training samples, and hence the online process,
which reads the MLP with [`read_class_mlp`](read_class_mlp.md), requires no memory
for the training samples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- mlphandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`mlphandle`** (input_control, state is modified)  class_mlp(-array) `→` MaybeSequence[HHandle]

MLP handle.

## Result

If the parameters are valid, the operator
`clear_samples_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`train_class_mlp`,
`write_samples_class_mlp`

## See also

`create_class_mlp`,
`clear_class_mlp`,
`add_sample_class_mlp`,
`read_samples_class_mlp`

## Module

Foundation
