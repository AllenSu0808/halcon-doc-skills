# dev_set_paint (Operator)

## Name

`dev_set_paint` — Define the gray value output mode.

## Signature

`dev_set_paint( : : Mode : )`

## Description

`dev_set_paint` defines the output mode that is used for displaying
image objects in the graphics window.

For a detailed description of all possible options see [`set_paint`](set_paint.md).
However, in contrast to that operator the display mode is also used for
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

**`Mode`** (input_control)  string-array `→`  (string / integer)

Grayvalue output name. Additional parameters possible.

Default:
'default'

Suggested values:
'default', '3d_plot'

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_set_paint('3d_plot')
dev_display(Image)
```

## Result

If the values of the specified parameters are correct,
`dev_set_paint` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Predecessors

`dev_open_window`

## Possible Successors

`dev_set_color`,
`dev_display`

## See also

`set_paint`

## Module

Foundation
