# get_drawing_object_iconic (Operator)

## Name

`get_drawing_object_iconic` — Return the iconic object of a drawing object.

## Signature

`get_drawing_object_iconic( : Object : DrawID : )`

## Description

`get_drawing_object_iconic` returns the iconic object *`Object`*
that corresponds to the drawing object *`DrawID`*.
In addition, the parameters that define the drawing object can be queried
with the operator [`get_drawing_object_params`](get_drawing_object_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Object`** (output_object)  object(-array) `→` object

Copy of the iconic object represented by the drawing object.

**`DrawID`** (input_control)  drawing_object `→`  (handle)

Handle of the drawing object.

## Result

[`clear_drawing_object`](clear_drawing_object.md) returns 2 (
H_MSG_TRUE)
if the *`DrawID`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle`,
`create_drawing_object_line`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_circle_sector`,
`create_drawing_object_xld`

## Possible Successors

`reduce_domain`,
`gen_region_contour_xld`,
`attach_drawing_object_to_window`

## Alternatives

`get_drawing_object_params`

## See also

`get_drawing_object_params`,
`attach_drawing_object_to_window`

## Module

Foundation
