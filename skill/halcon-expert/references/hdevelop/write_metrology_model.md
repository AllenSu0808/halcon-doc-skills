# write_metrology_model (Operator)

## Name

`write_metrology_model` — Write a metrology model to a file.

## Signature

`write_metrology_model( : : MetrologyHandle, FileName : )`

## Description

`write_metrology_model` writes a metrology model
to the file *`FileName`*. The metrology model
is defined by the handle *`MetrologyHandle`*. The metrology
model can be read with [`read_metrology_model`](read_metrology_model.md). The default
HALCON file extension for a metrology model is 'mtr'.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Attention

Note that only the input values are saved, i.e., no measure
regions and no results obtained by the operator
[`apply_metrology_model`](apply_metrology_model.md) are saved.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MetrologyHandle`** (input_control)  metrology_model `→`  (handle)

Handle of the metrology model.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`mtr`

## Result

If the parameters are valid, the operator
`write_metrology_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`apply_metrology_model`

## Possible Successors

`clear_metrology_model`

## See also

`read_metrology_model`

## Module

2D Metrology
