# distance_point_pluecker_line (Operator)

## Name

`distance_point_pluecker_line` — Calculate the distance between a 3D point and a 3D line given by
Plücker coordinates.

## Signature

`distance_point_pluecker_line( : : PointX, PointY, PointZ, LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentX, LineMomentY, LineMomentZ : Distance)`

## Description

`distance_point_pluecker_line` calculates the orthogonal
distance between 3D points and 3D lines.
The result is returned in *`Distance`*.
The input tuples can define 1 or n points $\mathbf{P}$
and lines, respectively.
The points are specified by
(*`PointX`*, *`PointY`*, *`PointZ`*).
The lines are given in Plücker coordinates
$\mathbf{L}$
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*)
and $\mathbf{M}$
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

Let $\mathbf{P}$ denote the point
(*`PointX`*, *`PointY`*, *`PointZ`*),
$\mathbf{L}$ the direction
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*),
and $\mathbf{M}$ the moment
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*)
of the Plücker line.
Furthermore, let $D$ denote the distance *`Distance`*. Then,
$D=\|\mathbf{P}\times\mathbf{L}-\mathbf{M}\|$,
where $\times$ denotes the cross product of two vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PointX`** (input_control)  point3d.x(-array) `→`  (real)

X coordinates of the original points.

**`PointY`** (input_control)  point3d.y(-array) `→`  (real)

Y coordinates of the original points.

**`PointZ`** (input_control)  point3d.z(-array) `→`  (real)

Z coordinates of the original points.

**`LineDirectionX`** (input_control)  point3d.x(-array) `→`  (real / integer)

X component of the direction vector of the corresponding
line.

**`LineDirectionY`** (input_control)  point3d.y(-array) `→`  (real / integer)

Y component of the direction vector of the corresponding
line.

**`LineDirectionZ`** (input_control)  point3d.z(-array) `→`  (real / integer)

Z component of the direction vector of the corresponding
line.

**`LineMomentX`** (input_control)  point3d.x(-array) `→`  (real / integer)

X component of the moment vector of the corresponding
line.

**`LineMomentY`** (input_control)  point3d.y(-array) `→`  (real / integer)

Y component of the moment vector of the corresponding
line.

**`LineMomentZ`** (input_control)  point3d.z(-array) `→`  (real / integer)

Z component of the moment vector of the corresponding
line.

**`Distance`** (output_control)  real(-array) `→`  (real)

Distance between the points and the lines.

## Possible Predecessors

`points_to_pluecker_line`,
`point_direction_to_pluecker_line`

## Alternatives

`distance_point_line`

## See also

`point_pluecker_line_to_hom_mat3d`

## Module

Foundation
