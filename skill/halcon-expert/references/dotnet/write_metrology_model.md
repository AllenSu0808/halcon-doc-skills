# WriteMetrologyModel (Operator)

## Name

`WriteMetrologyModel` — Write a metrology model to a file.

## Signature

`static void HOperatorSet.WriteMetrologyModel(HTuple metrologyHandle, HTuple fileName)`

`void HMetrologyModel.WriteMetrologyModel(string fileName)`

## Description

`WriteMetrologyModel` writes a metrology model
to the file *`fileName`*. The metrology model
is defined by the handle *`metrologyHandle`*. The metrology
model can be read with [`ReadMetrologyModel`](read_metrology_model.md). The default
HALCON file extension for a metrology model is 'mtr'.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Attention

Note that only the input values are saved, i.e., no measure
regions and no results obtained by the operator
[`ApplyMetrologyModel`](apply_metrology_model.md) are saved.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`mtr`

## Result

If the parameters are valid, the operator
`WriteMetrologyModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ApplyMetrologyModel`

## Possible Successors

`ClearMetrologyModel`

## See also

`ReadMetrologyModel`

## Module

2D Metrology
