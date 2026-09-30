# points_to_pluecker_line (Operator)

## Name

`points_to_pluecker_line` — Convert a 3D line given by two points to Plücker coordinates.

## Signature

`points_to_pluecker_line( : : Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z : LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentX, LineMomentY, LineMomentZ)`

## Description

`points_to_pluecker_line` converts the 3D line given by the
two points (*`Point1X`*, *`Point1Y`*, *`Point1Z`*)
and (*`Point2X`*, *`Point2Y`*, *`Point2Z`*) to
Plücker coordinates $\mathbf{L}=$
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*)
and $\mathbf{M}=$
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{P}$ denote the first point
(*`Point1X`*, *`Point1Y`*, *`Point1Z`*)
and $\mathbf{Q}$ the second point
(*`Point2X`*, *`Point2Y`*, *`Point2Z`*) on the line.
To compute the line direction $\mathbf{L}$, the
vector $\mathbf{D}=\mathbf{Q}-\mathbf{P}$ and
its length $\|\mathbf{D}\|$ are computed.
If $\|\mathbf{D}\|=0$, the points do not define a line
and an error is returned.
The line direction is given by
$\mathbf{L}=\mathbf{D}/\|\mathbf{D}\|$.
The line moment is given by the cross product
$\mathbf{M}=\mathbf{P}\times\mathbf{L}$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Point1X`** (input_control)  point3d.x(-array) `→`  (real)

X coordinates of the first point on the line.

**`Point1Y`** (input_control)  point3d.y(-array) `→`  (real)

Y coordinates of the first point on the line.

**`Point1Z`** (input_control)  point3d.z(-array) `→`  (real)

Z coordinates of the first point on the line.

**`Point2X`** (input_control)  point3d.x(-array) `→`  (real)

X coordinates of the second point on the line.

**`Point2Y`** (input_control)  point3d.y(-array) `→`  (real)

Y coordinates of the second point on the line.

**`Point2Z`** (input_control)  point3d.z(-array) `→`  (real)

Z coordinates of the second point on the line.

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

## Possible Predecessors

`get_line_of_sight`

## Possible Successors

`distance_point_pluecker_line`,
`point_pluecker_line_to_hom_mat3d`

## Alternatives

`point_direction_to_pluecker_line`

## See also

`pluecker_line_to_points`

## Module

Foundation
