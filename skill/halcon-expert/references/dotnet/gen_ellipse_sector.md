# GenEllipseSector (Operator)

## Name

`GenEllipseSector` — Create an ellipse sector.

## Signature

`static void HOperatorSet.GenEllipseSector(out HObject ellipseSector, HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, HTuple startAngle, HTuple endAngle)`

`public HRegion(HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, HTuple startAngle, HTuple endAngle)`

`public HRegion(double row, double column, double phi, double radius1, double radius2, double startAngle, double endAngle)`

`void HRegion.GenEllipseSector(HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, HTuple startAngle, HTuple endAngle)`

`void HRegion.GenEllipseSector(double row, double column, double phi, double radius1, double radius2, double startAngle, double endAngle)`

## Description

The operator `GenEllipseSector` generates one or more ellipse
sectors with the center
(*`row`*, *`column`*), the orientation *`phi`*,
the half-radii *`radius1`* and *`radius2`*, and the start and end
angles *`startAngle`* and *`endAngle`*.
The angles are given in radians in mathematically positive direction.
An illustration showing this can be found in the reference of
[`GenCircleSector`](gen_circle_sector.md).
Note, *"rad(360)"* is equivalent to *0*.
As a consequence a sector with *`startAngle`* = *0* and
*`endAngle`* = *"rad(360)"* results in an empty region.
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

**`ellipseSector`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created ellipse(s).

**`row`** (input_control)  coordinates.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`column`** (input_control)  coordinates.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`phi`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of the longer radius (Radius1).

Default:
0.0

Suggested values:
-1.5707, -1.1781, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.1781, 1.5707

Value range:
`-1.570796
≤
phi
≤
1.570796` (lin)

Restriction:
`- pi / 2 <= Phi <= pi / 2`

**`radius1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`radius2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`startAngle`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Start angle of the sector.

Default:
0.0

Suggested values:
0.0, 0.785398, 1.5708, 2.35619, 3.14159, 3.92699, 4.71239, 5.49779, 6.28318

Value range:
`0
≤
startAngle
≤
6.28318` (lin)

**`endAngle`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

End angle of the sector.

Default:
3.14159

Suggested values:
0.0, 0.785398, 1.5708, 2.35619, 3.14159, 3.92699, 4.71239, 5.49779, 6.28318

Value range:
`0
≤
endAngle
≤
6.28318` (lin)

## Example (HDevelop)

```
read_image (Image, 'fabrik')
gen_ellipse_sector (EllipseSector, 200, 200, rad(30),\
                     150, 90, rad(45), rad(280))
reduce_domain (Image, EllipseSector, ImageReduced)
dev_clear_window ()
dev_display (ImageReduced)
```

## Complexity

Runtime complexity: O(*`radius1`* * 2)

Storage complexity (byte): O(*`radius1`* * 8)

## Result

If the parameter values are correct, the operator [`GenEllipse`](gen_ellipse.md)
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
`GenCircleSector`,
`GenRegionPolygonFilled`,
`DrawEllipse`,
`GenEllipse`

## See also

`DispEllipse`,
`SetShape`,
`SmallestCircle`,
`ReduceDomain`

## Module

Foundation
