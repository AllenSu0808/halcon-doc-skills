# move_rectangle (Operator)

## Name

`move_rectangle` — Copy inside an output window.

## Warning

**`move_rectangle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`move_rectangle( : : WindowHandle, Row1, Column1, Row2, Column2, DestRow, DestColumn : )`

## Description

`move_rectangle` copies all entries in the rectangle
(*`Row1`*,*`Column1`*), (*`Row2`*,*`Column2`*)
of the output window to a new position inside the same window.
This position is determined by the upper left corner (*`DestRow`*,
*`DestColumn`*).
Regions of the window, which are “uncovered” through moving the rectangle,
are set to the color of the background.

If you want to move several rectangles at once, you may pass parameters
in form of tuples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1`** (input_control)  rectangle.origin.y(-array) `→`  (integer)

Row index of upper left corner of the source rectangle.

Default:
0

Value range:
`0
≤
Row1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column1`** (input_control)  rectangle.origin.x(-array) `→`  (integer)

Column index of upper left corner of the source rectangle.

Default:
0

Value range:
`0
≤
Column1
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Row2`** (input_control)  rectangle.corner.y(-array) `→`  (integer)

Row index of lower right corner of the source rectangle.

Default:
64

Value range:
`0
≤
Row2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column2`** (input_control)  rectangle.corner.x(-array) `→`  (integer)

Column index of lower right corner of the source rectangle.

Default:
64

Value range:
`0
≤
Column2
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`DestRow`** (input_control)  point.y(-array) `→`  (integer)

Row index of upper left corner of the target position.

Default:
64

Value range:
`0
≤
DestRow
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`DestColumn`** (input_control)  point.x(-array) `→`  (integer)

Column index of upper left corner of the target position.

Default:
64

Value range:
`0
≤
DestColumn
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
`move_rectangle` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`

## Alternatives

`copy_rectangle`

## See also

`open_window`

## Module

Foundation
