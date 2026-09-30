# disp_lut (Operator)

## Name

`disp_lut` — Graphical view of the look-up-table (lut).

## Warning

**`disp_lut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def disp_lut(window_handle: HHandle, row: int, column: int, scale: int) -> None`

## Description

`disp_lut` displays a graphical view of the look-up-table (lut)
in the valid window. A look-up-table defines the transformation of
image gray values to colors/gray levels on the screen. On most systems
this can be modified.
`disp_lut` creates a graphical view of the table assigned to
the output window with the logical window number *`window_handle`* and
displays it for every basic color
(red, green, blue).
*`row`* and *`column`* define the position of the center of
the graphic.
*`scale`* allows scaling of the graphic, whereby *1* means
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

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`row`** (input_control)  point.y `→` int

Row of center of the graphic.

Default:
128

Value range:
`0
≤
row
≤
511`

**`column`** (input_control)  point.x `→` int

Column of center of the graphic.

Default:
128

Value range:
`0
≤
column
≤
511`

**`scale`** (input_control)  integer `→` int

Scaling of the graphic.

Default:
1

List of values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Value range:
`0
≤
scale
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
