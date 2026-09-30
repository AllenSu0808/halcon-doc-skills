# point_direction_to_pluecker_line (Operator)

## Name

`point_direction_to_pluecker_line` — Convert a 3D line given by a point and a direction to Plücker
coordinates.

## Signature

`def point_direction_to_pluecker_line(point_x: MaybeSequence[float], point_y: MaybeSequence[float], point_z: MaybeSequence[float], direction_x: MaybeSequence[float], direction_y: MaybeSequence[float], direction_z: MaybeSequence[float]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def point_direction_to_pluecker_line_s(point_x: MaybeSequence[float], point_y: MaybeSequence[float], point_z: MaybeSequence[float], direction_x: MaybeSequence[float], direction_y: MaybeSequence[float], direction_z: MaybeSequence[float]) -> Tuple[float, float, float, float, float, float]`

## Description

`point_direction_to_pluecker_line` converts the 3D line given
by the point (*`point_x`*, *`point_y`*, *`point_z`*) and
the direction (*`direction_x`*, *`direction_y`*,
*`direction_z`*) to Plücker coordinates
$\mathbf{L}$
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*)
and $\mathbf{M}$
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{P}$ denote the point
(*`point_x`*, *`point_y`*, *`point_z`*)
and $\mathbf{D}$ the direction
(*`direction_x`*, *`direction_y`*, *`direction_z`*) of the line.
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

**`point_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X coordinates of the point on the line.

**`point_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y coordinates of the point on the line.

**`point_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z coordinates of the point on the line.

**`direction_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X coordinates of the direction of the line.

**`direction_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y coordinates of the direction of the line.

**`direction_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z coordinates of the direction of the line.

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

## Possible Successors

`distance_point_pluecker_line`,
`point_pluecker_line_to_hom_mat3d`

## Alternatives

`points_to_pluecker_line`

## See also

`pluecker_line_to_point_direction`

## Module

Foundation
