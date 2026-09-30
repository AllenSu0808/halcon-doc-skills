# write_variation_model (Operator)

## Name

`write_variation_model` — Write a variation model to a file.

## Signature

`def write_variation_model(model_id: HHandle, file_name: str) -> None`

## Description

`write_variation_model` writes a variation model to the file
*`file_name`*. The model can be read with
[`read_variation_model`](read_variation_model.md). The default HALCON file extension for a
variation model is 'vam'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  variation_model `→` HHandle

ID of the variation model.

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`vam`

## Result

If the file name is valid (write permission), the operator
`write_variation_model` returns 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`train_variation_model`

## See also

`read_variation_model`

## Module

Matching
