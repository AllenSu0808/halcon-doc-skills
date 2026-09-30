# dev_set_line_width (Operator)

## Name

`dev_set_line_width` — Define the line width for region contour output.

## Signature

`dev_set_line_width( : : LineWidth : )`

## Description

`dev_set_line_width` defines the line width (in pixel) that is used to
display region contours (in *'margin'* mode), XLDs, and other
geometric output (e.g., [`disp_region`](disp_region.md), [`disp_line`](disp_line.md), etc.).

For more information see the description of the operator
[`set_line_width`](set_line_width.md).
However, in contrast to that operator the new line width is also used for
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

**`LineWidth`** (input_control)  integer `→`  (integer)

Line width for region output in contour mode.

Default:
1

Restriction:
`LineWidth >= 1`

## Example (HDevelop)

```
read_image(Image,'monkey')
threshold(Image,Region,128,255)
dev_set_draw('margin')
dev_set_line_width(5)
dev_clear_window ()
dev_display(Region)
```

## Result

If the values of the specified parameters are correct,
`dev_set_line_width` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`

## See also

`set_line_width`,
`query_line_width`

## Module

Foundation
