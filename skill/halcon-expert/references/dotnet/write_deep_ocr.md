# WriteDeepOcr (Operator)

## Name

`WriteDeepOcr` — Write a Deep OCR model in a file.

## Signature

`static void HOperatorSet.WriteDeepOcr(HTuple deepOcrHandle, HTuple fileName)`

`void HDlModelOcr.WriteDeepOcr(string fileName)`

## Description

`WriteDeepOcr` writes the Deep OCR model
*`deepOcrHandle`* to the file given by *`fileName`*.
Please note that the runtime specific parameters *"gpu"*,
*"runtime"*, and *"runtime_init"* are not written.

The default HALCON file extension for Deep OCR models is
`'.hdo'`.

The Deep OCR model can be read with [`ReadDeepOcr`](read_deep_ocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deepOcrHandle`** (input_control)  deep_ocr `→` [HDlModelOcr](HDlModelOcr.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep OCR model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`hdo`

## Result

If the parameters are valid, the operator `WriteDeepOcr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeepOcr`,
`SetDeepOcrParam`

## Possible Successors

`ClearHandle`

## Module

OCR/OCV
