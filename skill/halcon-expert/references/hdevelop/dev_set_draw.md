# dev_set_draw (Operator)

## Name

`dev_set_draw` — Define the region fill mode.

## Signature

`dev_set_draw( : : DrawMode : )`

## Description

`dev_set_draw` defines the fill mode for regions.
If *`DrawMode`* is set to *'fill'*, regions are displayed
filled, if set to *'margin'*, only contours are displayed.
In the *'margin'* mode, the appearance of the contours can be
affected by [`dev_set_line_width`](dev_set_line_width.md) and [`set_line_style`](set_line_style.md).

For more information see the description of the operator [`set_draw`](set_draw.md).
However, in contrast to that operator the draw mode is also used for
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

**`DrawMode`** (input_control)  string `→`  (string)

Fill mode for region output.

Default:
'fill'

List of values:
'fill', 'margin'

## Example (HDevelop)

```
read_image(Image,'monkey')
threshold(Image,Region,128,255)
dev_clear_window ()
dev_set_color('red')
dev_set_draw('fill')
dev_display(Region)
dev_set_color('white')
dev_set_draw('margin')
dev_display(Region)
```

## Result

If the values of the specified parameters are correct,
`dev_set_draw` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_set_line_width`,
`dev_display`

## See also

`set_draw`

## Module

Foundation
