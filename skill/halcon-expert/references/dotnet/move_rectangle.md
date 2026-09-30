# MoveRectangle (Operator)

## Name

`MoveRectangle` — Copy inside an output window.

## Warning

**`MoveRectangle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.MoveRectangle(HTuple windowHandle, HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple destRow, HTuple destColumn)`

`void HWindow.MoveRectangle(HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple destRow, HTuple destColumn)`

`void HWindow.MoveRectangle(int row1, int column1, int row2, int column2, int destRow, int destColumn)`

## Description

`MoveRectangle` copies all entries in the rectangle
(*`row1`*,*`column1`*), (*`row2`*,*`column2`*)
of the output window to a new position inside the same window.
This position is determined by the upper left corner (*`destRow`*,
*`destColumn`*).
Regions of the window, which are “uncovered” through moving the rectangle,
are set to the color of the background.

If you want to move several rectangles at once, you may pass parameters
in form of tuples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row1`** (input_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of upper left corner of the source rectangle.

Default:
0

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

Column index of upper left corner of the source rectangle.

Default:
0

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

Row index of lower right corner of the source rectangle.

Default:
64

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

**`column2`** (input_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of lower right corner of the source rectangle.

Default:
64

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

**`destRow`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of upper left corner of the target position.

Default:
64

Value range:
`0
≤
destRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`destColumn`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner of the target position.

Default:
64

Value range:
`0
≤
destColumn
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Example (HDevelop)

```
* "Interactive" copy of a rectangle in the same window
draw_rectangle1(WindowHandle,L1,C1,L2,C2)
get_mbutton(WindowHandle,LN,CN,Button)
move_rectangle(WindowHandle,L1,C1,L2,C2,LN,CN)
```

## Result

If the window is valid and the specified parameters are correct
`MoveRectangle` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`OpenWindow`

## Alternatives

`CopyRectangle`

## See also

`OpenWindow`

## Module

Foundation
