# WriteSamplesClassGmm (Operator)

## Name

`WriteSamplesClassGmm` — Write the training data of a Gaussian Mixture Model to a file.

## Signature

`static void HOperatorSet.WriteSamplesClassGmm(HTuple GMMHandle, HTuple fileName)`

`void HClassGmm.WriteSamplesClassGmm(string fileName)`

## Description

`WriteSamplesClassGmm` writes the training samples stored
in the Gaussian Mixture Model (GMM) *`GMMHandle`* to the file
given by *`fileName`*. `WriteSamplesClassGmm` can be
used to build up a database of training samples, and hence to
improve the performance of the GMM by training it with an extended
data set (see [`TrainClassGmm`](train_class_gmm.md)).

The file *`fileName`* is overwritten by
`WriteSamplesClassGmm`. Nevertheless, extending the
database of training samples is easy because
[`ReadSamplesClassGmm`](read_samples_class_gmm.md) and [`AddSampleClassGmm`](add_sample_class_gmm.md) add
the training samples to the training samples that are already stored
in memory with the GMM.

The created file can be read with [`ReadSamplesClassMlp`](read_samples_class_mlp.md) if
the classifier of a multilayer perceptron (MLP) should be
used. The class of a training sample in the GMM corresponds to a
component of the target vector in the MLP being 1.0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

## Result

If the parameters are valid, the operator
`WriteSamplesClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`AddSampleClassGmm`

## Possible Successors

`ClearSamplesClassGmm`

## See also

`CreateClassGmm`,
`ReadSamplesClassGmm`,
`ReadSamplesClassMlp`,
`WriteSamplesClassMlp`

## Module

Foundation
