# ClearMetrologyObject (Operator)

## Name

`ClearMetrologyObject` — Delete metrology objects and free the allocated memory.

## Signature

`static void HOperatorSet.ClearMetrologyObject(HTuple metrologyHandle, HTuple index)`

`void HMetrologyModel.ClearMetrologyObject(HTuple index)`

`void HMetrologyModel.ClearMetrologyObject(string index)`

## Description

`ClearMetrologyObject` deletes in a metrology
model metrology objects created, e.g, by
[`AddMetrologyObjectCircleMeasure`](add_metrology_object_circle_measure.md),
[`AddMetrologyObjectEllipseMeasure`](add_metrology_object_ellipse_measure.md),
[`AddMetrologyObjectLineMeasure`](add_metrology_object_line_measure.md), or
[`AddMetrologyObjectRectangle2Measure`](add_metrology_object_rectangle2_measure.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

All memory used by the
metrology objects is freed. The handle of the metrology model is
passed in *`metrologyHandle`*. The index of the metrology
objects is passed in *`index`*. If *`index`* is set
to *"all"*, all metrology objects are deleted. After the
operator call the metrology objects are invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrologyHandle`** (input_control, state is modified)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Index of the metrology objects.

Default:
"all"

Suggested values:
"all", 0, 1, 2

## Result

If the parameters are valid, the operator `ClearMetrologyObject`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Module

2D Metrology
