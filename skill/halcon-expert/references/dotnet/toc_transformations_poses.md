## Poses

List of Operators ↓

A pose describes a rigid 3D transformation, i.e., a transformation
consisting of an arbitrary translation and rotation.
In HALCON, a pose is a tuple with 7 parameters: 3 parameters specifying the
translation (`transX`, `transY`, and `transZ`),
3 parameters describing the rotation (`rotX`, `rotY`, and
`rotZ`). The last parameter codes the order of the translations and
the rotations (as well as the direction of rotation).
Further information about these parameters can be found in
the documentation of [`CreatePose`](create_pose.md) and in the
`“Solution Guide III-C - 3D Vision”`.

3D poses can be interpreted in two ways: First, to describe the position and
orientation of one coordinate system relative to another (e.g., the pose of
a part's coordinate system relative to the camera coordinate system - in
short: the pose of the part relative to the camera). Following the second
interpretation, a pose describes how coordinates can be transformed between
two coordinate systems
(e.g., to transform points from part coordinates into camera coordinates).

A pose that transforms point coordinates from coordinate system 1
(*cs*1) to coordinate system 2 (*cs*2) is denoted as
$cs^2 P cs1$ ![figure](../assets/37e67f18e64de135.svg). The corresponding transformation of
a point given in *cs*1 ($\mathbf{p}^{\textit{c}s1}$) into
*cs*2 ($\mathbf{p}^{\textit{c}s2}$) is denoted as

$$\mathbf{p}^{\textit{c}s2}=^{cs2}\mathbf{P}_{cs1}\cdot\mathbf{p}^{\textit{c}s1}.$$

It should be noted that not the pose (as a tuple) but the
transformation described by this pose is used for the multiplication and the
above notation is only used for readability.
Hence, the pose $cs^2 P cs1$ ![figure](../assets/37e67f18e64de135.svg) describes the
rigid transformation that is represented by the homogeneous transformation
matrix
$\mathbf{H}(^{cs2}\mathbf{P}_{cs1})=^{\textit{c}s2}\mathbf{H}_{\textit{c}s1}$
(see, e.g., the documentation of [`CreatePose`](create_pose.md) for further details)
$$\left(\frac{p^{cs2}}{1}\right) = {cs2}\mathbf{H}_{cs1} \cdot \left(\frac{p^{cs1}}{1}\right) .$$ ![figure](../assets/30c36309bc78a9e9.svg)

Consequently, the pose $cs^2 P cs1$ ![figure](../assets/37e67f18e64de135.svg) describes the
transformation of points from *cs*1 into *cs*2.
Furthermore, as mentioned above, it also describes the transformation of the
coordinate system itself, however, in reverse order: Thus,
$cs^2 P cs1$ ![figure](../assets/37e67f18e64de135.svg) describes how coordinate system 2
must be transformed to obtain coordinate system 1, and hence, the pose of
coordinate system 2 relative to system 1.

With this notation, poses can easily concatenated like homogeneous matrices,
e.g.,
$$c s 2 P_{c s0} = c s 2 P_{c s1} \cdot c s 1 P_{c s0} .$$ ![figure](../assets/0ed078711c323ac5.svg)
Such a concatenation can be done using e.g., [`PoseCompose`](pose_compose.md).

---

#### List of Operators

- [`ConvertPoseType`](convert_pose_type.md) — Change the representation type of a 3D pose.

- [`CreatePose`](create_pose.md) — Create a 3D pose.

- [`DeserializePose`](deserialize_pose.md) — Deserialize a serialized pose.

- [`DualQuatToPose`](dual_quat_to_pose.md) — Convert a dual quaternion to a 3D pose.

- [`GetCirclePose`](get_circle_pose.md) — Determine the 3D pose of a circle from its perspective 2D projection.

- [`GetPoseType`](get_pose_type.md) — Get the representation type of a 3D pose.

- [`GetRectanglePose`](get_rectangle_pose.md) — Determine the 3D pose of a rectangle from its perspective 2D
  projection

- [`PoseAverage`](pose_average.md) — Compute the average of a set of poses.

- [`PoseCompose`](pose_compose.md) — Combine 3D poses given in two tuples.

- [`PoseInvert`](pose_invert.md) — Invert each pose in a tuple of 3D poses.

- [`PoseToDualQuat`](pose_to_dual_quat.md) — Convert a 3D pose to a unit dual quaternion.

- [`PoseToQuat`](pose_to_quat.md) — Convert the rotational part of a 3D pose to a quaternion.

- [`ProjHomMat2dToPose`](proj_hom_mat2d_to_pose.md) — Compute a pose out of a homography describing the relation between world
  and image coordinates.

- [`QuatToPose`](quat_to_pose.md) — Convert a quaternion into the corresponding 3D pose.

- [`ReadPose`](read_pose.md) — Read a 3D pose from a text file.

- [`SerializePose`](serialize_pose.md) — Serialize a pose.

- [`SetOriginPose`](set_origin_pose.md) — Translate the origin of a 3D pose.

- [`VectorToPose`](vector_to_pose.md) — Compute an absolute pose out of point correspondences between
  world and image coordinates.

- [`WritePose`](write_pose.md) — Write a 3D pose to a text file.
