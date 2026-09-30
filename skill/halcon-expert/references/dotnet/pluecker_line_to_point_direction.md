# PlueckerLineToPointDirection (Operator)

## Name

`PlueckerLineToPointDirection` — Convert a 3D line given by Plücker coordinates to a 3D line given by
a point and a direction.

## Signature

`static void HOperatorSet.PlueckerLineToPointDirection(HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ, out HTuple pointX, out HTuple pointY, out HTuple pointZ, out HTuple directionX, out HTuple directionY, out HTuple directionZ)`

`static void HMisc.PlueckerLineToPointDirection(HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ, out HTuple pointX, out HTuple pointY, out HTuple pointZ, out HTuple directionX, out HTuple directionY, out HTuple directionZ)`

`static void HMisc.PlueckerLineToPointDirection(double lineDirectionX, double lineDirectionY, double lineDirectionZ, double lineMomentX, double lineMomentY, double lineMomentZ, out double pointX, out double pointY, out double pointZ, out double directionX, out double directionY, out double directionZ)`

## Description

`PlueckerLineToPointDirection` converts a 3D line given by
Plücker coordinates to a line given by a point on the line and the
direction of the line.
The line is given in Plücker coordinates
$\mathbf{L}$
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*)
and $\mathbf{M}$
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*).
The direction is given by
(*`directionX`*, *`directionY`*, *`directionZ`*) of the line.
and the point on the line by
(*`pointX`*, *`pointY`*, *`pointZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.
All input tuples must be of same length.

Let $\mathbf{L}$ denote the line direction
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*),
$\mathbf{M}$ the line moment
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*),
$\mathbf{P}$ the point
(*`pointX`*, *`pointY`*, *`pointZ`*) on the line, and
$\mathbf{D}$ the direction
(*`directionX`*, *`directionY`*, *`directionZ`*) of the line.
Then, $\mathbf{P}=\mathbf{L}\times\mathbf{M}$ and
$\mathbf{D}=\mathbf{L}$.
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

**`pointX`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the first point on the line.

**`pointY`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the first point on the line.

**`pointZ`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the first point on the line.

**`directionX`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the direction of the line.

**`directionY`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the direction of the line.

**`directionZ`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the direction of the line.

## Alternatives

`PlueckerLineToPoints`

## See also

`PointDirectionToPlueckerLine`

## Module

Foundation
