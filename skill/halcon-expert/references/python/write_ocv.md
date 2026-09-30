# write_ocv (Operator)

## Name

`write_ocv` — Saving an OCV tool to file.

## Signature

`def write_ocv(ocvhandle: HHandle, file_name: str) -> None`

## Description

`write_ocv` writes an OCV tool to file.
This can be used to save the result of a training
([`traind_ocv_proj`](traind_ocv_proj.md)).
The whole information contained in the OCV tool is stored in the
file. The file can be reloaded afterwards using the operator
[`read_ocv`](read_ocv.md).

As file extension '.ocv' is used. If this extension is not
given with the file name, it will be added automatically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocvhandle`** (input_control)  ocv `→` HHandle

Handle of the OCV tool to be written.

**`file_name`** (input_control)  filename.write `→` str

Name of the file where the tool has to be saved.

Default:
"test_ocv"

File extension:
.`ocv`

## Result

`write_ocv` returns 2 (
H_MSG_TRUE)
, if
the data is correct and the file can be written.
Otherwise, an exception is raised.

## Possible Predecessors

`traind_ocv_proj`

## Possible Successors

`close_ocv`

## See also

`write_ocr`

## Module

OCR/OCV
