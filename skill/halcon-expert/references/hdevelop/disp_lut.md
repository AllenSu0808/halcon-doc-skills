# disp_lut (Operator)

## Name

`disp_lut` — Graphical view of the look-up-table (lut).

## Warning

**`disp_lut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`disp_lut( : : WindowHandle, Row, Column, Scale : )`

## Description

`disp_lut` displays a graphical view of the look-up-table (lut)
in the valid window. A look-up-table defines the transformation of
image gray values to colors/gray levels on the screen. On most systems
this can be modified.
`disp_lut` creates a graphical view of the table assigned to
the output window with the logical window number *`WindowHandle`* and
displays it for every basic color
(red, green, blue).
*`Row`* and *`Column`* define the position of the center of
the graphic.
*`Scale`* allows scaling of the graphic, whereby *1* means
displaying all 256 values, *2* means displaying 128 values, *3*
means displaying only 64 values, etc.
Tables for monochrome-representations are displayed in the currently set
color (see [`set_color`](set_color.md), [`set_rgb`](set_rgb.md), etc.).
Tables for displaying “false colors” are viewed with red, green and blue
for each color component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  point.y `→`  (integer)

Row of center of the graphic.

Default:
128

Value range:
`0
≤
Row
≤
511`

**`Column`** (input_control)  point.x `→`  (integer)

Column of center of the graphic.

Default:
128

Value range:
`0
≤
Column
≤
511`

**`Scale`** (input_control)  integer `→`  (integer)

Scaling of the graphic.

Default:
1

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Value range:
`0
≤
Scale
≤
20`

## Result

`disp_lut` returns 2 (
H_MSG_TRUE)
if the hardware supports a look-up-table,
the window is valid and the parameters are correct.
Otherwise an exception is raised.

## Possible Predecessors

`set_lut`

## See also

`open_window`,
`set_lut`,
`set_fix`,
`set_pixel`,
`write_lut`,
`get_lut`,
`set_color`

## Module

Foundation
