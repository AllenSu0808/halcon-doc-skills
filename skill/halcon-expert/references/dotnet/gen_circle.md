# GenCircle (Operator)

## Name

`GenCircle` — Create a circle.

## Signature

`static void HOperatorSet.GenCircle(out HObject circle, HTuple row, HTuple column, HTuple radius)`

`public HRegion(HTuple row, HTuple column, HTuple radius)`

`public HRegion(double row, double column, double radius)`

`void HRegion.GenCircle(HTuple row, HTuple column, HTuple radius)`

`void HRegion.GenCircle(double row, double column, double radius)`

## Description

The operator `GenCircle` generates one or more circles
described by the center and *`radius`*. If several circles
shall be generated the coordinates must be passed in the form of
tuples.

`GenCircle` only creates symmetric circles. To achieve this,
the radius is internally rounded down to a multiple of 0.5. If an
integer number is specified for the radius (i.e., 1, 2, 3, ...) an
even diameter is obtained, and hence the circle can only be
symmetric with respect to a center with coordinates that have a
fractional part of 0.5. Consequently, internally the coordinates of
the center are adapted to the closest coordinates that have a
fractional part of 0.5. Here, integer coordinates are rounded down
to the next smaller values with a fractional part of 0.5. For odd
diameters (i.e., radius = 1.5, 2.5, 3.5, ...), the circle can only
be symmetric with respect to a center with integer coordinates.
Hence, internally the coordinates of the center are rounded to the
nearest integer coordinates. It should be noted that the above
algorithm may lead to the fact that circles with an even diameter
are *not* contained in circles with the next larger odd
diameter, even if the coordinates specified in *`row`* and
*`column`* are identical.

If the circle extends beyond the image edge it is clipped to the
current image format if the value of the system flag *"clip_region"*
is set to *"true"* ([`SetSystem`](set_system.md)).

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Attention

For speed reasons, the resulting region may contain additional
pixels at the border and some individual pixels at the border may
be missing. This may lead to an inconsistency between the
operators [`SmallestCircle`](smallest_circle.md) and `GenCircle`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`circle`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Generated circle.

**`row`** (input_control)  circle.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Line index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 50.0, 100.0, 200.0, 300.0

Value range:
`row` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`column`** (input_control)  circle.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 50.0, 100.0, 200.0, 300.0

Value range:
`column` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`radius`** (input_control)  circle.radius(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of circle.

Default:
100.5

Suggested values:
1.0, 1.5, 2.0, 2.5, 3, 3.5, 4, 4.5, 5.5, 6.5, 7.5, 9.5, 11.5, 15.5, 20.5, 25.5, 31.5, 50.5

Value range:
`radius` (lin)

Restriction:
`Radius > 0.0`

## Example (HDevelop)

```
read_image(Image,'fabrik')
gen_circle(Circle,300.0,200.0,150.5)
reduce_domain(Image,Circle,Mask)
dev_clear_window ()
dev_display (Mask)
```

## Complexity

Runtime complexity: O(*`radius`* * 2)

Storage complexity (byte): O(*`radius`* * 8)

## Result

If the parameter values are correct,
the operator `GenCircle` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.
If an empty region is created by clipping (the circle is
completely outside of the image format) the operator
`set_system('store_empty_region',<'true'/'false'>)`
determines whether the empty region is put out.

## Possible Successors

`PaintRegion`,
`ReduceDomain`

## Alternatives

`GenEllipse`,
`GenRegionPolygonFilled`,
`GenRegionPoints`,
`GenRegionRuns`,
`DrawCircle`

## See also

`DispCircle`,
`SetShape`,
`SmallestCircle`,
`ReduceDomain`

## Module

Foundation
