# clear_rectangle (Operator)

## Name

`clear_rectangle` — Delete a rectangle on the output window.

## Warning

**`clear_rectangle` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`clear_rectangle( : : WindowHandle, Row1, Column1, Row2, Column2 : )`

## Description

`clear_rectangle` deletes all entries in the rectangle which
is defined through the upper left corner
(*`Row1`*,*`Column1`*) and the lower right corner
(*`Row2`*,*`Column2`*). Deletion means that the
specified rectangle is set to the background color (see
[`open_window`](open_window.md)).

If you want to delete more than one rectangle, you may pass several
rectangles, i.e., the parameters *`Row1`*, *`Column1`*,
*`Row2`* and *`Column2`* are tuples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row1`** (input_control)  rectangle.origin.y(-array) `→`  (integer)

Line index of upper left corner.

Default:
10

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

Column index of upper left corner.

Default:
10

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

Row index of lower right corner.

Default:
118

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

Restriction:
`Row2 > Row1`

**`Column2`** (input_control)  rectangle.corner.x(-array) `→`  (integer)

Column index of lower right corner.

Default:
118

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

Restriction:
`Column2 >= Column1`

## Example (HDevelop)

```
* Erase a rectangle in the output window interactively:
draw_rectangle1(WindowHandle,L1,C1,L2,C2)
```

## Result

If an output window exists and the specified parameters are correct
`clear_rectangle` returns 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`open_window`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`,
`set_rgb`,
`set_hsi`,
`draw_rectangle1`

## Alternatives

`clear_window`,
`disp_rectangle1`

## See also

`open_window`

## Module

Foundation
