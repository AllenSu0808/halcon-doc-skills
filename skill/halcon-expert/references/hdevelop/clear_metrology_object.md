# clear_metrology_object (Operator)

## Name

`clear_metrology_object` — Delete metrology objects and free the allocated memory.

## Signature

`clear_metrology_object( : : MetrologyHandle, Index : )`

## Description

`clear_metrology_object` deletes in a metrology
model metrology objects created, e.g, by
[`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md),
[`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md),
[`add_metrology_object_line_measure`](add_metrology_object_line_measure.md), or
[`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

All memory used by the
metrology objects is freed. The handle of the metrology model is
passed in *`MetrologyHandle`*. The index of the metrology
objects is passed in *`Index`*. If *`Index`* is set
to *'all'*, all metrology objects are deleted. After the
operator call the metrology objects are invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MetrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MetrologyHandle`** (input_control, state is modified)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Index`** (input_control)  integer(-array) `→`  (string / integer)

Index of the metrology objects.

Default:
'all'

Suggested values:
'all', 0, 1, 2

## Result

If the parameters are valid, the operator `clear_metrology_object`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Module

2D Metrology
