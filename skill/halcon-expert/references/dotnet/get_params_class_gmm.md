# GetParamsClassGmm (Operator)

## Name

`GetParamsClassGmm` — Return the parameters of a Gaussian Mixture Model.

## Signature

`static void HOperatorSet.GetParamsClassGmm(HTuple GMMHandle, out HTuple numDim, out HTuple numClasses, out HTuple minCenters, out HTuple maxCenters, out HTuple covarType)`

`int HClassGmm.GetParamsClassGmm(out int numClasses, out HTuple minCenters, out HTuple maxCenters, out string covarType)`

## Description

`GetParamsClassGmm` returns the parameters of a Gaussian
Mixture Model (GMM) that were specified when the GMM was created
with [`CreateClassGmm`](create_class_gmm.md). This is particularly useful if the
GMM was read with [`ReadClassGmm`](read_class_gmm.md). The output of
`GetParamsClassGmm` can, for example, be used to check
whether the feature vectors and/or the target data to be used have
appropriate dimensions to be used with GMM. For a description of
the parameters, see [`CreateClassGmm`](create_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`numDim`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of dimensions of the feature space.

**`numClasses`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of classes of the GMM.

**`minCenters`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Minimum number of centers per GMM class.

**`maxCenters`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of centers per GMM class.

**`covarType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the covariance matrices.

## Result

If the parameters are valid, the operator
`GetParamsClassGmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateClassGmm`,
`ReadClassGmm`

## Possible Successors

`AddSampleClassGmm`,
`TrainClassGmm`

## See also

`EvaluateClassGmm`,
`ClassifyClassGmm`

## Module

Foundation
