# ConvertPoint3dSpherToCart (Operator)

## Name

`ConvertPoint3dSpherToCart` — Convert spherical coordinates of a 3D point to Cartesian
coordinates.

## Signature

`static void HOperatorSet.ConvertPoint3dSpherToCart(HTuple longitude, HTuple latitude, HTuple radius, HTuple equatPlaneNormal, HTuple zeroMeridian, out HTuple x, out HTuple y, out HTuple z)`

`static void HMisc.ConvertPoint3dSpherToCart(HTuple longitude, HTuple latitude, HTuple radius, string equatPlaneNormal, string zeroMeridian, out HTuple x, out HTuple y, out HTuple z)`

`static void HMisc.ConvertPoint3dSpherToCart(double longitude, double latitude, double radius, string equatPlaneNormal, string zeroMeridian, out double x, out double y, out double z)`

## Description

The operator `ConvertPoint3dSpherToCart` converts the
spherical coordinates of a 3D point, which are given in
*`longitude`*, *`latitude`*, and *`radius`*, into the
Cartesian coordinates *`x`*, *`y`*, and *`z`*. The
spherical coordinates *`longitude`* and *`latitude`* must
be specified in radians. Furthermore, the *`latitude`* must be
within the range $[-\pi/2,+\pi/2]$, where the
latitude of the north pole is $\pi/2$, and hence, the
latitude of the south pole is $-\pi/2$.

The orientation of the spherical coordinate system with respect to
the Cartesian coordinate system can be specified with the parameters
*`equatPlaneNormal`* and *`zeroMeridian`*.

*`equatPlaneNormal`* determines the normal of the equatorial
plane (longitude == 0) pointing to the north pole (positive
latitude) and may take the following values:

- ***"x"*:** —

  The equatorial plane is the yz plane. The
  positive x axis points to the north pole.
- ***"-x"*:** —

  The equatorial plane is the yz plane. The
  positive x axis points to the south pole.
- ***"y"*:** —

  The equatorial plane is the xz plane. The
  positive y axis points to the north pole.
- ***"-y"*:** —

  The equatorial plane is the xz plane. The
  positive y axis points to the south pole.
- ***"z"*:** —

  The equatorial plane is the xy plane. The
  positive z axis points to the north pole.
- ***"-z"*:** —

  The equatorial plane is the xy plane. The
  positive z axis points to the south pole.

The position of the zero meridian can be specified with the
parameter *`zeroMeridian`*. For this, the coordinate axis
(lying in the equatorial plane) that points to the zero meridian
must be passed. The following values for *`zeroMeridian`* are
valid:

- ***"x"*:** —

  The *positive* x axis points in the direction of the zero
  meridian.
- ***"-x"*:** —

  The *negative* x axis points in the direction of the zero
  meridian.
- ***"y"*:** —

  The *positive* y axis points in the direction of the zero
  meridian.
- ***"-y"*:** —

  The *negative* y axis points in the direction of the zero
  meridian.
- ***"z"*:** —

  The *positive* z axis points in the direction of the zero
  meridian.
- ***"-z"*:** —

  The *negative* z axis points in the direction of the zero
  meridian.

Only reasonable combinations of *`equatPlaneNormal`* and
*`zeroMeridian`* are permitted, i.e., the normal of the
equatorial plane must not be parallel to the direction of the zero
meridian. For example, the combination
*`equatPlaneNormal`*=*"y"* and
*`zeroMeridian`*=*"-y"* is not permitted.

Note that in order to guarantee a consistent conversion back from
Cartesian to spherical coordinates by using
[`ConvertPoint3dCartToSpher`](convert_point_3d_cart_to_spher.md), the same values must be
passed for *`equatPlaneNormal`* and *`zeroMeridian`* as
were passed to `ConvertPoint3dSpherToCart`.

The operator `ConvertPoint3dSpherToCart` can be used,
for example, to convert a camera position that is given in spherical
coordinates into Cartesian coordinates. The result can then be
utilized to create a complete camera pose by passing the
Cartesian coordinates to [`CreateCamPoseLookAtPoint`](create_cam_pose_look_at_point.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`longitude`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Longitude of the 3D point.

**`latitude`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Latitude of the 3D point.

Restriction:
`- pi / 2 <= Latitude && Latitude <= pi / 2`

**`radius`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Radius of the 3D point.

**`equatPlaneNormal`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Normal vector of the equatorial plane (points to the
north pole).

Default:
"-y"

List of values:
"-x", "-y", "-z", "x", "y", "z"

**`zeroMeridian`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Coordinate axis in the equatorial plane that points
to the zero meridian.

Default:
"-z"

List of values:
"-x", "-y", "-z", "x", "y", "z"

**`x`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the 3D point.

**`y`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the 3D point.

**`z`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the 3D point.

## Result

If the parameters are valid, the operator
`ConvertPoint3dSpherToCart` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`GetShapeModel3dParams`

## See also

`ConvertPoint3dCartToSpher`

## Module

3D Metrology
