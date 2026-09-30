# CreateCamPoseLookAtPoint (Operator)

## Name

`CreateCamPoseLookAtPoint` — Create a 3D camera pose from camera center and viewing direction.

## Signature

`static void HOperatorSet.CreateCamPoseLookAtPoint(HTuple camPosX, HTuple camPosY, HTuple camPosZ, HTuple lookAtX, HTuple lookAtY, HTuple lookAtZ, HTuple refPlaneNormal, HTuple camRoll, out HTuple camPose)`

`static HPose[] HPose.CreateCamPoseLookAtPoint(HTuple camPosX, HTuple camPosY, HTuple camPosZ, HTuple lookAtX, HTuple lookAtY, HTuple lookAtZ, HTuple refPlaneNormal, HTuple camRoll)`

`void HPose.CreateCamPoseLookAtPoint(double camPosX, double camPosY, double camPosZ, double lookAtX, double lookAtY, double lookAtZ, HTuple refPlaneNormal, double camRoll)`

## Description

The operator `CreateCamPoseLookAtPoint` creates a 3D
camera pose with respect to a world coordinate system based on two
points and the camera roll angle.

The first of the two points defines the position of the optical
center of the camera in the world coordinate system, i.e., the
origin of the camera coordinate system. It is given by its three
coordinates *`camPosX`*, *`camPosY`*, and
*`camPosZ`*. The second of the two points defines the viewing
direction of the camera. It represents the point in the world
coordinate system at which the camera is to look. It is also
specified by its three coordinates *`lookAtX`*,
*`lookAtY`*, and *`lookAtZ`*. Consequently, the second
point lies on the z axis of the camera coordinate system.

Finally, the remaining degree of freedom to be specified is a
rotation of the camera around its z axis, i.e., the roll angle of
the camera. To determine this rotation, the normal of a reference
plane can be specified in *`refPlaneNormal`*, which defines the
reference orientation of the camera. Finally, the camera roll angle
can be specified in *`camRoll`*, which describes a rotation of
the camera around its z axis with respect to its reference
orientation.

The reference plane can be seen as a plane in the world coordinate
system that is parallel to the x axis of the camera (in its
reference orientation, i.e., with a roll angle of 0). In an
alternative interpretation, the normal vector of the reference plane
projected onto the image plane points upwards, i.e., it is mapped to
the negative y axis of the camera coordinate system. The parameter
*`refPlaneNormal`* may take one of the following values:

- ***"x"*:** —

  The reference plane is the yz plane of the world coordinate
  system. The projected x axis of the world coordinate system points
  *upwards* in the image plane.
- ***"-x"*:** —

  The reference plane is the yz plane of the world coordinate
  system. The projected x axis of the world coordinate system points
  *downwards* in the image plane.
- ***"y"*:** —

  The reference plane is the xz plane of the world coordinate
  system. The projected y axis of the world coordinate system points
  *upwards* in the image plane.
- ***"-y"*:** —

  The reference plane is the xz plane of the world coordinate
  system. The projected y axis of the world coordinate system points
  *downwards* in the image plane.
- ***"z"*:** —

  The reference plane is the xy plane of the world coordinate
  system. The projected z axis of the world coordinate system points
  *upwards* in the image plane.
- ***"-z"*:** —

  The reference plane is the xy plane of the world coordinate
  system. The projected z axis of the world coordinate system points
  *downwards* in the image plane.

Alternatively to the above values, an arbitrary normal vector can be
specified in *`refPlaneNormal`*, which is not restricted to the
coordinate axes. For this, a tuple of three values representing the
three components of the normal vector must be passed.

Note that the position of the optical center and the point at which
the camera looks must differ from each other. Furthermore, the
normal vector of the reference plane and the z axis of the camera
must not be parallel. Otherwise, the camera pose is not
well-defined.

`CreateCamPoseLookAtPoint` is particularly useful if a 3D
object model or a 3D shape model should be visualized from a certain
camera position. In this case, the pose that is created by
`CreateCamPoseLookAtPoint` can be passed to
[`ProjectObjectModel3d`](project_object_model_3d.md) or [`ProjectShapeModel3d`](project_shape_model_3d.md),
respectively.

It is also possible to pass tuples of different length for different
input parameters. In this case, internally the maximum number of
parameter values over all input control parameters is computed.
This number is taken as the number of output camera poses. Then,
all input parameters can contain a single value or the same number
of values as output camera poses. In the first case, the single
value is used for the computation of all camera poses, while in the
second case the respective value of the element in the parameter is
used for the computation of the corresponding camera pose.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camPosX`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the optical center of the camera.

**`camPosY`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the optical center of the camera.

**`camPosZ`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the optical center of the camera.

**`lookAtX`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the 3D point to which the camera
is directed.

**`lookAtY`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the 3D point to which the camera
is directed.

**`lookAtZ`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the 3D point to which the camera
is directed.

**`refPlaneNormal`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / double)

Normal vector of the reference plane (points up).

Default:
"-y"

List of values:
"-x", "-y", "-z", "x", "y", "z"

**`camRoll`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Camera roll angle.

Default:
0

**`camPose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D camera pose.

## Result

If the parameters are valid, the operator
`CreateCamPoseLookAtPoint` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised. If the parameters are chosen such
that the pose is not well defined, the error 8940 is raised.

## Possible Predecessors

`ConvertPoint3dSpherToCart`

## Alternatives

`CreatePose`

## Module

3D Metrology
