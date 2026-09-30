# ReadSamplesClassGmm (Operator)

## Name

`ReadSamplesClassGmm` — Read the training data of a Gaussian Mixture Model from a file.

## Signature

`static void HOperatorSet.ReadSamplesClassGmm(HTuple GMMHandle, HTuple fileName)`

`void HClassGmm.ReadSamplesClassGmm(string fileName)`

## Description

`ReadSamplesClassGmm` reads training samples from the file
given by *`fileName`* and adds them to the training samples
that have already been stored in the Gaussian Mixture Model (GMM)
given by *`GMMHandle`*. The GMM must be created with
[`CreateClassGmm`](create_class_gmm.md) before calling
`ReadSamplesClassGmm`. As described with
[`TrainClassGmm`](train_class_gmm.md) and [`WriteSamplesClassGmm`](write_samples_class_gmm.md),
`ReadSamplesClassGmm`, [`AddSampleClassGmm`](add_sample_class_gmm.md), and
[`WriteSamplesClassGmm`](write_samples_class_gmm.md) can be used to build up a database
of training samples, and hence to improve the performance of the GMM
by retraining the GMM with extended data sets.

It should be noted that the training samples must have the correct
dimensionality. The feature vectors stored in *`fileName`*
must have the lengths `numDim` that was specified with
[`CreateClassGmm`](create_class_gmm.md), and enough classes must have been created
in [`CreateClassGmm`](create_class_gmm.md). If this is not the case, an error
message is returned.

It is possible to read files of samples that were written with
[`WriteSamplesClassSvm`](write_samples_class_svm.md) or [`WriteSamplesClassMlp`](write_samples_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

## Result

If the parameters are valid, the operator
`ReadSamplesClassGmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateClassGmm`

## Possible Successors

`TrainClassGmm`

## Alternatives

`AddSampleClassGmm`

## See also

`WriteSamplesClassGmm`,
`WriteSamplesClassMlp`,
`ClearSamplesClassGmm`

## Module

Foundation
