# WriteOcv (Operator)

## Name

`WriteOcv` — Saving an OCV tool to file.

## Signature

`static void HOperatorSet.WriteOcv(HTuple OCVHandle, HTuple fileName)`

`void HOCV.WriteOcv(string fileName)`

## Description

`WriteOcv` writes an OCV tool to file.
This can be used to save the result of a training
([`TraindOcvProj`](traind_ocv_proj.md)).
The whole information contained in the OCV tool is stored in the
file. The file can be reloaded afterwards using the operator
[`ReadOcv`](read_ocv.md).

As file extension '.ocv' is used. If this extension is not
given with the file name, it will be added automatically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCVHandle`** (input_control)  ocv `→` [HOCV](HOCV.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCV tool to be written.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file where the tool has to be saved.

Default:
"test_ocv"

File extension:
.`ocv`

## Result

`WriteOcv` returns 2 (
H_MSG_TRUE)
, if
the data is correct and the file can be written.
Otherwise, an exception is raised.

## Possible Predecessors

`TraindOcvProj`

## Possible Successors

`CloseOcv`

## See also

`WriteOcr`

## Module

OCR/OCV
