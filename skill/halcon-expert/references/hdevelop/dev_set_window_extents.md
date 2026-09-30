# dev_set_window_extents (Operator)

## Name

`dev_set_window_extents` — Change position and size of the active floating graphics window.

## Signature

`dev_set_window_extents( : : Row, Column, Width, Height : )`

## Description

`dev_set_window_extents` changes the position and/or the size
of the currently active floating graphics window.

The parameters *`Row`* and *`Column`* specify the new
position (upper left corner) of the window.
Note that the offset values specified under
`Edit` -> `Preferences` ->
`General Options` -> `General Options`
-> `Window open offset` are added to the row and
the column index, respectively. For more information, see the chapter
“Menu `Edit`” in the `“HDevelop User's Guide”`.
Negative coordinates of the position are ignored, i.e., in this
direction the window will not be moved.

The parameters *`Width`* and *`Height`* specify the new size of
the window.
This is the size of the inner part that actually displays the iconic
objects.
If one of the two values is negative, this dimension will remain unchanged.

## Attention

This operator only works for single floating graphics windows, i.e.,
graphics windows that are neither docked nor tabbed.

Never use [`set_window_extents`](set_window_extents.md) to change the size and position
of an HDevelop graphics window. The operator
`dev_set_window_extents` has to be used instead.

Using the code export feature of HDevelop, the code that is generated
for this operator may have a different behavior than the related
HALCON operator.
For a detailed description of the code export of HDevelop graphics
operators into the different programming languages see in the
`“HDevelop User's Guide”` the chapter `Code Export`
-> `General Aspects of Code Generation`
-> `Graphics Windows`.

## Parameters

**`Row`** (input_control)  rectangle.origin.y `→`  (integer)

Row index of upper left corner.

Default:
0

Minimum increment:
1

Recommended increment:
1

Restriction:
`Row >= 0 || Row == -1`

**`Column`** (input_control)  rectangle.origin.x `→`  (integer)

Column index of upper left corner.

Default:
0

Minimum increment:
1

Recommended increment:
1

Restriction:
`Column >= 0 || Column == -1`

**`Width`** (input_control)  rectangle.extent.x `→`  (integer)

Width of the window.

Default:
256

Minimum increment:
1

Recommended increment:
1

Restriction:
`Width > 0 || Width == -1`

**`Height`** (input_control)  rectangle.extent.y `→`  (integer)

Height of the window.

Default:
256

Minimum increment:
1

Recommended increment:
1

Restriction:
`Height > 0 || Height == -1`

## Example (HDevelop)

```
dev_close_window ()
read_image (For5, 'for5')
get_image_size (For5, Width, Height)
dev_open_window (0, 0, Width, Height, 'black', WindowHandle)
dev_display (For5)
stop ()
dev_set_window_extents (-1,-1,Width/2,Height/2)
dev_display (For5)
stop ()
dev_set_window_extents (200,200,-1,-1)
```

## Result

If the values of the specified parameters are correct,
`dev_set_window_extents` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised and an error code returned.

## Possible Successors

`dev_display`,
`dev_set_lut`,
`dev_set_color`,
`dev_set_draw`,
`dev_set_part`

## See also

`set_window_extents`

## Module

Foundation
