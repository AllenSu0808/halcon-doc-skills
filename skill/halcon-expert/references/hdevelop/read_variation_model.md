# read_variation_model (Operator)

## Name

`read_variation_model` — Read a variation model from a file.

## Signature

`read_variation_model( : : FileName : ModelID)`

## Description

The operator `read_variation_model` reads a variation model,
which has been written with [`write_variation_model`](write_variation_model.md), from the
file *`FileName`*.
The default HALCON file extension for a variation model is 'vam'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`vam`

**`ModelID`** (output_control)  variation_model `→`  (handle)

ID of the variation model.

## Result

If the file name is valid, the operator `read_variation_model`
returns 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`compare_variation_model`,
`compare_ext_variation_model`

## See also

`write_variation_model`

## Module

Matching
