# DispLut (Operator)

## Name

`DispLut` — Graphical view of the look-up-table (lut).

## Warning

**`DispLut` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.DispLut(HTuple windowHandle, HTuple row, HTuple column, HTuple scale)`

`void HWindow.DispLut(int row, int column, int scale)`

## Description

`DispLut` displays a graphical view of the look-up-table (lut)
in the valid window. A look-up-table defines the transformation of
image gray values to colors/gray levels on the screen. On most systems
this can be modified.
`DispLut` creates a graphical view of the table assigned to
the output window with the logical window number *`windowHandle`* and
displays it for every basic color
(red, green, blue).
*`row`* and *`column`* define the position of the center of
the graphic.
*`scale`* allows scaling of the graphic, whereby *1* means
displaying all 256 values, *2* means displaying 128 values, *3*
means displaying only 64 values, etc.
Tables for monochrome-representations are displayed in the currently set
color (see [`SetColor`](set_color.md), [`SetRgb`](set_rgb.md), etc.).
Tables for displaying “false colors” are viewed with red, green and blue
for each color component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row of center of the graphic.

Default:
128

Value range:
`0
≤
row
≤
511`

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column of center of the graphic.

Default:
128

Value range:
`0
≤
column
≤
511`

**`scale`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

`DispLut` returns 2 (
H_MSG_TRUE)
if the hardware supports a look-up-table,
the window is valid and the parameters are correct.
Otherwise an exception is raised.

## Possible Predecessors

`SetLut`

## See also

`OpenWindow`,
`SetLut`,
`SetFix`,
`SetPixel`,
`WriteLut`,
`GetLut`,
`SetColor`

## Module

Foundation
