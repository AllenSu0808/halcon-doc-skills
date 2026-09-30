# distance_point_pluecker_line (Operator)

## Name

`distance_point_pluecker_line` — Calculate the distance between a 3D point and a 3D line given by
Plücker coordinates.

## Signature

`def distance_point_pluecker_line(point_x: MaybeSequence[float], point_y: MaybeSequence[float], point_z: MaybeSequence[float], line_direction_x: MaybeSequence[Union[float, int]], line_direction_y: MaybeSequence[Union[float, int]], line_direction_z: MaybeSequence[Union[float, int]], line_moment_x: MaybeSequence[Union[float, int]], line_moment_y: MaybeSequence[Union[float, int]], line_moment_z: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def distance_point_pluecker_line_s(point_x: MaybeSequence[float], point_y: MaybeSequence[float], point_z: MaybeSequence[float], line_direction_x: MaybeSequence[Union[float, int]], line_direction_y: MaybeSequence[Union[float, int]], line_direction_z: MaybeSequence[Union[float, int]], line_moment_x: MaybeSequence[Union[float, int]], line_moment_y: MaybeSequence[Union[float, int]], line_moment_z: MaybeSequence[Union[float, int]]) -> float`

## Description

`distance_point_pluecker_line` calculates the orthogonal
distance between 3D points and 3D lines.
The result is returned in *`distance`*.
The input tuples can define 1 or n points $\mathbf{P}$
and lines, respectively.
The points are specified by
(*`point_x`*, *`point_y`*, *`point_z`*).
The lines are given in Plücker coordinates
$\mathbf{L}$
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*)
and $\mathbf{M}$
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

Let $\mathbf{P}$ denote the point
(*`point_x`*, *`point_y`*, *`point_z`*),
$\mathbf{L}$ the direction
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*),
and $\mathbf{M}$ the moment
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*)
of the Plücker line.
Furthermore, let $D$ denote the distance *`distance`*. Then,
$D=\|\mathbf{P}\times\mathbf{L}-\mathbf{M}\|$,
where $\times$ denotes the cross product of two vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`point_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X coordinates of the original points.

**`point_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y coordinates of the original points.

**`point_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z coordinates of the original points.

**`line_direction_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

X component of the direction vector of the corresponding
line.

**`line_direction_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Y component of the direction vector of the corresponding
line.

**`line_direction_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Z component of the direction vector of the corresponding
line.

**`line_moment_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

X component of the moment vector of the corresponding
line.

**`line_moment_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Y component of the moment vector of the corresponding
line.

**`line_moment_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Z component of the moment vector of the corresponding
line.

**`distance`** (output_control)  real(-array) `→` Sequence[float]

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
