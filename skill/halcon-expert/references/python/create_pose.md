# create_pose (Operator)

## Name

`create_pose` — Create a 3D pose.

## Signature

`def create_pose(trans_x: float, trans_y: float, trans_z: float, rot_x: float, rot_y: float, rot_z: float, order_of_transform: str, order_of_rotation: str, view_of_transform: str) -> Sequence[Union[int, float]]`

## Description

`create_pose` creates the 3D pose *`pose`*. A pose describes a
rigid 3D transformation, i.e., a transformation consisting of an arbitrary
translation and rotation, with 6 parameters: *`trans_x`*,
*`trans_y`*, and *`trans_z`* specify the translation along the x-,
y-, and z-axis, respectively, while *`rot_x`*, *`rot_y`*, and
*`rot_z`* describe the rotation.

3D poses are typically used in two ways: First, to describe the position and
orientation of one coordinate system relative to another (e.g., the pose of a
part's coordinate system relative to the camera coordinate system - in short:
the pose of the part relative to the camera) and secondly, to describe how
coordinates can be transformed between two coordinate systems (e.g., to
transform points from part coordinates into camera coordinates).

### Representation of orientation (rotation)

A 3D rotation around an arbitrary axis can be represented by 3 parameters in
multiple ways. HALCON lets you choose between three of them with the
parameter *`order_of_rotation`*: If you pass the value *"gba"*, the
rotation is described by the following chain of rotations around the three
axes (see [`hom_mat3d_rotate`](hom_mat3d_rotate.md) for the content for the rotation matrices
$\mathbf{R}_{x},\mathbf{R}_{y}\text{, and}\mathbf{R}_{z}$):

$$\mathbf{R}_{gba}=\mathbf{R}_{x}(\texttt{RotX})\cdot\mathbf{R}_{y}(\texttt{RotY})\cdot\mathbf{R}_{z}(\texttt{RotZ})$$

$\mathbf{R}_{gba}$ is referred to
as the Yaw-Pitch-Roll convention in the literature.
Please note that you can “read” this chain in two ways: If you start from
the right, the rotations are always performed relative to the global (i.e.,
fixed or “old”) coordinate system. Thus,
$\mathbf{R}_{gba}$ can be read as follows:
First rotate around the z-axis, then around the “old” y-axis, and finally
around the “old” x-axis. In contrast, if you read from the left to the
right, the rotations are performed relative to the local (i.e., “new”)
coordinate system. Then, $\mathbf{R}_{gba}$
corresponds to the following: First rotate around the x-axis, the around the
“new” y-axis, and finally around the “new(est)” z-axis.

Reading $\mathbf{R}_{gba}$ from right to
left corresponds to the following sequence of operator calls:

|  |
| --- |
| [`hom_mat3d_identity(HomMat3DIdent)`](hom_mat3d_identity.md) |
| [`hom_mat3d_rotate(HomMat3DIdent, RotZ, "z", 0, 0, 0, HomMat3DRotZ)`](hom_mat3d_rotate.md) |
| [`hom_mat3d_rotate(HomMat3DRotZ, RotY, "y", 0, 0, 0, HomMat3DRotYZ)`](hom_mat3d_rotate.md) |
| [`hom_mat3d_rotate(HomMat3DRotYZ, RotX, "x", 0, 0, 0, HomMat3DXYZ)`](hom_mat3d_rotate.md) |

In contrast, reading from left to right corresponds to the following operator
sequence:

|  |
| --- |
| [`hom_mat3d_identity(HomMat3DIdent)`](hom_mat3d_identity.md) |
| [`hom_mat3d_rotate_local(HomMat3DIdent, RotX, "x", HomMat3DRotX)`](hom_mat3d_rotate_local.md) |
| [`hom_mat3d_rotate_local(HomMat3DRotX, RotY, "y", HomMat3DRotXY)`](hom_mat3d_rotate_local.md) |
| [`hom_mat3d_rotate_local(HomMat3DRotXY, RotZ, "z", HomMat3DXYZ)`](hom_mat3d_rotate_local.md) |

When passing *"abg"* in *`order_of_rotation`*, the rotation
corresponds to the following chain:

$$\mathbf{R}_{abg}=\mathbf{R}_{z}(\texttt{RotZ})\cdot\mathbf{R}_{y}(\texttt{RotY})\cdot\mathbf{R}_{x}(\texttt{RotX})$$

$\mathbf{R}_{abg}$ is referred to
as the Roll-Pitch-Yaw convention in the literature.

If you pass *"rodriguez"* in *`order_of_rotation`*, the rotation
parameters *`rot_x`*, *`rot_y`*, and *`rot_z`* are interpreted as
the x-, y-, and z-component of the so-called Rodriguez rotation vector. The
direction of the vector defines the (arbitrary) axis of rotation. The length
of the vector usually defines the rotation angle with positive orientation.
Here, a variation of the Rodriguez vector is used, where the length of the
vector defines the tangent of half the rotation angle:

$$R_{ Rodrigues } = rotate around \begin{pmatrix} RotX \\ RotY \\ RotZ \end{pmatrix} by 2 \cdot arctan\big(\sqrt{RotX^{2} + RotY^{2} + RotZ^{2}}\big)$$ ![figure](../assets/f610408dafcea12a.svg)

Please note that these 3D poses can be ambiguous, meaning a homogeneous
transformation matrix can have several pose representations.
For example, for
$\mathbf{R}_{gba}$ with $b=\pm90$
the following poses correspond to the same homogeneous transformation
matrix:

|  |
| --- |
| `create_pose(0, 0, 0, 30, 90, 54, 'Rp+T', 'gba', 'point', Pose1)` |
| `create_pose(0, 0, 0, 17, 90, 67, 'Rp+T', 'gba', 'point', Pose2)` |

If this leads to problems, you can instead use homogeneous transformation
matrices or quaternions ([`axis_angle_to_quat`](axis_angle_to_quat.md)) to represent rotations.

### Corresponding homogeneous transformation matrix

You can obtain the homogeneous transformation matrix corresponding to a pose
with the operator [`pose_to_hom_mat3d`](pose_to_hom_mat3d.md). In the standard definition, this
is the following homogeneous transformation matrix which can be split into
two separate matrices, one for the translation
(H(T)) and one for the rotation
(H(R)):

$$H_{pose} = \begin{bmatrix} \mathbf{R} & \mathbf{T} \\ 0\ 0 \ 1 \end{bmatrix} = \begin{bmatrix} R( RotX, RotY, RotZ ) & \begin{array}{c} \text{TransX} \\ \text{TransY} \\ \text{TransZ} \end{array} \\ 0 & 0 & 0 & 1 \end{bmatrix} = H(\mathbf{T}) \cdot H(\mathbf{R})$$ ![figure](../assets/e0688dc02e9f73ec.svg)

### Transformation of coordinates

The following equation describes how a point can be transformed from
coordinate system 1 (*cs*1) into coordinate system 2 (*cs*2)
with a pose, or more exactly, with the corresponding homogeneous
transformation matrix $cs^2H_c^1$ ![figure](../assets/90cd9770d582e93c.svg)
(input and output points as homogeneous vectors, see also
[`affine_trans_point_3d`](affine_trans_point_3d.md)). Note that to transform points from
*cs*1 into *cs*2, you use the transformation matrix that
describes the pose of *cs*1 relative to *cs*2.

$$\left(\begin{array}{c}\mathbf{p}^{cs2}\\1\end{array}\right) = {\mathbf{H}}_{cs1}^{cs2} \cdot \left(\begin{array}{c}\mathbf{p}^{cs1}\\1\end{array}\right) = \left( {\mathbf{R}}(\text{RotX},\text{RotY},\text{RotZ}) \cdot \mathbf{p}^{cs1} + \begin{pmatrix}\text{TransX} \\ \text{TransY} \\ \text{TransZ}\end{pmatrix} \right)$$ ![figure](../assets/b2d2c7a730374d93.svg)

This corresponds to the following operator calls:

|  |
| --- |
| `pose_to_hom_mat3d(PoseOf1In2, HomMat3DFrom1In2)` |
| `affine_trans_point_3d(HomMat3DFrom1In2, P1X, P1Y, P1Z, P2X, P2Y, P2Z)` |

### Non-standard pose definitions

So far, we described the standard pose definition. To create such poses, you
select the (default) values *"Rp+T"* for the parameter
*`order_of_transform`* and *"point"* for *`view_of_transform`*.
By specifying other values for these parameters, you can create non-standard
poses types which we describe briefly below. Please note that these
representation types are only supported for backwards compatibility; we
strongly recommend to use the standard types.

If you select *"R(p-T)"* for *`order_of_transform`*, the created
pose corresponds to the following chain of transformations, i.e., the
sequence of rotation and translation is reversed and the translation is
negated:

$$H_{R(p-T)} = \left[ R(R_{\text{RotX}},R_{\text{RotY}},R_{\text{RotZ}}) \quad 0 \ 0 \ 0 \ 1 \right] \\quad \cdot \\left[ \begin{array}{cccc}1&0&0&-TransX \\0&1&0&-TransY \\0&0&1&-TransZ \\0&0&0&1\end{array}\right] = H(R) \cdot H(-T)$$ ![figure](../assets/98a9ac39ba5da2f4.svg)

If you select *"coordinate_system"* for *`view_of_transform`*, the
sequence of transformations remains constant, but the rotation angles are
negated. Please note that, contrary to its name, this is not equivalent to
transforming a coordinate system!

$$H_{coordinate_system} = \begin{bmatrix} 1 & 0 & 0 & \text{TransX} \\ 0 & 1 & 0 & \text{TransY} \\ 0 & 0 & 1 & \text{TransZ} \\ 0 & 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} \mathrm{R}(-\text{RotX}, -\text{RotY}, -\text{RotZ}) \\ 0 \\ 0 \\ 0 \end{bmatrix}$$ ![figure](../assets/907bd3c4c226d229.svg)

### Returned data structure

The created 3D pose is returned in *`pose`* which is a tuple of length
seven. The first three elements hold the translation parameters
*`trans_x`*, *`trans_y`*, and *`trans_z`*, followed by the
rotation parameters *`rot_x`*, *`rot_y`*, and *`rot_z`*. The last
element codes the representation type of the pose that you selected with
the parameters *`order_of_transform`*, *`order_of_rotation`*, and
*`view_of_transform`*. The following table lists the possible
combinations. As already noted, we recommend to use only the representation
types with *`order_of_transform`* = *"Rp+T"* and
*`view_of_transform`* = *"point"* (codes 0, 2, and 4).

| *`order_of_transform`* | *`order_of_rotation`* | *`view_of_transform`* | Code |
| --- | --- | --- | --- |
| *"Rp+T"* | *"gba"* | *"point"* | 0 |
| *"Rp+T"* | *"abg"* | *"point"* | 2 |
| *"Rp+T"* | *"rodriguez"* | *"point"* | 4 |
| *"Rp+T"* | *"gba"* | *"coordinate_system"* | 1 |
| *"Rp+T"* | *"abg"* | *"coordinate_system"* | 3 |
| *"Rp+T"* | *"rodriguez"* | *"coordinate_system"* | 5 |
| *"R(p-T)"* | *"gba"* | *"point"* | 8 |
| *"R(p-T)"* | *"abg"* | *"point"* | 10 |
| *"R(p-T)"* | *"rodriguez"* | *"point"* | 12 |
| *"R(p-T)"* | *"gba"* | *"coordinate_system"* | 9 |
| *"R(p-T)"* | *"abg"* | *"coordinate_system"* | 11 |
| *"R(p-T)"* | *"rodriguez"* | *"coordinate_system"* | 13 |

You can convert poses into other representation types using
[`convert_pose_type`](convert_pose_type.md) and query the type using [`get_pose_type`](get_pose_type.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`trans_x`** (input_control)  real `→` float

Translation along the x-axis (in [m]).

Default:
0.1

Suggested values:
-1.0, -0.75, -0.5, -0.25, -0.2, -0.1, -0.5, -0.25, -0.125, -0.01, 0.0, 0.01, 0.125, 0.25, 0.5, 0.1, 0.2, 0.25, 0.5, 0.75, 1.0

**`trans_y`** (input_control)  real `→` float

Translation along the y-axis (in [m]).

Default:
0.1

Suggested values:
-1.0, -0.75, -0.5, -0.25, -0.2, -0.1, -0.5, -0.25, -0.125, -0.01, 0.0, 0.01, 0.125, 0.25, 0.5, 0.1, 0.2, 0.25, 0.5, 0.75, 1.0

**`trans_z`** (input_control)  real `→` float

Translation along the z-axis (in [m]).

Default:
0.1

Suggested values:
-1.0, -0.75, -0.5, -0.25, -0.2, -0.1, -0.5, -0.25, -0.125, -0.01, 0.0, 0.01, 0.125, 0.25, 0.5, 0.1, 0.2, 0.25, 0.5, 0.75, 1.0

**`rot_x`** (input_control)  real `→` float

Rotation around x-axis or x component of the Rodriguez
vector (in [°] or without unit).

Default:
90.0

Suggested values:
0.0, 90.0, 180.0, 270.0

Value range:
`0
≤
rot_x
≤
360`

**`rot_y`** (input_control)  real `→` float

Rotation around y-axis or y component of the Rodriguez
vector (in [°] or without unit).

Default:
90.0

Suggested values:
0.0, 90.0, 180.0, 270.0

Value range:
`0
≤
rot_y
≤
360`

**`rot_z`** (input_control)  real `→` float

Rotation around z-axis or z component of the Rodriguez
vector (in [°] or without unit).

Default:
90.0

Suggested values:
0.0, 90.0, 180.0, 270.0

Value range:
`0
≤
rot_z
≤
360`

**`order_of_transform`** (input_control)  string `→` str

Order of rotation and translation.

Default:
"Rp+T"

Suggested values:
"Rp+T", "R(p-T)"

**`order_of_rotation`** (input_control)  string `→` str

Meaning of the rotation values.

Default:
"gba"

Suggested values:
"gba", "abg", "rodriguez"

**`view_of_transform`** (input_control)  string `→` str

View of transformation.

Default:
"point"

Suggested values:
"point", "coordinate_system"

**`pose`** (output_control)  pose `→` Sequence[Union[int, float]]

3D pose.

Number of elements:
7

## Result

`create_pose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Successors

`pose_to_hom_mat3d`,
`write_pose`,
`camera_calibration`,
`hand_eye_calibration`

## Alternatives

`read_pose`,
`hom_mat3d_to_pose`

## See also

`hom_mat3d_rotate`,
`hom_mat3d_translate`,
`convert_pose_type`,
`get_pose_type`,
`hom_mat3d_to_pose`,
`pose_to_hom_mat3d`,
`write_pose`,
`read_pose`

## Module

Foundation
