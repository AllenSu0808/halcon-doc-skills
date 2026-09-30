# clear_drawing_object (Operator)

## Name

`clear_drawing_object` — Delete drawing object.

## Signature

`clear_drawing_object( : : DrawID : )`

## Description

This operator deletes the drawing object *`DrawID`*.
The object is automatically detached from the windows to which it had been
previously attached. After calling `clear_drawing_object` the draw
object can no longer be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DrawID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DrawID`** (input_control, state is modified)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

`clear_drawing_object` returns 2 (
H_MSG_TRUE)
if the *`DrawID`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_xld`,
`create_drawing_object_line`,
`create_drawing_object_circle`,
`create_drawing_object_text`,
`detach_drawing_object_from_window`,
`attach_drawing_object_to_window`

## Possible Successors

`clear_window`,
`close_window`

## See also

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle_sector`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_xld`,
`create_drawing_object_line`,
`create_drawing_object_circle`,
`create_drawing_object_text`

## Module

Foundation
