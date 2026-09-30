# set_drawing_object_xld (Operator)

## Name

`set_drawing_object_xld` — Set the contour of an interactive draw XLD.

## Signature

`def set_drawing_object_xld(contour: HObject, draw_id: HHandle) -> None`

## Description

`set_drawing_object_xld` substitutes the XLD currently contained in the draw
object by the new *`contour`*. The contour must contain at least two
points, so that the interaction as described in [`create_drawing_object_xld`](create_drawing_object_xld.md) is
possible.

In addition, if the drawing object *`draw_id`* is currently attached to a
HALCON window, the window will be redrawn with each call of `set_drawing_object_xld`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

XLD contour.

**`draw_id`** (input_control)  drawing_object `→` HHandle

Handle of the drawing object.

## Result

`set_drawing_object_xld` returns 2 (
H_MSG_TRUE)
if the *`draw_id`* is valid and
*`contour`* is a contour consisting of at least two points.
If necessary, an exception is raised.

## Possible Predecessors

`create_drawing_object_xld`

## Possible Successors

`attach_drawing_object_to_window`,
`clear_drawing_object`

## Alternatives

`create_drawing_object_xld`

## See also

`attach_drawing_object_to_window`

## Module

Foundation
