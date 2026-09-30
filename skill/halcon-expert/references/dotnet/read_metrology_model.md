# ReadMetrologyModel (Operator)

## Name

`ReadMetrologyModel` — Read a metrology model from a file.

## Signature

`static void HOperatorSet.ReadMetrologyModel(HTuple fileName, out HTuple metrologyHandle)`

`public HMetrologyModel(string fileName)`

`void HMetrologyModel.ReadMetrologyModel(string fileName)`

## Description

`ReadMetrologyModel` reads a metrology model, which has
been written to file with [`WriteMetrologyModel`](write_metrology_model.md), from
the file *`fileName`*.
The default HALCON file extension for a metrology model is 'mtr'. The
values contained in the read metrology model are stored in a metrology model
with the handle *`metrologyHandle`*. Access to the parameters of the
metrology model is possible, e.g., with the operator
[`GetMetrologyObjectParam`](get_metrology_object_param.md) or
[`GetMetrologyObjectFuzzyParam`](get_metrology_object_fuzzy_param.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`mtr`

**`metrologyHandle`** (output_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

## Result

If the parameters are valid, the operator
`ReadMetrologyModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`GetMetrologyObjectIndices`,
`ApplyMetrologyModel`

## See also

`WriteMetrologyModel`

## Module

2D Metrology
