# write_deep_ocr (Operator)

## Name

`write_deep_ocr` — Write a Deep OCR model in a file.

## Signature

`write_deep_ocr( : : DeepOcrHandle, FileName : )`

## Description

`write_deep_ocr` writes the Deep OCR model
*`DeepOcrHandle`* to the file given by *`FileName`*.
Please note that the runtime specific parameters *'gpu'*,
*'runtime'*, and *'runtime_init'* are not written.

The default HALCON file extension for Deep OCR models is
`'.hdo'`.

The Deep OCR model can be read with [`read_deep_ocr`](read_deep_ocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DeepOcrHandle`** (input_control)  deep_ocr `→`  (handle)

Handle of the Deep OCR model.

**`FileName`** (input_control)  filename.write `→`  (string)

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
