# PointPlueckerLineToHomMat3d (Operator)

## Name

`PointPlueckerLineToHomMat3d` — Approximate a 3D affine transformation from 3D point-to-line
correspondences.

## Signature

`static void HOperatorSet.PointPlueckerLineToHomMat3d(HTuple transformationType, HTuple pointX, HTuple pointY, HTuple pointZ, HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ, out HTuple homMat3D)`

`void HHomMat3D.PointPlueckerLineToHomMat3d(string transformationType, HTuple pointX, HTuple pointY, HTuple pointZ, HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentX, HTuple lineMomentY, HTuple lineMomentZ)`

## Description

`PointPlueckerLineToHomMat3d` approximates a 3D affine
transformation from 3D point-to-line correspondences and returns it
as the homogeneous transformation matrix *`homMat3D`*.
The input tuples must be of same length and determine at least
3 point-to-line correspondences.
The corresponding points and lines must be at the same index positions in
the tuples.
The points are given by
(*`pointX`*, *`pointY`*, *`pointZ`*).
The lines are given by their Plücker coordinates
$\mathbf{L}$
(*`lineDirectionX`*, *`lineDirectionY`*, *`lineDirectionZ`*)
and $\mathbf{M}$
(*`lineMomentX`*, *`lineMomentY`*, *`lineMomentZ`*)
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

The type of the 3D transformation to compute is specified with
*`transformationType`*.
For *`transformationType`* = *"rigid"*, a rigid 3D
transformation (a rotation and a translation) is computed.
This is the only transformation type that is supported at the moment.

Note that for the minimum number of 3 correspondences, up to 8 valid
solutions are possible.
`PointPlueckerLineToHomMat3d` returns an arbitrarily chosen valid
solution in this case.
If a unique solution is desired, at least 4 correspondences should be
specified. Furthermore, note that no well-defined solution exists if all lines
are parallel. In this case, `PointPlueckerLineToHomMat3d` returns
an error.

The returned transformation minimizes the sum of the squared
orthogonal distances of the points transformed with
*`homMat3D`* from their corresponding lines
(see [`DistancePointPlueckerLine`](distance_point_pluecker_line.md)).

*`homMat3D`* can be used directly with operators that transform
3D data using affine transformations, e.g., [`AffineTransPoint3d`](affine_trans_point_3d.md).
To transform lines given in Plücker coordinates, the operator
[`DualQuatTransLine3d`](dual_quat_trans_line_3d.md) can be used.
Here, *`homMat3D`* must be converted into a pose using
[`HomMat3dToPose`](hom_mat3d_to_pose.md), the pose must be inverted using
[`PoseInvert`](pose_invert.md) and then converted into a dual quaternion using
[`PoseToDualQuat`](pose_to_dual_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transformationType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the transformation to compute.

Default:
"rigid"

List of values:
"rigid"

**`pointX`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double*)

X coordinate of the original points.

**`pointY`** (input_control)  point3d.y-array `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the original points.

**`pointZ`** (input_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the original points.

**`lineDirectionX`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the direction vector of the corresponding
line.

**`lineDirectionY`** (input_control)  point3d.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the direction vector of the corresponding
line.

**`lineDirectionZ`** (input_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the direction vector of the corresponding
line.

**`lineMomentX`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the moment vector of the corresponding
line.

**`lineMomentY`** (input_control)  point3d.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the moment vector of the corresponding
line.

**`lineMomentZ`** (input_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the moment vector of the corresponding
line.

**`homMat3D`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Example (HDevelop)

```
* In this example, we assume that correspondences between points
* (PX, PY, PZ) and Plücker lines (LX, LY, LZ) - (MX, MY, MZ) have
* already been computed.
point_pluecker_line_to_hom_mat3d ('rigid', PX, PY, PZ, LX, LY, LZ, \
                                  MX, MY, MZ, HomMat3D)
hom_mat3d_to_pose (HomMat3D, Pose)
* Compute the residual errors in 3D space, i.e., the distance of the
* points (PX, PY, PZ) transformed by HomMat3D from the lines.
affine_trans_point_3d (HomMat3D, PX, PY, PZ, TPX, TPY, TPZ)
distance_point_pluecker_line (TPX, TPY, TPZ, LX, LY, LZ, \
                              MX, MY, MZ, D)
* The same distance can also be computed by transforming the lines
* instead of the points.  Here, the inverse pose must be used.
pose_invert (Pose, PoseInv)
pose_to_dual_quat (PoseInv, DualQuat)
dual_quat_trans_line_3d (DualQuat, 'moment', LX, LY, LZ, MX, MY, MZ, \
                         TLX, TLY, TLZ, TMX, TMY, TMZ)
distance_point_pluecker_line (PX, PY, PZ, TLX, TLY, TLZ, \
                              TMX, TMY, TMZ, D)
```

## Possible Predecessors

`GetLineOfSight`,
`PointsToPlueckerLine`,
`PointDirectionToPlueckerLine`

## Possible Successors

`HomMat3dToPose`,
`AffineTransPoint3d`,
`PoseInvert`,
`PoseToDualQuat`,
`DualQuatTransLine3d`,
`DistancePointPlueckerLine`

## See also

`VectorToHomMat3d`

## Module

Foundation
