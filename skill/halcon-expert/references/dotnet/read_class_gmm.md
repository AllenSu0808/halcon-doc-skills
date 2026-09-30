# ReadClassGmm (Operator)

## Name

`ReadClassGmm` — Read a Gaussian Mixture Model from a file.

## Signature

`static void HOperatorSet.ReadClassGmm(HTuple fileName, out HTuple GMMHandle)`

`public HClassGmm(string fileName)`

`void HClassGmm.ReadClassGmm(string fileName)`

## Description

`ReadClassGmm` reads a Gaussian Mixture Model (GMM) that has
been stored with [`WriteClassGmm`](write_class_gmm.md). Since the training of an
GMM can consume a relatively long time, the GMM is typically trained
in an offline process and written to a file with
[`WriteClassGmm`](write_class_gmm.md). In the online process the GMM is read with
`ReadClassGmm` and subsequently used for evaluation with
[`EvaluateClassGmm`](evaluate_class_gmm.md) or for classification with
[`ClassifyClassGmm`](classify_class_gmm.md).
The default HALCON file extension for the GMM classifier is 'ggc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`ggc`

**`GMMHandle`** (output_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

## Result

If the parameters are valid, the operator `ReadClassGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Successors

`ClassifyClassGmm`,
`EvaluateClassGmm`,
`CreateClassLutGmm`

## See also

`CreateClassGmm`,
`WriteClassGmm`

## Module

Foundation
