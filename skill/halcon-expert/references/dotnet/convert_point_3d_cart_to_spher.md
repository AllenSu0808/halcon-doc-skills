# ConvertPoint3dCartToSpher (Operator)

## Name

`ConvertPoint3dCartToSpher` — Convert Cartesian coordinates of a 3D point to spherical
coordinates.

## Signature

`static void HOperatorSet.ConvertPoint3dCartToSpher(HTuple x, HTuple y, HTuple z, HTuple equatPlaneNormal, HTuple zeroMeridian, out HTuple longitude, out HTuple latitude, out HTuple radius)`

`static HTuple HMisc.ConvertPoint3dCartToSpher(HTuple x, HTuple y, HTuple z, string equatPlaneNormal, string zeroMeridian, out HTuple latitude, out HTuple radius)`

`static double HMisc.ConvertPoint3dCartToSpher(double x, double y, double z, string equatPlaneNormal, string zeroMeridian, out double latitude, out double radius)`

## Description

The operator `ConvertPoint3dCartToSpher` converts
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
*`equatPlaneNormal`* and *`zeroMeridian`*.

*`equatPlaneNormal`* determines the normal of the equatorial
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
spherical to Cartesian coordinates by using
[`ConvertPoint3dSpherToCart`](convert_point_3d_spher_to_cart.md), the same values must be
passed for *`equatPlaneNormal`* and *`zeroMeridian`* as
were passed to `ConvertPoint3dCartToSpher`.

The operator `ConvertPoint3dCartToSpher` can be used, for
example, to convert a given camera position into spherical
coordinates. If multiple camera positions are converted in this way,
one obtains a pose range (in spherical coordinates), which can be
passed to [`CreateShapeModel3d`](create_shape_model_3d.md) in order to create a 3D
shape model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`x`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the 3D point.

**`y`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the 3D point.

**`z`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the 3D point.

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

**`longitude`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Longitude of the 3D point.

**`latitude`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Latitude of the 3D point.

**`radius`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Radius of the 3D point.

## Result

If the parameters are valid, the operator
`ConvertPoint3dCartToSpher` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Successors

`CreateShapeModel3d`,
`FindShapeModel3d`

## See also

`ConvertPoint3dSpherToCart`

## Module

3D Metrology
