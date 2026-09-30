# dev_set_part (Operator)

## Name

`dev_set_part` — Modify the displayed image part.

## Signature

`dev_set_part( : : Row1, Column1, Row2, Column2 : )`

## Description

`dev_set_part` is used to set the part of the image that is displayed
in the graphics window.
The parameters *`Row1`* and *`Column1`* specify the
upper left corner, *`Row2`* and *`Column2`* the lower
right corner of the image part to display.

For more information see the description of the operator
[`set_part`](set_part.md).
In addition, if *`Row1`* is larger than *`Row2`* or
*`Column1`* larger than *`Column2`*, the zooming in the particular
dimension will be reset to show the complete height and/or width of the image.
Please note that this is not possible with the operator [`set_part`](set_part.md)
outside HDevelop.

In addition, note that the part is automatically reset, if a new program is
loaded, a program reset is performed, or a new image with a different
image size is displayed.

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

**`Row1`** (input_control)  rectangle.origin.y `→`  (integer)

Row of the upper left corner of the
chosen image part.

Default:
0

**`Column1`** (input_control)  rectangle.origin.x `→`  (integer)

Column of the upper left corner of the
chosen image part.

Default:
0

**`Row2`** (input_control)  rectangle.corner.y `→`  (integer)

Row of the lower right corner of the
chosen image part.

Default:
128

**`Column2`** (input_control)  rectangle.corner.x `→`  (integer)

Column of the lower right corner of the
chosen image part.

Default:
128

## Example (HDevelop)

```
read_image (Image, 'fabrik')
for i := 1 to 240 by 10
  dev_set_part (i, i, 511-i, 511-i)
  dev_display (Image)
endfor
dev_set_part (1, 1, -1, -1)
dev_display (Image)
```

## Result

If the values of the specified parameters are correct,
`dev_set_part` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`

## See also

`set_part`

## Module

Foundation
