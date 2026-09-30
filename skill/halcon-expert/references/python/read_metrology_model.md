# read_metrology_model (Operator)

## Name

`read_metrology_model` — Read a metrology model from a file.

## Signature

`def read_metrology_model(file_name: str) -> HHandle`

## Description

`read_metrology_model` reads a metrology model, which has
been written to file with [`write_metrology_model`](write_metrology_model.md), from
the file *`file_name`*.
The default HALCON file extension for a metrology model is 'mtr'. The
values contained in the read metrology model are stored in a metrology model
with the handle *`metrology_handle`*. Access to the parameters of the
metrology model is possible, e.g., with the operator
[`get_metrology_object_param`](get_metrology_object_param.md) or
[`get_metrology_object_fuzzy_param`](get_metrology_object_fuzzy_param.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`mtr`

**`metrology_handle`** (output_control)  metrology_model `→` HHandle

Handle of the metrology model.

## Result

If the parameters are valid, the operator
`read_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`get_metrology_object_indices`,
`apply_metrology_model`

## See also

`write_metrology_model`

## Module

2D Metrology
