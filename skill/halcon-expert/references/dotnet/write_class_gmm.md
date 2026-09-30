# WriteClassGmm (Operator)

## Name

`WriteClassGmm` — Write a Gaussian Mixture Model to a file.

## Signature

`static void HOperatorSet.WriteClassGmm(HTuple GMMHandle, HTuple fileName)`

`void HClassGmm.WriteClassGmm(string fileName)`

## Description

`WriteClassGmm` writes the Gaussian Mixture Model (GMM)
*`GMMHandle`* to the file given by *`fileName`*.
The default HALCON file extension for the GMM classifier is 'ggc'.
`WriteClassGmm` is typically called after the GMM has been
trained with [`TrainClassGmm`](train_class_gmm.md). The GMM can be read with
[`ReadClassGmm`](read_class_gmm.md). `WriteClassGmm` does *not*
write any training samples that possibly have been stored in the
GMM. For this purpose, [`WriteSamplesClassGmm`](write_samples_class_gmm.md) should be
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`ggc`

## Result

If the parameters are valid, the operator `WriteClassGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`TrainClassGmm`

## Possible Successors

`ClearClassGmm`

## See also

`CreateClassGmm`,
`ReadClassGmm`,
`WriteSamplesClassGmm`

## Module

Foundation
