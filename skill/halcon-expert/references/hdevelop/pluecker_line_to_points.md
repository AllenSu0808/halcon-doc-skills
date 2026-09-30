# pluecker_line_to_points (Operator)

## Name

`pluecker_line_to_points` — Convert a 3D line given by Plücker coordinates to a 3D line given by
two points.

## Signature

`pluecker_line_to_points( : : LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentX, LineMomentY, LineMomentZ : Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z)`

## Description

`pluecker_line_to_points` converts a 3D line given by Plücker
coordinates $\mathbf{L}$
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*)
and $\mathbf{M}$
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*).
to a line given by two points on the line
(*`Point1X`*, *`Point1Y`*, *`Point1Z`*) and
(*`Point2X`*, *`Point2Y`*, *`Point2Z`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{L}$ denote the line direction
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*),
$\mathbf{M}$ the line moment
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*),
$\mathbf{P}$ the first point
(*`Point1X`*, *`Point1Y`*, *`Point1Z`*) on the line, and
$\mathbf{Q}$ the second point
(*`Point2X`*, *`Point2Y`*, *`Point2Z`*) on the line.
Then, $\mathbf{P}=\mathbf{L}\times\mathbf{M}$ and
$\mathbf{Q}=\mathbf{P}+\mathbf{L}$.
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

**`Point1X`** (output_control)  point3d.x(-array) `→`  (real)

X coordinate of the first point on the line.

**`Point1Y`** (output_control)  point3d.y(-array) `→`  (real)

Y coordinate of the first point on the line.

**`Point1Z`** (output_control)  point3d.z(-array) `→`  (real)

Z coordinate of the first point on the line.

**`Point2X`** (output_control)  point3d.x(-array) `→`  (real)

X coordinate of the second point on the line.

**`Point2Y`** (output_control)  point3d.y(-array) `→`  (real)

Y coordinate of the second point on the line.

**`Point2Z`** (output_control)  point3d.z(-array) `→`  (real)

Z coordinate of the second point on the line.

## Possible Successors

`distance_point_line`

## Alternatives

`pluecker_line_to_point_direction`

## See also

`points_to_pluecker_line`

## Module

Foundation
