# write_samples_class_gmm (Operator)

## Name

`write_samples_class_gmm` — Write the training data of a Gaussian Mixture Model to a file.

## Signature

`def write_samples_class_gmm(gmmhandle: HHandle, file_name: str) -> None`

## Description

`write_samples_class_gmm` writes the training samples stored
in the Gaussian Mixture Model (GMM) *`gmmhandle`* to the file
given by *`file_name`*. `write_samples_class_gmm` can be
used to build up a database of training samples, and hence to
improve the performance of the GMM by training it with an extended
data set (see [`train_class_gmm`](train_class_gmm.md)).

The file *`file_name`* is overwritten by
`write_samples_class_gmm`. Nevertheless, extending the
database of training samples is easy because
[`read_samples_class_gmm`](read_samples_class_gmm.md) and [`add_sample_class_gmm`](add_sample_class_gmm.md) add
the training samples to the training samples that are already stored
in memory with the GMM.

The created file can be read with [`read_samples_class_mlp`](read_samples_class_mlp.md) if
the classifier of a multilayer perceptron (MLP) should be
used. The class of a training sample in the GMM corresponds to a
component of the target vector in the MLP being 1.0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gmmhandle`** (input_control)  class_gmm `→` HHandle

GMM handle.

**`file_name`** (input_control)  filename.write `→` str

File name.

## Result

If the parameters are valid, the operator
`write_samples_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`add_sample_class_gmm`

## Possible Successors

`clear_samples_class_gmm`

## See also

`create_class_gmm`,
`read_samples_class_gmm`,
`read_samples_class_mlp`,
`write_samples_class_mlp`

## Module

Foundation
