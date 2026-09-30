# distance_point_line (Operator)

## Name

`distance_point_line` — Calculate the distance between a 3D point and a 3D line given by two
points on the line.

## Signature

`def distance_point_line(point_x: MaybeSequence[float], point_y: MaybeSequence[float], point_z: MaybeSequence[float], point_1x: MaybeSequence[Union[float, int]], point_1y: MaybeSequence[Union[float, int]], point_1z: MaybeSequence[Union[float, int]], point_2x: MaybeSequence[Union[float, int]], point_2y: MaybeSequence[Union[float, int]], point_2z: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def distance_point_line_s(point_x: MaybeSequence[float], point_y: MaybeSequence[float], point_z: MaybeSequence[float], point_1x: MaybeSequence[Union[float, int]], point_1y: MaybeSequence[Union[float, int]], point_1z: MaybeSequence[Union[float, int]], point_2x: MaybeSequence[Union[float, int]], point_2y: MaybeSequence[Union[float, int]], point_2z: MaybeSequence[Union[float, int]]) -> float`

## Description

`distance_point_line` calculates the orthogonal distance
between 3D points and 3D lines. The lines are specified by two
points on the line ($\mathbf{Q}$ and $\mathbf{R}$).
The result is returned in *`distance`*.
The input tuples can define 1 or n points.
The points are specified by
(*`point_x`*, *`point_y`*, *`point_z`*).
The line is specified by two points on the line
(*`point_1x`*, *`point_1y`*, *`point_1z`*) and
(*`point_2x`*, *`point_2y`*, *`point_2z`*).

Let $\mathbf{P}$ denote the point
(*`point_x`*, *`point_y`*, *`point_z`*),
$\mathbf{Q}$ the first point
(*`point_1x`*, *`point_1y`*, *`point_1z`*) on the line, and
$\mathbf{R}$ the second point
(*`point_2x`*, *`point_2y`*, *`point_2z`*) on the line.
First, the line direction
$\mathbf{V}=\mathbf{R}-\mathbf{Q}$ and
its length $\|\mathbf{V}\|$ are computed.
If $\|\mathbf{V}\|=0$, the points $\mathbf{Q}$ and
$\mathbf{R}$ do not define a line and an error is returned.
Furthermore, let $D$ denote the distance *`distance`*. Then,
$D=\|(\mathbf{P}-\mathbf{Q})\times\mathbf{V}\|/\|\mathbf{V}\|$,
where $\times$ denotes the cross product of two vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`point_x`** (input_control)  point3d.x(-array) `→` MaybeSequence[float]

X coordinate of the original points.

**`point_y`** (input_control)  point3d.y(-array) `→` MaybeSequence[float]

Y coordinate of the original points.

**`point_z`** (input_control)  point3d.z(-array) `→` MaybeSequence[float]

Z coordinate of the original points.

**`point_1x`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

X coordinate of the first point on the line.

**`point_1y`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Y coordinate of the first point on the line.

**`point_1z`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Z coordinate of the first point on the line.

**`point_2x`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

X coordinate of the second point on the line.

**`point_2y`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Y coordinate of the second point on the line.

**`point_2z`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Z coordinate of the second point on the line.

**`distance`** (output_control)  real(-array) `→` Sequence[float]

Distance between the points and the lines.

## Possible Predecessors

`get_line_of_sight`

## Alternatives

`distance_point_pluecker_line`

## See also

`point_pluecker_line_to_hom_mat3d`

## Module

Foundation
