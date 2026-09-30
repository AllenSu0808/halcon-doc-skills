# read_class_gmm (Operator)

## Name

`read_class_gmm` — Read a Gaussian Mixture Model from a file.

## Signature

`read_class_gmm( : : FileName : GMMHandle)`

## Description

`read_class_gmm` reads a Gaussian Mixture Model (GMM) that has
been stored with [`write_class_gmm`](write_class_gmm.md). Since the training of an
GMM can consume a relatively long time, the GMM is typically trained
in an offline process and written to a file with
[`write_class_gmm`](write_class_gmm.md). In the online process the GMM is read with
`read_class_gmm` and subsequently used for evaluation with
[`evaluate_class_gmm`](evaluate_class_gmm.md) or for classification with
[`classify_class_gmm`](classify_class_gmm.md).
The default HALCON file extension for the GMM classifier is 'ggc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`ggc`

**`GMMHandle`** (output_control)  class_gmm `→`  (handle)

GMM handle.

## Result

If the parameters are valid, the operator `read_class_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Successors

`classify_class_gmm`,
`evaluate_class_gmm`,
`create_class_lut_gmm`

## See also

`create_class_gmm`,
`write_class_gmm`

## Module

Foundation
