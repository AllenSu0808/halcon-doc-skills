# gen_circle (Operator)

## Name

`gen_circle` — Create a circle.

## Signature

`gen_circle( : Circle : Row, Column, Radius : )`

## Description

The operator `gen_circle` generates one or more circles
described by the center and *`Radius`*. If several circles
shall be generated the coordinates must be passed in the form of
tuples.

`gen_circle` only creates symmetric circles. To achieve this,
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
diameter, even if the coordinates specified in *`Row`* and
*`Column`* are identical.

If the circle extends beyond the image edge it is clipped to the
current image format if the value of the system flag *'clip_region'*
is set to *'true'* ([`set_system`](set_system.md)).

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
operators [`smallest_circle`](smallest_circle.md) and `gen_circle`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Circle`** (output_object)  region(-array) `→` object

Generated circle.

**`Row`** (input_control)  circle.center.y(-array) `→`  (real / integer)

Line index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 50.0, 100.0, 200.0, 300.0

Value range:
`Row` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Column`** (input_control)  circle.center.x(-array) `→`  (real / integer)

Column index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 50.0, 100.0, 200.0, 300.0

Value range:
`Column` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Radius`** (input_control)  circle.radius(-array) `→`  (real / integer)

Radius of circle.

Default:
100.5

Suggested values:
1.0, 1.5, 2.0, 2.5, 3, 3.5, 4, 4.5, 5.5, 6.5, 7.5, 9.5, 11.5, 15.5, 20.5, 25.5, 31.5, 50.5

Value range:
`Radius` (lin)

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

Runtime complexity: O(*`Radius`* * 2)

Storage complexity (byte): O(*`Radius`* * 8)

## Result

If the parameter values are correct,
the operator `gen_circle` returns the value 2 (
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

`paint_region`,
`reduce_domain`

## Alternatives

`gen_ellipse`,
`gen_region_polygon_filled`,
`gen_region_points`,
`gen_region_runs`,
`draw_circle`

## See also

`disp_circle`,
`set_shape`,
`smallest_circle`,
`reduce_domain`

## Module

Foundation
