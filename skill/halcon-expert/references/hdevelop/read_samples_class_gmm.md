# read_samples_class_gmm (Operator)

## Name

`read_samples_class_gmm` — Read the training data of a Gaussian Mixture Model from a file.

## Signature

`read_samples_class_gmm( : : GMMHandle, FileName : )`

## Description

`read_samples_class_gmm` reads training samples from the file
given by *`FileName`* and adds them to the training samples
that have already been stored in the Gaussian Mixture Model (GMM)
given by *`GMMHandle`*. The GMM must be created with
[`create_class_gmm`](create_class_gmm.md) before calling
`read_samples_class_gmm`. As described with
[`train_class_gmm`](train_class_gmm.md) and [`write_samples_class_gmm`](write_samples_class_gmm.md),
`read_samples_class_gmm`, [`add_sample_class_gmm`](add_sample_class_gmm.md), and
[`write_samples_class_gmm`](write_samples_class_gmm.md) can be used to build up a database
of training samples, and hence to improve the performance of the GMM
by retraining the GMM with extended data sets.

It should be noted that the training samples must have the correct
dimensionality. The feature vectors stored in *`FileName`*
must have the lengths `NumDim` that was specified with
[`create_class_gmm`](create_class_gmm.md), and enough classes must have been created
in [`create_class_gmm`](create_class_gmm.md). If this is not the case, an error
message is returned.

It is possible to read files of samples that were written with
[`write_samples_class_svm`](write_samples_class_svm.md) or [`write_samples_class_mlp`](write_samples_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm `→`  (handle)

GMM handle.

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

## Result

If the parameters are valid, the operator
`read_samples_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_class_gmm`

## Possible Successors

`train_class_gmm`

## Alternatives

`add_sample_class_gmm`

## See also

`write_samples_class_gmm`,
`write_samples_class_mlp`,
`clear_samples_class_gmm`

## Module

Foundation
