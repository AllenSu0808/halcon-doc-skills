# PointsToPlueckerLine (Operator)

## Name

`PointsToPlueckerLine` — Convert a 3D line given by two points to Plücker coordinates.

## Signature

`static void HOperatorSet.PointsToPlueckerLine(HTuple point1X, HTuple point1Y, HTuple point1Z, HTuple point2X, HTuple point2Y, HTuple point2Z, out HTuple lineDirectionX, out HTuple lineDirectionY, out HTuple lineDirectionZ, out HTuple lineMomentX, out HTuple lineMomentY, out HTuple lineMomentZ)`

`static void HMisc.PointsToPlueckerLine(HTuple point1X, HTuple point1Y, HTuple point1Z, HTuple point2X, HTuple point2Y, HTuple point2Z, out HTuple lineDirectionX, out HTuple lineDirectionY, out HTuple lineDirectionZ, out HTuple lineMomentX, out HTuple lineMomentY, out HTuple lineMomentZ)`

`static void HMisc.PointsToPlueckerLine(double point1X, double point1Y, double point1Z, double point2X, double point2Y, double point2Z, out double lineDirectionX, out double lineDirectionY, out double lineDirectionZ, out double lineMomentX, out double lineMomentY, out double lineMomentZ)`

## Description

`PointsToPlueckerLine` converts the 3D line given by the
two points (*`point1X`*, *`point1Y`*, *`point1Z`*)
and (*`point2X`*, *`point2Y`*, *`point2Z`*) to
Plücker coordinates $\mathbf{L}=$
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*)
and $\mathbf{M}=$
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{P}$ denote the first point
(*`point1X`*, *`point1Y`*, *`point1Z`*)
and $\mathbf{Q}$ the second point
(*`point2X`*, *`point2Y`*, *`point2Z`*) on the line.
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

**`point1X`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the first point on the line.

**`point1Y`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the first point on the line.

**`point1Z`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the first point on the line.

**`point2X`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the second point on the line.

**`point2Y`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the second point on the line.

**`point2Z`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the second point on the line.

**`lineDirectionX`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X component of the direction vector of the line.

**`lineDirectionY`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y component of the direction vector of the line.

**`lineDirectionZ`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z component of the direction vector of the line.

**`lineMomentX`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X component of the moment vector of the line.

**`lineMomentY`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y component of the moment vector of the line.

**`lineMomentZ`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z component of the moment vector of the line.

## Possible Predecessors

`GetLineOfSight`

## Possible Successors

`DistancePointPlueckerLine`,
`PointPlueckerLineToHomMat3d`

## Alternatives

`PointDirectionToPlueckerLine`

## See also

`PlueckerLineToPoints`

## Module

Foundation
