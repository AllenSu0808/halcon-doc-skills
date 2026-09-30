# ClearRectangle (Operator)

## Name

`ClearRectangle` — Delete a rectangle on the output window.

## Warning

**`ClearRectangle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.ClearRectangle(HTuple windowHandle, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.ClearRectangle(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HWindow.ClearRectangle(int row1, int column1, int row2, int column2)`

## Description

`ClearRectangle` deletes all entries in the rectangle which
is defined through the upper left corner
(*`row1`*,*`column1`*) and the lower right corner
(*`row2`*,*`column2`*). Deletion means that the
specified rectangle is set to the background color (see
[`OpenWindow`](open_window.md)).

If you want to delete more than one rectangle, you may pass several
rectangles, i.e., the parameters *`row1`*, *`column1`*,
*`row2`* and *`column2`* are tuples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (input_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index of upper left corner.

Default:
10

Value range:
`0
≤
row1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`column1`** (input_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner.

Default:
10

Value range:
`0
≤
column1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`row2`** (input_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of lower right corner.

Default:
118

Value range:
`0
≤
row2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Row2 > Row1`

**`column2`** (input_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of lower right corner.

Default:
118

Value range:
`0
≤
column2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`Column2 >= Column1`

## Example (HDevelop)

```
* Erase a rectangle in the output window interactively:
draw_rectangle1(WindowHandle,L1,C1,L2,C2)
```

## Result

If an output window exists and the specified parameters are correct
`ClearRectangle` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`,
`SetRgb`,
`SetHsi`,
`DrawRectangle1`

## Alternatives

`ClearWindow`,
`DispRectangle1`

## See also

`OpenWindow`

## Module

Foundation
