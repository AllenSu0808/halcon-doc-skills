# point_pluecker_line_to_hom_mat3d (Operator)

## Name

`point_pluecker_line_to_hom_mat3d` — Approximate a 3D affine transformation from 3D point-to-line
correspondences.

## Signature

`def point_pluecker_line_to_hom_mat3d(transformation_type: str, point_x: Sequence[float], point_y: Sequence[float], point_z: Sequence[float], line_direction_x: Sequence[Union[float, int]], line_direction_y: Sequence[Union[float, int]], line_direction_z: Sequence[Union[float, int]], line_moment_x: Sequence[Union[float, int]], line_moment_y: Sequence[Union[float, int]], line_moment_z: Sequence[Union[float, int]]) -> Sequence[float]`

## Description

`point_pluecker_line_to_hom_mat3d` approximates a 3D affine
transformation from 3D point-to-line correspondences and returns it
as the homogeneous transformation matrix *`hom_mat_3d`*.
The input tuples must be of same length and determine at least
3 point-to-line correspondences.
The corresponding points and lines must be at the same index positions in
the tuples.
The points are given by
(*`point_x`*, *`point_y`*, *`point_z`*).
The lines are given by their Plücker coordinates
$\mathbf{L}$
(*`line_direction_x`*, *`line_direction_y`*, *`line_direction_z`*)
and $\mathbf{M}$
(*`line_moment_x`*, *`line_moment_y`*, *`line_moment_z`*)
For the definition of Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

The type of the 3D transformation to compute is specified with
*`transformation_type`*.
For *`transformation_type`* = *"rigid"*, a rigid 3D
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
*`hom_mat_3d`* from their corresponding lines
(see [`distance_point_pluecker_line`](distance_point_pluecker_line.md)).

*`hom_mat_3d`* can be used directly with operators that transform
3D data using affine transformations, e.g., [`affine_trans_point_3d`](affine_trans_point_3d.md).
To transform lines given in Plücker coordinates, the operator
[`dual_quat_trans_line_3d`](dual_quat_trans_line_3d.md) can be used.
Here, *`hom_mat_3d`* must be converted into a pose using
[`hom_mat3d_to_pose`](hom_mat3d_to_pose.md), the pose must be inverted using
[`pose_invert`](pose_invert.md) and then converted into a dual quaternion using
[`pose_to_dual_quat`](pose_to_dual_quat.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transformation_type`** (input_control)  string `→` str

Type of the transformation to compute.

Default:
"rigid"

List of values:
"rigid"

**`point_x`** (input_control)  point3d.x-array `→` Sequence[float]

X coordinate of the original points.

**`point_y`** (input_control)  point3d.y-array `→` Sequence[float]

Y coordinate of the original points.

**`point_z`** (input_control)  point3d.z-array `→` Sequence[float]

Z coordinate of the original points.

**`line_direction_x`** (input_control)  point3d.x-array `→` Sequence[Union[float, int]]

X component of the direction vector of the corresponding
line.

**`line_direction_y`** (input_control)  point3d.y-array `→` Sequence[Union[float, int]]

Y component of the direction vector of the corresponding
line.

**`line_direction_z`** (input_control)  point3d.z-array `→` Sequence[Union[float, int]]

Z component of the direction vector of the corresponding
line.

**`line_moment_x`** (input_control)  point3d.x-array `→` Sequence[Union[float, int]]

X component of the moment vector of the corresponding
line.

**`line_moment_y`** (input_control)  point3d.y-array `→` Sequence[Union[float, int]]

Y component of the moment vector of the corresponding
line.

**`line_moment_z`** (input_control)  point3d.z-array `→` Sequence[Union[float, int]]

Z component of the moment vector of the corresponding
line.

**`hom_mat_3d`** (output_control)  hom_mat3d `→` Sequence[float]

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
