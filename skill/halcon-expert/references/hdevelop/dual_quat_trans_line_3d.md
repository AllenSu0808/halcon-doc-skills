# dual_quat_trans_line_3d (Operator)

## Name

`dual_quat_trans_line_3d` — Transform a 3D line with a unit dual quaternion.

## Signature

`dual_quat_trans_line_3d( : : DualQuaternion, LineFormat, LineDirectionX, LineDirectionY, LineDirectionZ, LineMomentOrPointX, LineMomentOrPointY, LineMomentOrPointZ : TransLineDirectionX, TransLineDirectionY, TransLineDirectionZ, TransLineMomentOrPointX, TransLineMomentOrPointY, TransLineMomentOrPointZ)`

## Description

The operator `dual_quat_trans_line_3d` transforms a 3D line that
is represented by its Plücker coordinates by a 3D rigid transformation that
is given by the unit dual quaternion *`DualQuaternion`*.

For a brief introduction to dual quaternions, Plücker coordinates and the
used notation, see `“Solution Guide III-C - 3D Vision”`.

If *`LineFormat`* is set to *'moment'*, the moment of
the line must be passed in *`LineMomentOrPointX`*,
*`LineMomentOrPointY`*, and *`LineMomentOrPointZ`*.

If *`LineFormat`* is set to *'point'*, instead of the moment
an arbitrary point on the line can be passed in *`LineMomentOrPointX`*,
*`LineMomentOrPointY`*, and *`LineMomentOrPointZ`*.

The parameters of the transformed line are returned in
*`TransLineDirectionX`*, *`TransLineDirectionY`*,
*`TransLineDirectionZ`*, *`TransLineMomentOrPointX`*,
*`TransLineMomentOrPointY`*, and *`TransLineMomentOrPointZ`* in the
format that was specified in *`LineFormat`*.
If *`LineFormat`* is set to *'point'*, the point on the line
that is closest to the origin of the coordinate system is returned.

## Attention

`dual_quat_trans_line_3d` returns meaningful results only if
*`DualQuaternion`* is a unit dual quaternion and the length of
the line direction is 1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DualQuaternion`** (input_control)  dual_quaternion `→`  (real / integer)

Unit dual quaternion representing the transformation.

**`LineFormat`** (input_control)  string `→`  (string)

Format of the line parameters.

Default:
'moment'

List of values:
'moment', 'point'

**`LineDirectionX`** (input_control)  point3d.x(-array) `→`  (real / integer)

X component of the direction vector of the line.

**`LineDirectionY`** (input_control)  point3d.y(-array) `→`  (real / integer)

Y component of the direction vector of the line.

**`LineDirectionZ`** (input_control)  point3d.z(-array) `→`  (real / integer)

Z component of the direction vector of the line.

**`LineMomentOrPointX`** (input_control)  point3d.x(-array) `→`  (real / integer)

X component of the moment vector or a point on the line.

**`LineMomentOrPointY`** (input_control)  point3d.y(-array) `→`  (real / integer)

Y component of the moment vector or a point on the line.

**`LineMomentOrPointZ`** (input_control)  point3d.z(-array) `→`  (real / integer)

Z component of the moment vector or a point on the line.

**`TransLineDirectionX`** (output_control)  point3d.x(-array) `→`  (real / integer)

X component of the direction vector of the
transformed line.

**`TransLineDirectionY`** (output_control)  point3d.y(-array) `→`  (real / integer)

Y component of the direction vector of the
transformed line.

**`TransLineDirectionZ`** (output_control)  point3d.z(-array) `→`  (real / integer)

Z component of the direction vector of the
transformed line.

**`TransLineMomentOrPointX`** (output_control)  point3d.x(-array) `→`  (real / integer)

X component of the moment vector or a point on the
transformed line.

**`TransLineMomentOrPointY`** (output_control)  point3d.y(-array) `→`  (real / integer)

Y component of the moment vector or a point on the
transformed line.

**`TransLineMomentOrPointZ`** (output_control)  point3d.z(-array) `→`  (real / integer)

Z component of the moment vector or a point on the
transformed line.

## Possible Predecessors

`points_to_pluecker_line`,
`point_direction_to_pluecker_line`

## Possible Successors

`dual_quat_compose`,
`dual_quat_conjugate`,
`pose_to_dual_quat`

## Alternatives

`affine_trans_point_3d`,
`dual_quat_trans_point_3d`

## See also

`dual_quat_to_hom_mat3d`,
`dual_quat_to_screw`,
`dual_quat_to_pose`,
`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`quat_rotate_point_3d`

## Module

Foundation
