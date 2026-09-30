# write_variation_model (Operator)

## Name

`write_variation_model` — Write a variation model to a file.

## Signature

`write_variation_model( : : ModelID, FileName : )`

## Description

`write_variation_model` writes a variation model to the file
*`FileName`*. The model can be read with
[`read_variation_model`](read_variation_model.md). The default HALCON file extension for a
variation model is 'vam'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  variation_model `→`  (handle)

ID of the variation model.

**`FileName`** (input_control)  filename.write `→`  (string)

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
