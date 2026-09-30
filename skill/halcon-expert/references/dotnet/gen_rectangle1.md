# GenRectangle1 (Operator)

## Name

`GenRectangle1` — Create a rectangle parallel to the coordinate axes.

## Signature

`static void HOperatorSet.GenRectangle1(out HObject rectangle, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`public HRegion(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`public HRegion(double row1, double column1, double row2, double column2)`

`void HRegion.GenRectangle1(HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`void HRegion.GenRectangle1(double row1, double column1, double row2, double column2)`

## Description

The operator `GenRectangle1` generates one or more rectangles parallel
to the coordinate axes which are described by the upper left corner
(*`row1`*, *`column1`*) and the lower right corner
(*`row2`*, *`column2`*).
More than one region can be created by passing a tuple of corner points.
The coordinate system runs from (0,0) (upper left corner) to
(Width-1,Height-1). See [`GetSystem`](get_system.md)
and [`ResetObjDb`](reset_obj_db.md) in this context.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rectangle`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created rectangle.

**`row1`** (input_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Line of upper left corner point.

Default:
30.0

Suggested values:
0.0, 10.0, 20.0, 50.0, 100.0, 200.0

Value range:
`row1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`column1`** (input_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column of upper left corner point.

Default:
20.0

Suggested values:
0.0, 10.0, 20.0, 50.0, 100.0, 200.0

Value range:
`column1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`row2`** (input_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Line of lower right corner point.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 511.0

Value range:
`row2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`Row2 >= Row1`

**`column2`** (input_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column of lower right corner point.

Default:
200.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 511.0

Value range:
`column2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`Column2 >= Column1`

## Example (HDevelop)

```
* Contrast improvement in a rectangular region of interest
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
read_image(Image,'mreut')
dev_display (Image)
draw_rectangle1(WindowHandle,Row1,Column1,Row2,Column2)
gen_rectangle1(Rectangle,Row1,Column1,Row2,Column2)
reduce_domain(Image,Rectangle,Mask)
emphasize(Mask,Emphasize,9,9,1.0)
dev_display (Emphasize)
```

## Result

If the parameter values are correct, the operator `GenRectangle1`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`PaintRegion`,
`ReduceDomain`

## Alternatives

`GenRectangle2`,
`GenRegionPolygon`,
`FillUp`,
`GenRegionRuns`,
`GenRegionPoints`,
`GenRegionLine`

## See also

`DrawRectangle1`,
`ReduceDomain`,
`SmallestRectangle1`

## Module

Foundation
