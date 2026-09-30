# ReadDeepOcr (Operator)

## Name

`ReadDeepOcr` — Read a Deep OCR model from a file.

## Signature

`static void HOperatorSet.ReadDeepOcr(HTuple fileName, out HTuple deepOcrHandle)`

`public HDlModelOcr(string fileName)`

`void HDlModelOcr.ReadDeepOcr(string fileName)`

## Description

The operator `ReadDeepOcr` reads a Deep OCR model.
Such models have to be in the HALCON format.
As a result, the handle *`deepOcrHandle`* is returned.

The model is loaded from the file *`fileName`*.
This file is thereby searched in the directory `$HALCONROOT/dl/`
as well as in the currently used directory.
The default HALCON file extension for Deep OCR models is
`'.hdo'`.

Please note that the values of runtime specific parameters are not written
to file, see [`WriteDeepOcr`](write_deep_ocr.md).
As a consequence when reading a model these parameters are initialized with
their default value, see [`GetDeepOcrParam`](get_deep_ocr_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`hdo`

**`deepOcrHandle`** (output_control)  deep_ocr `→` [HDlModelOcr](HDlModelOcr.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep OCR model.

## Result

If the parameters are valid, the operator `ReadDeepOcr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeepOcr`

## Possible Successors

`SetDeepOcrParam`,
`GetDeepOcrParam`,
`ApplyDeepOcr`

## Alternatives

`CreateDeepOcr`

## Module

OCR/OCV
