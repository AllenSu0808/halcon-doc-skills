# convert_point_3d_spher_to_cart (Operator)

## Name

`convert_point_3d_spher_to_cart` — Convert spherical coordinates of a 3D point to Cartesian
coordinates.

## Signature

`def convert_point_3d_spher_to_cart(longitude: MaybeSequence[float], latitude: MaybeSequence[float], radius: MaybeSequence[float], equat_plane_normal: str, zero_meridian: str) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def convert_point_3d_spher_to_cart_s(longitude: MaybeSequence[float], latitude: MaybeSequence[float], radius: MaybeSequence[float], equat_plane_normal: str, zero_meridian: str) -> Tuple[float, float, float]`

## Description

The operator `convert_point_3d_spher_to_cart` converts the
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
*`equat_plane_normal`* and *`zero_meridian`*.

*`equat_plane_normal`* determines the normal of the equatorial
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
parameter *`zero_meridian`*. For this, the coordinate axis
(lying in the equatorial plane) that points to the zero meridian
must be passed. The following values for *`zero_meridian`* are
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

Only reasonable combinations of *`equat_plane_normal`* and
*`zero_meridian`* are permitted, i.e., the normal of the
equatorial plane must not be parallel to the direction of the zero
meridian. For example, the combination
*`equat_plane_normal`*=*"y"* and
*`zero_meridian`*=*"-y"* is not permitted.

Note that in order to guarantee a consistent conversion back from
Cartesian to spherical coordinates by using
[`convert_point_3d_cart_to_spher`](convert_point_3d_cart_to_spher.md), the same values must be
passed for *`equat_plane_normal`* and *`zero_meridian`* as
were passed to `convert_point_3d_spher_to_cart`.

The operator `convert_point_3d_spher_to_cart` can be used,
for example, to convert a camera position that is given in spherical
coordinates into Cartesian coordinates. The result can then be
utilized to create a complete camera pose by passing the
Cartesian coordinates to [`create_cam_pose_look_at_point`](create_cam_pose_look_at_point.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`longitude`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Longitude of the 3D point.

**`latitude`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Latitude of the 3D point.

Restriction:
`- pi / 2 <= Latitude && Latitude <= pi / 2`

**`radius`** (input_control)  real(-array) `→` MaybeSequence[float]

Radius of the 3D point.

**`equat_plane_normal`** (input_control)  string `→` str

Normal vector of the equatorial plane (points to the
north pole).

Default:
"-y"

List of values:
"-x", "-y", "-z", "x", "y", "z"

**`zero_meridian`** (input_control)  string `→` str

Coordinate axis in the equatorial plane that points
to the zero meridian.

Default:
"-z"

List of values:
"-x", "-y", "-z", "x", "y", "z"

**`x`** (output_control)  real(-array) `→` Sequence[float]

X coordinate of the 3D point.

**`y`** (output_control)  real(-array) `→` Sequence[float]

Y coordinate of the 3D point.

**`z`** (output_control)  real(-array) `→` Sequence[float]

Z coordinate of the 3D point.

## Result

If the parameters are valid, the operator
`convert_point_3d_spher_to_cart` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`get_shape_model_3d_params`

## See also

`convert_point_3d_cart_to_spher`

## Module

3D Metrology
