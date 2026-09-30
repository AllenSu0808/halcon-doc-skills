# point_direction_to_pluecker_line (Operator)

## Name

`point_direction_to_pluecker_line` — Convert a 3D line given by a point and a direction to Plücker
coordinates.

## Signature

`point_direction_to_pluecker_line( : : PointX, PointY, PointZ, DirectionX, DirectionY, DirectionZ : LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentX, LineMomentY, LineMomentZ)`

## Description

`point_direction_to_pluecker_line` converts the 3D line given
by the point (*`PointX`*, *`PointY`*, *`PointZ`*) and
the direction (*`DirectionX`*, *`DirectionY`*,
*`DirectionZ`*) to Plücker coordinates
$\mathbf{L}$
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*)
and $\mathbf{M}$
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{P}$ denote the point
(*`PointX`*, *`PointY`*, *`PointZ`*)
and $\mathbf{D}$ the direction
(*`DirectionX`*, *`DirectionY`*, *`DirectionZ`*) of the line.
To compute the line direction $\mathbf{L}$,
the length $\|\mathbf{D}\|$ of the vector $\mathbf{D}$
is computed.
If $\|\mathbf{D}\|=0$, the direction $\mathbf{D}$
does not define a line and an error is returned.
The further calculations to Plücker coordinates are given in
[`points_to_pluecker_line`](points_to_pluecker_line.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PointX`** (input_control)  point3d.x(-array) `→`  (real)

X coordinates of the point on the line.

**`PointY`** (input_control)  point3d.y(-array) `→`  (real)

Y coordinates of the point on the line.

**`PointZ`** (input_control)  point3d.z(-array) `→`  (real)

Z coordinates of the point on the line.

**`DirectionX`** (input_control)  point3d.x(-array) `→`  (real)

X coordinates of the direction of the line.

**`DirectionY`** (input_control)  point3d.y(-array) `→`  (real)

Y coordinates of the direction of the line.

**`DirectionZ`** (input_control)  point3d.z(-array) `→`  (real)

Z coordinates of the direction of the line.

**`LineDirectionX`** (output_control)  point3d.x(-array) `→`  (real)

X component of the direction vector of the line.

**`LineDirectionY`** (output_control)  point3d.y(-array) `→`  (real)

Y component of the direction vector of the line.

**`LineDirectionZ`** (output_control)  point3d.z(-array) `→`  (real)

Z component of the direction vector of the line.

**`LineMomentX`** (output_control)  point3d.x(-array) `→`  (real)

X component of the moment vector of the line.

**`LineMomentY`** (output_control)  point3d.y(-array) `→`  (real)

Y component of the moment vector of the line.

**`LineMomentZ`** (output_control)  point3d.z(-array) `→`  (real)

Z component of the moment vector of the line.

## Possible Successors

`distance_point_pluecker_line`,
`point_pluecker_line_to_hom_mat3d`

## Alternatives

`points_to_pluecker_line`

## See also

`pluecker_line_to_point_direction`

## Module

Foundation
