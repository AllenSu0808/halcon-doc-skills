# point_pluecker_line_to_hom_mat3d (Operator)

## Name

`point_pluecker_line_to_hom_mat3d` — Approximate a 3D affine transformation from 3D point-to-line
correspondences.

## Signature

`point_pluecker_line_to_hom_mat3d( : : TransformationType, PointX, PointY, PointZ, LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentX, LineMomentY, LineMomentZ : HomMat3D)`

## Description

`point_pluecker_line_to_hom_mat3d` approximates a 3D affine
transformation from 3D point-to-line correspondences and returns it
as the homogeneous transformation matrix *`HomMat3D`*.
The input tuples must be of same length and determine at least
3 point-to-line correspondences.
The corresponding points and lines must be at the same index positions in
the tuples.
The points are given by
(*`PointX`*, *`PointY`*, *`PointZ`*).
The lines are given by their Plücker coordinates
$\mathbf{L}$
(*`LineDirectionX`*, *`LineDirectionY`*, *`LineDirectionZ`*)
and $\mathbf{M}$
(*`LineMomentX`*, *`LineMomentY`*, *`LineMomentZ`*)
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

The type of the 3D transformation to compute is specified with
*`TransformationType`*.
For *`TransformationType`* = *'rigid'*, a rigid 3D
transformation (a rotation and a translation) is computed.
This is the only transformation type that is supported at the moment.

Note that for the minimum number of 3 correspondences, up to 8 valid
solutions are possible.
`point_pluecker_line_to_hom_mat3d` returns an arbitrarily chosen valid
solution in this case.
If a unique solution is desired, at least 4 correspondences should be
specified. Furthermore, note that no well-defined solution exists if all lines
are parallel. In this case, `point_pluecker_line_to_hom_mat3d` returns
an error.

The returned transformation minimizes the sum of the squared
orthogonal distances of the points transformed with
*`HomMat3D`* from their corresponding lines
(see [`distance_point_pluecker_line`](distance_point_pluecker_line.md)).

*`HomMat3D`* can be used directly with operators that transform
3D data using affine transformations, e.g., [`affine_trans_point_3d`](affine_trans_point_3d.md).
To transform lines given in Plücker coordinates, the operator
[`dual_quat_trans_line_3d`](dual_quat_trans_line_3d.md) can be used.
Here, *`HomMat3D`* must be converted into a pose using
[`hom_mat3d_to_pose`](hom_mat3d_to_pose.md), the pose must be inverted using
[`pose_invert`](pose_invert.md) and then converted into a dual quaternion using
[`pose_to_dual_quat`](pose_to_dual_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TransformationType`** (input_control)  string `→`  (string)

Type of the transformation to compute.

Default:
'rigid'

List of values:
'rigid'

**`PointX`** (input_control)  point3d.x-array `→`  (real)

X coordinate of the original points.

**`PointY`** (input_control)  point3d.y-array `→`  (real)

Y coordinate of the original points.

**`PointZ`** (input_control)  point3d.z-array `→`  (real)

Z coordinate of the original points.

**`LineDirectionX`** (input_control)  point3d.x-array `→`  (real / integer)

X component of the direction vector of the corresponding
line.

**`LineDirectionY`** (input_control)  point3d.y-array `→`  (real / integer)

Y component of the direction vector of the corresponding
line.

**`LineDirectionZ`** (input_control)  point3d.z-array `→`  (real / integer)

Z component of the direction vector of the corresponding
line.

**`LineMomentX`** (input_control)  point3d.x-array `→`  (real / integer)

X component of the moment vector of the corresponding
line.

**`LineMomentY`** (input_control)  point3d.y-array `→`  (real / integer)

Y component of the moment vector of the corresponding
line.

**`LineMomentZ`** (input_control)  point3d.z-array `→`  (real / integer)

Z component of the moment vector of the corresponding
line.

**`HomMat3D`** (output_control)  hom_mat3d `→`  (real)

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

`get_line_of_sight`,
`points_to_pluecker_line`,
`point_direction_to_pluecker_line`

## Possible Successors

`hom_mat3d_to_pose`,
`affine_trans_point_3d`,
`pose_invert`,
`pose_to_dual_quat`,
`dual_quat_trans_line_3d`,
`distance_point_pluecker_line`

## See also

`vector_to_hom_mat3d`

## Module

Foundation
