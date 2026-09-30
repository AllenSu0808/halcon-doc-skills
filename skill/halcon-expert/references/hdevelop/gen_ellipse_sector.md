# gen_ellipse_sector (Operator)

## Name

`gen_ellipse_sector` — Create an ellipse sector.

## Signature

`gen_ellipse_sector( : EllipseSector : Row, Column, Phi, Radius1, Radius2, StartAngle, EndAngle : )`

## Description

The operator `gen_ellipse_sector` generates one or more ellipse
sectors with the center
(*`Row`*, *`Column`*), the orientation *`Phi`*,
the half-radii *`Radius1`* and *`Radius2`*, and the start and end
angles *`StartAngle`* and *`EndAngle`*.
The angles are given in radians in mathematically positive direction.
An illustration showing this can be found in the reference of
[`gen_circle_sector`](gen_circle_sector.md).
Note, *'rad(360)'* is equivalent to *0*.
As a consequence a sector with *`StartAngle`* = *0* and
*`EndAngle`* = *'rad(360)'* results in an empty region.
More than one region can be created by
passing tuples of parameter values.

The center must be located within the image coordinates.
The coordinate system runs from (0,0) (upper left corner) to
(Width-1,Height-1). See [`get_system`](get_system.md)
and [`reset_obj_db`](reset_obj_db.md) in this context.
If the ellipse reaches beyond the edge of the image it is clipped
to the current image format according to the value of
the system flag *'clip_region'* ([`set_system`](set_system.md)).

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

**`EllipseSector`** (output_object)  region(-array) `→` object

Created ellipse(s).

**`Row`** (input_control)  coordinates.y(-array) `→`  (real / integer)

Line index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`Row` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Column`** (input_control)  coordinates.x(-array) `→`  (real / integer)

Column index of center.

Default:
200.0

Suggested values:
0.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`Column` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Phi`** (input_control)  angle.rad(-array) `→`  (real / integer)

Orientation of the longer radius (Radius1).

Default:
0.0

Suggested values:
-1.5707, -1.1781, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.1781, 1.5707

Value range:
`-1.570796
≤
Phi
≤
1.570796` (lin)

Restriction:
`- pi / 2 <= Phi <= pi / 2`

**`Radius1`** (input_control)  number(-array) `→`  (real / integer)

Longer radius.

Default:
100.0

Suggested values:
2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`Radius1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`Radius1 > 0`

**`Radius2`** (input_control)  number(-array) `→`  (real / integer)

Shorter radius.

Default:
60.0

Suggested values:
1.0, 2.0, 4.0, 5.0, 10.0, 20.0, 50.0, 100.0, 256.0, 300.0, 400.0

Value range:
`Radius2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`Radius2 > 0`

**`StartAngle`** (input_control)  angle.rad(-array) `→`  (real / integer)

Start angle of the sector.

Default:
0.0

Suggested values:
0.0, 0.785398, 1.5708, 2.35619, 3.14159, 3.92699, 4.71239, 5.49779, 6.28318

Value range:
`0
≤
StartAngle
≤
6.28318` (lin)

**`EndAngle`** (input_control)  angle.rad(-array) `→`  (real / integer)

End angle of the sector.

Default:
3.14159

Suggested values:
0.0, 0.785398, 1.5708, 2.35619, 3.14159, 3.92699, 4.71239, 5.49779, 6.28318

Value range:
`0
≤
EndAngle
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

Runtime complexity: O(*`Radius1`* * 2)

Storage complexity (byte): O(*`Radius1`* * 8)

## Result

If the parameter values are correct, the operator [`gen_ellipse`](gen_ellipse.md)
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.
The clipping according to the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.

## Possible Successors

`paint_region`,
`reduce_domain`

## Alternatives

`gen_circle`,
`gen_circle_sector`,
`gen_region_polygon_filled`,
`draw_ellipse`,
`gen_ellipse`

## See also

`disp_ellipse`,
`set_shape`,
`smallest_circle`,
`reduce_domain`

## Module

Foundation
