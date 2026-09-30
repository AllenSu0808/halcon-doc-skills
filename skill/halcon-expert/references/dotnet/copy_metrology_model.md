# CopyMetrologyModel (Operator)

## Name

`CopyMetrologyModel` — Copy a metrology model.

## Signature

`static void HOperatorSet.CopyMetrologyModel(HTuple metrologyHandle, HTuple index, out HTuple copiedMetrologyHandle)`

`int HMetrologyModel.CopyMetrologyModel(HTuple index)`

`int HMetrologyModel.CopyMetrologyModel(string index)`

## Description

`CopyMetrologyModel` creates a new metrology model and
copies the selected metrology objects of the input metrology model
to this new output metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The input metrology model is defined by a handle *`metrologyHandle`*.
The parameter *`index`* determines the metrology objects that are
copied. With *`index`* set to *"all"*, all metrology objects are
copied. The operator returns the handle *`copiedMetrologyHandle`* of
the new metrology model. It can be used to save memory space. Access to the
parameters of the metrology objects is possible, e.g., with the operator
[`GetMetrologyObjectParam`](get_metrology_object_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`copiedMetrologyHandle`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Handle of the copied metrology model.

## Result

If the parameters are valid, the operator
`CopyMetrologyModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Module

2D Metrology
