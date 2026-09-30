# CopyMetrologyObject (Operator)

## Name

`CopyMetrologyObject` — Copy metrology metrology objects of a metrology model.

## Warning

**`CopyMetrologyObject` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.CopyMetrologyObject(HTuple metrologyHandle, HTuple index, out HTuple copiedIndices)`

`HTuple HMetrologyModel.CopyMetrologyObject(HTuple index)`

`int HMetrologyModel.CopyMetrologyObject(string index)`

## Description

`CopyMetrologyObject` copies metrology metrology objects
within this metrology model.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
parameter *`index`* determines the metrology objects that are copied.
With *`index`* set to *"all"*, all metrology objects are copied.
The operator `CopyMetrologyObject` returns the index of the new
created metrology objects in the parameter *`copiedIndices`*. The order
of the new metrology objects corresponds to the order of the original
metrology objects. Access to the parameters of the metrology objects of the
metrology model is possible, e.g., with the operator
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

**`copiedIndices`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the copied metrology objects.

## Result

If the parameters are valid, the operator
`CopyMetrologyObject` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Module

2D Metrology
