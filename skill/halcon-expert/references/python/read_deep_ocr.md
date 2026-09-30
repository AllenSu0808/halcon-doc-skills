# read_deep_ocr (Operator)

## Name

`read_deep_ocr` — Read a Deep OCR model from a file.

## Signature

`def read_deep_ocr(file_name: str) -> HHandle`

## Description

The operator `read_deep_ocr` reads a Deep OCR model.
Such models have to be in the HALCON format.
As a result, the handle *`deep_ocr_handle`* is returned.

The model is loaded from the file *`file_name`*.
This file is thereby searched in the directory `$HALCONROOT/dl/`
as well as in the currently used directory.
The default HALCON file extension for Deep OCR models is
`'.hdo'`.

Please note that the values of runtime specific parameters are not written
to file, see [`write_deep_ocr`](write_deep_ocr.md).
As a consequence when reading a model these parameters are initialized with
their default value, see [`get_deep_ocr_param`](get_deep_ocr_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Filename

File extension:
.`hdo`

**`deep_ocr_handle`** (output_control)  deep_ocr `→` HHandle

Handle of the Deep OCR model.

## Result

If the parameters are valid, the operator `read_deep_ocr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_ocr`

## Possible Successors

`set_deep_ocr_param`,
`get_deep_ocr_param`,
`apply_deep_ocr`

## Alternatives

`create_deep_ocr`

## Module

OCR/OCV
