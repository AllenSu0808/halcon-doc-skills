# pluecker_line_to_point_direction (Operator)

## Name

`pluecker_line_to_point_direction` — Convert a 3D line given by Plücker coordinates to a 3D line given by
a point and a direction.

## Signature

`pluecker_line_to_point_direction( : : LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentX, LineMomentY, LineMomentZ : PointX, PointY, PointZ, DirectionX, DirectionY, DirectionZ)`

## Description

`pluecker_line_to_point_direction` converts a 3D line given by
Plücker coordinates to a line given by a point on the line and the
direction of the line.
The line is given in Plücker coordinates
$\mathbf{L}$
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*)
and $\mathbf{M}$
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*).
The direction is given by
(*`DirectionX`*, *`DirectionY`*, *`DirectionZ`*) of the line.
and the point on the line by
(*`PointX`*, *`PointY`*, *`PointZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{L}$ denote the line direction
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*),
$\mathbf{M}$ the line moment
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*),
$\mathbf{P}$ the point
(*`PointX`*, *`PointY`*, *`PointZ`*) on the line, and
$\mathbf{D}$ the direction
(*`DirectionX`*, *`DirectionY`*, *`DirectionZ`*) of the line.
Then, $\mathbf{P}=\mathbf{L}\times\mathbf{M}$ and
$\mathbf{D}=\mathbf{L}$.
Note that $\mathbf{P}$ is the point on the line closest to the origin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`LineDirectionX`** (input_control)  point3d.x(-array) `→`  (real)

X component of the direction vector of the line.

**`LineDirectionY`** (input_control)  point3d.y(-array) `→`  (real)

Y component of the direction vector of the line.

**`LineDirectionZ`** (input_control)  point3d.z(-array) `→`  (real)

Z component of the direction vector of the line.

**`LineMomentX`** (input_control)  point3d.x(-array) `→`  (real)

X component of the moment vector of the line.

**`LineMomentY`** (input_control)  point3d.y(-array) `→`  (real)

Y component of the moment vector of the line.

**`LineMomentZ`** (input_control)  point3d.z(-array) `→`  (real)

Z component of the moment vector of the line.

**`PointX`** (output_control)  point3d.x(-array) `→`  (real)

X coordinate of the first point on the line.

**`PointY`** (output_control)  point3d.y(-array) `→`  (real)

Y coordinate of the first point on the line.

**`PointZ`** (output_control)  point3d.z(-array) `→`  (real)

Z coordinate of the first point on the line.

**`DirectionX`** (output_control)  point3d.x(-array) `→`  (real)

X coordinates of the direction of the line.

**`DirectionY`** (output_control)  point3d.y(-array) `→`  (real)

Y coordinates of the direction of the line.

**`DirectionZ`** (output_control)  point3d.z(-array) `→`  (real)

Z coordinates of the direction of the line.

## Alternatives

`pluecker_line_to_points`

## See also

`point_direction_to_pluecker_line`

## Module

Foundation
