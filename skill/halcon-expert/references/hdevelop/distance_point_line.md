# distance_point_line (Operator)

## Name

`distance_point_line` — Calculate the distance between a 3D point and a 3D line given by two
points on the line.

## Signature

`distance_point_line( : : PointX, PointY, PointZ, Point1X, Point1Y, Point1Z, Point2X, Point2Y, Point2Z : Distance)`

## Description

`distance_point_line` calculates the orthogonal distance
between 3D points and 3D lines. The lines are specified by two
points on the line ($\mathbf{Q}$ and $\mathbf{R}$).
The result is returned in *`Distance`*.
The input tuples can define 1 or n points.
The points are specified by
(*`PointX`*, *`PointY`*, *`PointZ`*).
The line is specified by two points on the line
(*`Point1X`*, *`Point1Y`*, *`Point1Z`*) and
(*`Point2X`*, *`Point2Y`*, *`Point2Z`*).

Let $\mathbf{P}$ denote the point
(*`PointX`*, *`PointY`*, *`PointZ`*),
$\mathbf{Q}$ the first point
(*`Point1X`*, *`Point1Y`*, *`Point1Z`*) on the line, and
$\mathbf{R}$ the second point
(*`Point2X`*, *`Point2Y`*, *`Point2Z`*) on the line.
First, the line direction
$\mathbf{V}=\mathbf{R}-\mathbf{Q}$ and
its length $\|\mathbf{V}\|$ are computed.
If $\|\mathbf{V}\|=0$, the points $\mathbf{Q}$ and
$\mathbf{R}$ do not define a line and an error is returned.
Furthermore, let $D$ denote the distance *`Distance`*. Then,
$D=\|(\mathbf{P}-\mathbf{Q})\times\mathbf{V}\|/\|\mathbf{V}\|$,
where $\times$ denotes the cross product of two vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PointX`** (input_control)  point3d.x(-array) `→`  (real)

X coordinate of the original points.

**`PointY`** (input_control)  point3d.y(-array) `→`  (real)

Y coordinate of the original points.

**`PointZ`** (input_control)  point3d.z(-array) `→`  (real)

Z coordinate of the original points.

**`Point1X`** (input_control)  point3d.x(-array) `→`  (real / integer)

X coordinate of the first point on the line.

**`Point1Y`** (input_control)  point3d.y(-array) `→`  (real / integer)

Y coordinate of the first point on the line.

**`Point1Z`** (input_control)  point3d.z(-array) `→`  (real / integer)

Z coordinate of the first point on the line.

**`Point2X`** (input_control)  point3d.x(-array) `→`  (real / integer)

X coordinate of the second point on the line.

**`Point2Y`** (input_control)  point3d.y(-array) `→`  (real / integer)

Y coordinate of the second point on the line.

**`Point2Z`** (input_control)  point3d.z(-array) `→`  (real / integer)

Z coordinate of the second point on the line.

**`Distance`** (output_control)  real(-array) `→`  (real)

Distance between the points and the lines.

## Possible Predecessors

`get_line_of_sight`

## Alternatives

`distance_point_pluecker_line`

## See also

`point_pluecker_line_to_hom_mat3d`

## Module

Foundation
