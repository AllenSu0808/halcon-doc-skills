# GetDrawingObjectIconic (Operator)

## Name

`GetDrawingObjectIconic` — Return the iconic object of a drawing object.

## Signature

`static void HOperatorSet.GetDrawingObjectIconic(out HObject objectVal, HTuple drawID)`

`HObject HDrawingObject.GetDrawingObjectIconic()`

## Description

`GetDrawingObjectIconic` returns the iconic object *`objectVal`*
that corresponds to the drawing object *`drawID`*.
In addition, the parameters that define the drawing object can be queried
with the operator [`GetDrawingObjectParams`](get_drawing_object_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Copy of the iconic object represented by the drawing object.

**`drawID`** (input_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

[`ClearDrawingObject`](clear_drawing_object.md) returns 2 (
H_MSG_TRUE)
if the *`drawID`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectLine`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectXld`

## Possible Successors

`ReduceDomain`,
`GenRegionContourXld`,
`AttachDrawingObjectToWindow`

## Alternatives

`GetDrawingObjectParams`

## See also

`GetDrawingObjectParams`,
`AttachDrawingObjectToWindow`

## Module

Foundation
