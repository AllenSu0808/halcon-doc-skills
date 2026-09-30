# DistancePointLine (Operator)

## Name

`DistancePointLine` — Calculate the distance between a 3D point and a 3D line given by two
points on the line.

## Signature

`static void HOperatorSet.DistancePointLine(HTuple pointX, HTuple pointY, HTuple pointZ, HTuple point1X, HTuple point1Y, HTuple point1Z, HTuple point2X, HTuple point2Y, HTuple point2Z, out HTuple distance)`

`static HTuple HMisc.DistancePointLine(HTuple pointX, HTuple pointY, HTuple pointZ, HTuple point1X, HTuple point1Y, HTuple point1Z, HTuple point2X, HTuple point2Y, HTuple point2Z)`

`static double HMisc.DistancePointLine(double pointX, double pointY, double pointZ, double point1X, double point1Y, double point1Z, double point2X, double point2Y, double point2Z)`

## Description

`DistancePointLine` calculates the orthogonal distance
between 3D points and 3D lines. The lines are specified by two
points on the line ($\mathbf{Q}$ and $\mathbf{R}$).
The result is returned in *`distance`*.
The input tuples can define 1 or n points.
The points are specified by
(*`pointX`*, *`pointY`*, *`pointZ`*).
The line is specified by two points on the line
(*`point1X`*, *`point1Y`*, *`point1Z`*) and
(*`point2X`*, *`point2Y`*, *`point2Z`*).

Let $\mathbf{P}$ denote the point
(*`pointX`*, *`pointY`*, *`pointZ`*),
$\mathbf{Q}$ the first point
(*`point1X`*, *`point1Y`*, *`point1Z`*) on the line, and
$\mathbf{R}$ the second point
(*`point2X`*, *`point2Y`*, *`point2Z`*) on the line.
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

**`pointX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the original points.

**`pointY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the original points.

**`pointZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the original points.

**`point1X`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X coordinate of the first point on the line.

**`point1Y`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y coordinate of the first point on the line.

**`point1Z`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z coordinate of the first point on the line.

**`point2X`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X coordinate of the second point on the line.

**`point2Y`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y coordinate of the second point on the line.

**`point2Z`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z coordinate of the second point on the line.

**`distance`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Distance between the points and the lines.

## Possible Predecessors

`GetLineOfSight`

## Alternatives

`DistancePointPlueckerLine`

## See also

`PointPlueckerLineToHomMat3d`

## Module

Foundation
