# DistancePointPlueckerLine (Operator)

## Name

`DistancePointPlueckerLine` — Calculate the distance between a 3D point and a 3D line given by
Plücker coordinates.

## Signature

`static void HOperatorSet.DistancePointPlueckerLine(HTuple pointX, HTuple pointY, HTuple pointZ, HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ, out HTuple distance)`

`static HTuple HMisc.DistancePointPlueckerLine(HTuple pointX, HTuple pointY, HTuple pointZ, HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ)`

`static double HMisc.DistancePointPlueckerLine(double pointX, double pointY, double pointZ, double lineDirectionX, double lineDirectionY, double lineDirectionZ, double lineMomentX, double lineMomentY, double lineMomentZ)`

## Description

`DistancePointPlueckerLine` calculates the orthogonal
distance between 3D points and 3D lines.
The result is returned in *`distance`*.
The input tuples can define 1 or n points $\mathbf{P}$
and lines, respectively.
The points are specified by
(*`pointX`*, *`pointY`*, *`pointZ`*).
The lines are given in Plücker coordinates
$\mathbf{L}$
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*)
and $\mathbf{M}$
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*).
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

Let $\mathbf{P}$ denote the point
(*`pointX`*, *`pointY`*, *`pointZ`*),
$\mathbf{L}$ the direction
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*),
and $\mathbf{M}$ the moment
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*)
of the Plücker line.
Furthermore, let $D$ denote the distance *`distance`*. Then,
$D=\|\mathbf{P}\times\mathbf{L}-\mathbf{M}\|$,
where $\times$ denotes the cross product of two vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pointX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the original points.

**`pointY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the original points.

**`pointZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the original points.

**`lineDirectionX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the direction vector of the corresponding
line.

**`lineDirectionY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the direction vector of the corresponding
line.

**`lineDirectionZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the direction vector of the corresponding
line.

**`lineMomentX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the moment vector of the corresponding
line.

**`lineMomentY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the moment vector of the corresponding
line.

**`lineMomentZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the moment vector of the corresponding
line.

**`distance`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Distance between the points and the lines.

## Possible Predecessors

`PointsToPlueckerLine`,
`PointDirectionToPlueckerLine`

## Alternatives

`DistancePointLine`

## See also

`PointPlueckerLineToHomMat3d`

## Module

Foundation
