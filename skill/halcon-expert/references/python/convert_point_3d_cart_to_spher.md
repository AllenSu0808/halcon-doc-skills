# convert_point_3d_cart_to_spher (Operator)

## Name

`convert_point_3d_cart_to_spher` — Convert Cartesian coordinates of a 3D point to spherical
coordinates.

## Signature

`def convert_point_3d_cart_to_spher(x: MaybeSequence[float], y: MaybeSequence[float], z: MaybeSequence[float], equat_plane_normal: str, zero_meridian: str) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def convert_point_3d_cart_to_spher_s(x: MaybeSequence[float], y: MaybeSequence[float], z: MaybeSequence[float], equat_plane_normal: str, zero_meridian: str) -> Tuple[float, float, float]`

## Description

The operator `convert_point_3d_cart_to_spher` converts
Cartesian coordinates of a 3D point, which are given in *`x`*,
*`y`*, and *`z`*, into spherical coordinates. The
spherical coordinates are returned in *`longitude`*,
*`latitude`*, and *`radius`*. The *`longitude`* is
returned in the range $[-\pi,+\pi]$ while the
*`latitude`* is returned in the range
$[-\pi/2,+\pi/2]$. Furthermore, the latitude of
the north pole is $\pi/2$, and hence, the latitude of the
south pole is $-\pi/2$.

The orientation of the spherical coordinate system with respect to
the Cartesian coordinate system can be specified with the parameters
*`equat_plane_normal`* and *`zero_meridian`*.

*`equat_plane_normal`* determines the normal of the equatorial
plane (longitude == 0) pointing to the north pole (positive
latitude) and may take the following values:

- ***"x"*:** —

  The equatorial plane is the yz plane. The positive x axis points
  to the north pole.
- ***"-x"*:** —

  The equatorial plane is the yz plane. The positive x axis points
  to the south pole.
- ***"y"*:** —

  The equatorial plane is the xz plane. The positive y axis points
  to the north pole.
- ***"-y"*:** —

  The equatorial plane is the xz plane. The positive y axis points
  to the south pole.
- ***"z"*:** —

  The equatorial plane is the xy plane. The positive z axis points
  to the north pole.
- ***"-z"*:** —

  The equatorial plane is the xy plane. The positive z axis points
  to the south pole.

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
spherical to Cartesian coordinates by using
[`convert_point_3d_spher_to_cart`](convert_point_3d_spher_to_cart.md), the same values must be
passed for *`equat_plane_normal`* and *`zero_meridian`* as
were passed to `convert_point_3d_cart_to_spher`.

The operator `convert_point_3d_cart_to_spher` can be used, for
example, to convert a given camera position into spherical
coordinates. If multiple camera positions are converted in this way,
one obtains a pose range (in spherical coordinates), which can be
passed to [`create_shape_model_3d`](create_shape_model_3d.md) in order to create a 3D
shape model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`x`** (input_control)  real(-array) `→` MaybeSequence[float]

X coordinate of the 3D point.

**`y`** (input_control)  real(-array) `→` MaybeSequence[float]

Y coordinate of the 3D point.

**`z`** (input_control)  real(-array) `→` MaybeSequence[float]

Z coordinate of the 3D point.

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

**`longitude`** (output_control)  angle.rad(-array) `→` Sequence[float]

Longitude of the 3D point.

**`latitude`** (output_control)  angle.rad(-array) `→` Sequence[float]

Latitude of the 3D point.

**`radius`** (output_control)  real(-array) `→` Sequence[float]

Radius of the 3D point.

## Result

If the parameters are valid, the operator
`convert_point_3d_cart_to_spher` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Successors

`create_shape_model_3d`,
`find_shape_model_3d`

## See also

`convert_point_3d_spher_to_cart`

## Module

3D Metrology
