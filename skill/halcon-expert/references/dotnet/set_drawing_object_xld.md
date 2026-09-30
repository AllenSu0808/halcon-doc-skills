# SetDrawingObjectXld (Operator)

## Name

`SetDrawingObjectXld` — Set the contour of an interactive draw XLD.

## Signature

`static void HOperatorSet.SetDrawingObjectXld(HObject contour, HTuple drawID)`

`void HDrawingObject.SetDrawingObjectXld(HXLDCont contour)`

## Description

`SetDrawingObjectXld` substitutes the XLD currently contained in the draw
object by the new *`contour`*. The contour must contain at least two
points, so that the interaction as described in [`CreateDrawingObjectXld`](create_drawing_object_xld.md) is
possible.

In addition, if the drawing object *`drawID`* is currently attached to a
HALCON window, the window will be redrawn with each call of `SetDrawingObjectXld`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

XLD contour.

**`drawID`** (input_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

## Result

`SetDrawingObjectXld` returns 2 (
H_MSG_TRUE)
if the *`drawID`* is valid and
*`contour`* is a contour consisting of at least two points.
If necessary, an exception is raised.

## Possible Predecessors

`CreateDrawingObjectXld`

## Possible Successors

`AttachDrawingObjectToWindow`,
`ClearDrawingObject`

## Alternatives

`CreateDrawingObjectXld`

## See also

`AttachDrawingObjectToWindow`

## Module

Foundation
