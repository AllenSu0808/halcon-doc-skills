# GenEllipse (Operator)

## Name

`GenEllipse` — Create an ellipse.

## Signature

`static void HOperatorSet.GenEllipse(out HObject ellipse, HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2)`

`void HRegion.GenEllipse(HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2)`

`void HRegion.GenEllipse(double row, double column, double phi, double radius1, double radius2)`

## Description

The operator `GenEllipse` generates one or more ellipses with the
center
(*`row`*, *`column`*), the orientation *`phi`*
and the half-radii (half axes) *`radius1`* and *`radius2`*.
The angle is indicated in arc measure according to the x axis
in mathematically positive direction.
More than one region can be created by
passing tuples of parameter values.

The center must be located within the image coordinates.
The coordinate system runs from (0,0) (upper left corner) to
(Width-1,Height-1). See [`GetSystem`](get_system.md)
and [`ResetObjDb`](reset_obj_db.md) in this context.
If the ellipse reaches beyond the edge of the image it is clipped
to the current image format according to the value of
the system flag *"clip_region"* ([`SetSystem`](set_system.md)).

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

**`ellipse`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created ellipse(s).

**`row`** (input_control)  ellipse.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Line index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`row` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`column`** (input_control)  ellipse.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`column` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`phi`** (input_control)  ellipse.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of the longer radius (Radius1).

Default:
0.0

Suggested values:
-1.178097, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.178097

Value range:
`phi` (lin)

**`radius1`** (input_control)  ellipse.radius1(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Longer radius.

Default:
100.0

Suggested values:
2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`radius1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`Radius1 > 0`

**`radius2`** (input_control)  ellipse.radius2(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Shorter radius.

Default:
60.0

Suggested values:
1.0, 2.0, 4.0, 5.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`radius2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`Radius2 > 0`

## Example (HDevelop)

```
read_image (Image, 'fabrik')
gen_ellipse (Ellipse, 200, 200, rad(10), 160, 90)
reduce_domain (Image, Ellipse, ImageReduced)
dev_clear_window ()
dev_display (ImageReduced)
```

## Complexity

Runtime complexity: O(*`radius1`* * 2)

Storage complexity (byte): O(*`radius1`* * 8)

## Result

If the parameter values are correct, the operator `GenEllipse`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`PaintRegion`,
`ReduceDomain`

## Alternatives

`GenCircle`,
`GenRegionPolygonFilled`,
`DrawEllipse`

## See also

`DispEllipse`,
`SetShape`,
`SmallestCircle`,
`ReduceDomain`

## Module

Foundation
