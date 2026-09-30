# points_to_pluecker_line (Operator)

## Name

`points_to_pluecker_line` — Convert a 3D line given by two points to Plücker coordinates.

## Signature

`def points_to_pluecker_line(point_1x: MaybeSequence[float], point_1y: MaybeSequence[float], point_1z: MaybeSequence[float], point_2x: MaybeSequence[float], point_2y: MaybeSequence[float], point_2z: MaybeSequence[float]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def points_to_pluecker_line_s(point_1x: MaybeSequence[float], point_1y: MaybeSequence[float], point_1z: MaybeSequence[float], point_2x: MaybeSequence[float], point_2y: MaybeSequence[float], point_2z: MaybeSequence[float]) -> Tuple[float, float, float, float, float, float]`

## Description

`points_to_pluecker_line` converts the 3D line given by the
two points (*`point_1x`*, *`point_1y`*, *`point_1z`*)
and (*`point_2x`*, *`point_2y`*, *`point_2z`*) to
Plücker coordinates $\mathbf{L}=$
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*)
and $\mathbf{M}=$
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{P}$ denote the first point
(*`point_1x`*, *`point_1y`*, *`point_1z`*)
and $\mathbf{Q}$ the second point
(*`point_2x`*, *`point_2y`*, *`point_2z`*) on the line.
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

**`point_1x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X coordinates of the first point on the line.

**`point_1y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y coordinates of the first point on the line.

**`point_1z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z coordinates of the first point on the line.

**`point_2x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X coordinates of the second point on the line.

**`point_2y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y coordinates of the second point on the line.

**`point_2z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z coordinates of the second point on the line.

**`line_direction_x`** (output_control)  point3d.x(-array) `→` Sequence[float]

X component of the direction vector of the line.

**`line_direction_y`** (output_control)  point3d.y(-array) `→` Sequence[float]

Y component of the direction vector of the line.

**`line_direction_z`** (output_control)  point3d.z(-array) `→` Sequence[float]

Z component of the direction vector of the line.

**`line_moment_x`** (output_control)  point3d.x(-array) `→` Sequence[float]

X component of the moment vector of the line.

**`line_moment_y`** (output_control)  point3d.y(-array) `→` Sequence[float]

Y component of the moment vector of the line.

**`line_moment_z`** (output_control)  point3d.z(-array) `→` Sequence[float]

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
