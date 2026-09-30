# PlueckerLineToPoints (Operator)

## Name

`PlueckerLineToPoints` — Convert a 3D line given by Plücker coordinates to a 3D line given by
two points.

## Signature

`static void HOperatorSet.PlueckerLineToPoints(HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ, out HTuple point1X, out HTuple point1Y, out HTuple point1Z, out HTuple point2X, out HTuple point2Y, out HTuple point2Z)`

`static void HMisc.PlueckerLineToPoints(HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ, out HTuple point1X, out HTuple point1Y, out HTuple point1Z, out HTuple point2X, out HTuple point2Y, out HTuple point2Z)`

`static void HMisc.PlueckerLineToPoints(double lineDirectionX, double lineDirectionY, double lineDirectionZ, double lineMomentX, double lineMomentY, double lineMomentZ, out double point1X, out double point1Y, out double point1Z, out double point2X, out double point2Y, out double point2Z)`

## Description

`PlueckerLineToPoints` converts a 3D line given by Plücker
coordinates $\mathbf{L}$
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*)
and $\mathbf{M}$
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*).
to a line given by two points on the line
(*`point1X`*, *`point1Y`*, *`point1Z`*) and
(*`point2X`*, *`point2Y`*, *`point2Z`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{L}$ denote the line direction
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*),
$\mathbf{M}$ the line moment
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*),
$\mathbf{P}$ the first point
(*`point1X`*, *`point1Y`*, *`point1Z`*) on the line, and
$\mathbf{Q}$ the second point
(*`point2X`*, *`point2Y`*, *`point2Z`*) on the line.
Then, $\mathbf{P}=\mathbf{L}\times\mathbf{M}$ and
$\mathbf{Q}=\mathbf{P}+\mathbf{L}$.
Note that $\mathbf{P}$ is the point on the line closest to the origin.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`lineDirectionX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X component of the direction vector of the line.

**`lineDirectionY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y component of the direction vector of the line.

**`lineDirectionZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z component of the direction vector of the line.

**`lineMomentX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X component of the moment vector of the line.

**`lineMomentY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y component of the moment vector of the line.

**`lineMomentZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z component of the moment vector of the line.

**`point1X`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the first point on the line.

**`point1Y`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the first point on the line.

**`point1Z`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the first point on the line.

**`point2X`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the second point on the line.

**`point2Y`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the second point on the line.

**`point2Z`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the second point on the line.

## Possible Successors

`DistancePointLine`

## Alternatives

`PlueckerLineToPointDirection`

## See also

`PointsToPlueckerLine`

## Module

Foundation
