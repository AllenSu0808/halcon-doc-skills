# clear_samples_class_gmm (Operator)

## Name

`clear_samples_class_gmm` — Clear the training data of a Gaussian Mixture Model.

## Signature

`def clear_samples_class_gmm(gmmhandle: MaybeSequence[HHandle]) -> None`

## Description

`clear_samples_class_gmm` clears all training samples that
have been stored in the Gaussian Mixture Model (GMM)
*`gmmhandle`*. `clear_samples_class_gmm` should only be
used if the GMM is trained in the same process that uses the GMM for
evaluation with [`evaluate_class_gmm`](evaluate_class_gmm.md) or for classification
with [`classify_class_gmm`](classify_class_gmm.md). In this case, the memory required
for the training samples can be freed with
`clear_samples_class_gmm`, and hence memory can be saved. In
the normal usage, in which the GMM is trained offline and written to
a file with [`write_class_gmm`](write_class_gmm.md), it is typically unnecessary to
call `clear_samples_class_gmm` because [`write_class_gmm`](write_class_gmm.md)
does not save the training samples, and hence the online process,
which reads the GMM with [`read_class_gmm`](read_class_gmm.md), requires no memory
for the training samples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- gmmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`gmmhandle`** (input_control, state is modified)  class_gmm(-array) `→` MaybeSequence[HHandle]

GMM handle.

## Result

If the parameters are valid, the operator
`clear_samples_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`train_class_gmm`,
`write_samples_class_gmm`

## See also

`create_class_gmm`,
`clear_class_gmm`,
`add_sample_class_gmm`,
`read_samples_class_gmm`

## Module

Foundation
