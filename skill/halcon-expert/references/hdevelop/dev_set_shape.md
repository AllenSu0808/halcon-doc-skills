# dev_set_shape (Operator)

## Name

`dev_set_shape` — Define the region output shape.

## Signature

`dev_set_shape( : : Shape : )`

## Description

`dev_set_shape` defines the shape that is used for displaying regions.
The available shapes can be queried with [`query_shape`](query_shape.md).

These shapes are supported:

- ***'original'*:** —

  The shape is displayed unchanged. Nevertheless
  modifications via parameters like
  [`dev_set_line_width`](dev_set_line_width.md) can take place.
  This is also true for all other modes.
- ***'outer_circle'*:** —

  Each region is displayed by the smallest surrounding
  circle. (See [`smallest_circle`](smallest_circle.md).)
- ***'inner_circle'*:** —

  Each region is displayed by the largest included
  circle. (See [`inner_circle`](inner_circle.md).)
- ***'ellipse'*:** —

  Each region is displayed by an ellipse with the same
  moments and orientation (See [`elliptic_axis`](elliptic_axis.md).)
- ***'rectangle1'*:** —

  Each region is displayed by the smallest surrounding
  rectangle parallel to the coordinate axes. (See
  [`smallest_rectangle1`](smallest_rectangle1.md).)
- ***'rectangle2'*:** —

  Each region is displayed by the smallest surrounding
  rectangle. (See [`smallest_rectangle2`](smallest_rectangle2.md).)
- ***'convex'*:** —

  Each region is displayed by its convex hull (See
  [`shape_trans`](shape_trans.md).)
- ***'icon'*:** —

  Each region is displayed by the icon set with
  [`set_icon`](set_icon.md) in the center of gravity.

For more information see the description of the operator
[`set_shape`](set_shape.md).
However, in contrast to that operator the selected shape is also used for
all new graphics windows that are opened afterwards.

## Attention

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`Shape`** (input_control)  string `→`  (string)

Region output mode.

Default:
'original'

List of values:
'convex', 'ellipse', 'icon', 'inner_circle', 'original', 'outer_circle', 'rectangle1', 'rectangle2'

## Example (HDevelop)

```
read_image(Image,'monkey')
threshold(Image,Region,128,255)
connection(Region,Regions)
dev_set_shape('rectangle1')
dev_set_draw('margin')
dev_set_line_width(5)
dev_clear_window()
dev_display(Regions)
```

## Result

If the values of the specified parameters are correct,
`dev_set_shape` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`,
`dev_set_color`

## See also

`set_shape`,
`dev_set_line_width`

## Module

Foundation
