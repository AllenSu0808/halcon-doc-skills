# PointDirectionToPlueckerLine (Operator)

## Name

`PointDirectionToPlueckerLine` — Convert a 3D line given by a point and a direction to Plücker
coordinates.

## Signature

`static void HOperatorSet.PointDirectionToPlueckerLine(HTuple pointX, HTuple pointY, HTuple pointZ, HTuple directionX, HTuple directionY, HTuple directionZ, out HTuple lineDirectionX, out HTuple lineDirectionY, out HTuple lineDirectionZ, out HTuple lineMomentX, out HTuple lineMomentY, out HTuple lineMomentZ)`

`static void HMisc.PointDirectionToPlueckerLine(HTuple pointX, HTuple pointY, HTuple pointZ, HTuple directionX, HTuple directionY, HTuple directionZ, out HTuple lineDirectionX, out HTuple lineDirectionY, out HTuple lineDirectionZ, out HTuple lineMomentX, out HTuple lineMomentY, out HTuple lineMomentZ)`

`static void HMisc.PointDirectionToPlueckerLine(double pointX, double pointY, double pointZ, double directionX, double directionY, double directionZ, out double lineDirectionX, out double lineDirectionY, out double lineDirectionZ, out double lineMomentX, out double lineMomentY, out double lineMomentZ)`

## Description

`PointDirectionToPlueckerLine` converts the 3D line given
by the point (*`pointX`*, *`pointY`*, *`pointZ`*) and
the direction (*`directionX`*, *`directionY`*,
*`directionZ`*) to Plücker coordinates
$\mathbf{L}$
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*)
and $\mathbf{M}$
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{P}$ denote the point
(*`pointX`*, *`pointY`*, *`pointZ`*)
and $\mathbf{D}$ the direction
(*`directionX`*, *`directionY`*, *`directionZ`*) of the line.
To compute the line direction $\mathbf{L}$,
the length $\|\mathbf{D}\|$ of the vector $\mathbf{D}$
is computed.
If $\|\mathbf{D}\|=0$, the direction $\mathbf{D}$
does not define a line and an error is returned.
The further calculations to Plücker coordinates are given in
[`PointsToPlueckerLine`](points_to_pluecker_line.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pointX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the point on the line.

**`pointY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the point on the line.

**`pointZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the point on the line.

**`directionX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the direction of the line.

**`directionY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the direction of the line.

**`directionZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the direction of the line.

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

## Possible Successors

`DistancePointPlueckerLine`,
`PointPlueckerLineToHomMat3d`

## Alternatives

`PointsToPlueckerLine`

## See also

`PlueckerLineToPointDirection`

## Module

Foundation
