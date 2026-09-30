# write_deep_ocr (Operator)

## Name

`write_deep_ocr` — Write a Deep OCR model in a file.

## Signature

`def write_deep_ocr(deep_ocr_handle: HHandle, file_name: str) -> None`

## Description

`write_deep_ocr` writes the Deep OCR model
*`deep_ocr_handle`* to the file given by *`file_name`*.
Please note that the runtime specific parameters *"gpu"*,
*"runtime"*, and *"runtime_init"* are not written.

The default HALCON file extension for Deep OCR models is
`'.hdo'`.

The Deep OCR model can be read with [`read_deep_ocr`](read_deep_ocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deep_ocr_handle`** (input_control)  deep_ocr `→` HHandle

Handle of the Deep OCR model.

**`file_name`** (input_control)  filename.write `→` str

Filename

File extension:
.`hdo`

## Result

If the parameters are valid, the operator `write_deep_ocr`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_deep_ocr`,
`set_deep_ocr_param`

## Possible Successors

`clear_handle`

## Module

OCR/OCV
