# ClearSamplesClassGmm (Operator)

## Name

`ClearSamplesClassGmm` — Clear the training data of a Gaussian Mixture Model.

## Signature

`static void HOperatorSet.ClearSamplesClassGmm(HTuple GMMHandle)`

`static void HClassGmm.ClearSamplesClassGmm(HClassGmm[] GMMHandle)`

`void HClassGmm.ClearSamplesClassGmm()`

## Description

`ClearSamplesClassGmm` clears all training samples that
have been stored in the Gaussian Mixture Model (GMM)
*`GMMHandle`*. `ClearSamplesClassGmm` should only be
used if the GMM is trained in the same process that uses the GMM for
evaluation with [`EvaluateClassGmm`](evaluate_class_gmm.md) or for classification
with [`ClassifyClassGmm`](classify_class_gmm.md). In this case, the memory required
for the training samples can be freed with
`ClearSamplesClassGmm`, and hence memory can be saved. In
the normal usage, in which the GMM is trained offline and written to
a file with [`WriteClassGmm`](write_class_gmm.md), it is typically unnecessary to
call `ClearSamplesClassGmm` because [`WriteClassGmm`](write_class_gmm.md)
does not save the training samples, and hence the online process,
which reads the GMM with [`ReadClassGmm`](read_class_gmm.md), requires no memory
for the training samples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm(-array) `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

## Result

If the parameters are valid, the operator
`ClearSamplesClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`TrainClassGmm`,
`WriteSamplesClassGmm`

## See also

`CreateClassGmm`,
`ClearClassGmm`,
`AddSampleClassGmm`,
`ReadSamplesClassGmm`

## Module

Foundation
