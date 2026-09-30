# shade_height_field (Operator)

## Name

`shade_height_field` — Shade a height field.

## Signature

`def shade_height_field(image_height: HObject, slant: Union[float, int], tilt: Union[float, int], albedo: Union[float, int], ambient: Union[float, int], shadows: str) -> HObject`

## Description

`shade_height_field` computes a shaded image from the
height field *`image_height`* as if the image were illuminated
by an infinitely far away light source. It is assumed that the
surface described by the height field has Lambertian reflection
properties determined by *`albedo`* and *`ambient`*.
The parameter *`shadows`* determines whether shadows are to
be calculated.

## Attention

`shade_height_field` assumes that the heights are given
on a lattice with step width 1. If this is not the case, the
heights must be divided by the step width before the call to
`shade_height_field`. Otherwise, the derivatives used
internally to compute the orientation of the surface will be
estimated to steep or too flat. Example: The height field is given
on 100*100 points on the square [0,1]*[0,1]. Then the heights must
be divided by 1/100 first. A Cartesian coordinate system with the
origin in the lower left corner of the image is used internally.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image_height`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int4 / real)

Height field to be shaded.

**`image_shade`** (output_object)  image(-array) `→` HObject (byte)

Shaded image.

**`slant`** (input_control)  angle.deg `→` Union[float, int]

Angle between the light source and the positive z-axis
(in degrees).

Default:
0.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
slant
≤
180.0` (lin)

Minimum increment:
0.01

Recommended increment:
10.0

**`tilt`** (input_control)  angle.deg `→` Union[float, int]

Angle between the light source and the x-axis after
projection into the xy-plane (in degrees).

Default:
0.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
tilt
≤
360.0` (lin)

Minimum increment:
0.01

Recommended increment:
10.0

**`albedo`** (input_control)  number `→` Union[float, int]

Amount of light reflected by the surface.

Default:
1.0

Suggested values:
0.1, 0.5, 1.0, 5.0

Value range:
`0.0
≤
albedo
≤
5.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Albedo >= 0.0`

**`ambient`** (input_control)  number `→` Union[float, int]

Amount of ambient light.

Default:
0.0

Suggested values:
0.1, 0.5, 1.0

Value range:
`0.0
≤
ambient
≤
1.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Ambient >= 0.0`

**`shadows`** (input_control)  string `→` str

Should shadows be calculated?

Default:
"false"

Suggested values:
"true", "false"

## Result

If all parameters are correct `shade_height_field` returns
the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`sfs_mod_lr`,
`sfs_orig_lr`,
`sfs_pentland`,
`photometric_stereo`

## Module

Foundation
