# pluecker_line_to_points (Operator)

## Name

`pluecker_line_to_points` — Convert a 3D line given by Plücker coordinates to a 3D line given by
two points.

## Signature

`def pluecker_line_to_points(line_direction_x: MaybeSequence[float], line_direction_y: MaybeSequence[float], line_direction_z: MaybeSequence[float], line_moment_x: MaybeSequence[float], line_moment_y: MaybeSequence[float], line_moment_z: MaybeSequence[float]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def pluecker_line_to_points_s(line_direction_x: MaybeSequence[float], line_direction_y: MaybeSequence[float], line_direction_z: MaybeSequence[float], line_moment_x: MaybeSequence[float], line_moment_y: MaybeSequence[float], line_moment_z: MaybeSequence[float]) -> Tuple[float, float, float, float, float, float]`

## Description

`pluecker_line_to_points` converts a 3D line given by Plücker
coordinates $\mathbf{L}$
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*)
and $\mathbf{M}$
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*).
to a line given by two points on the line
(*`point_1x`*, *`point_1y`*, *`point_1z`*) and
(*`point_2x`*, *`point_2y`*, *`point_2z`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{L}$ denote the line direction
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*),
$\mathbf{M}$ the line moment
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*),
$\mathbf{P}$ the first point
(*`point_1x`*, *`point_1y`*, *`point_1z`*) on the line, and
$\mathbf{Q}$ the second point
(*`point_2x`*, *`point_2y`*, *`point_2z`*) on the line.
Then, $\mathbf{P}=\mathbf{L}\times\mathbf{M}$ and
$\mathbf{Q}=\mathbf{P}+\mathbf{L}$.
Note that $\mathbf{P}$ is the point on the line closest to the origin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`line_direction_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X component of the direction vector of the line.

**`line_direction_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y component of the direction vector of the line.

**`line_direction_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z component of the direction vector of the line.

**`line_moment_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X component of the moment vector of the line.

**`line_moment_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y component of the moment vector of the line.

**`line_moment_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z component of the moment vector of the line.

**`point_1x`** (output_control)  point3d.x(-array) `→` Sequence[float]

X coordinate of the first point on the line.

**`point_1y`** (output_control)  point3d.y(-array) `→` Sequence[float]

Y coordinate of the first point on the line.

**`point_1z`** (output_control)  point3d.z(-array) `→` Sequence[float]

Z coordinate of the first point on the line.

**`point_2x`** (output_control)  point3d.x(-array) `→` Sequence[float]

X coordinate of the second point on the line.

**`point_2y`** (output_control)  point3d.y(-array) `→` Sequence[float]

Y coordinate of the second point on the line.

**`point_2z`** (output_control)  point3d.z(-array) `→` Sequence[float]

Z coordinate of the second point on the line.

## Possible Successors

`distance_point_line`

## Alternatives

`pluecker_line_to_point_direction`

## See also

`points_to_pluecker_line`

## Module

Foundation
