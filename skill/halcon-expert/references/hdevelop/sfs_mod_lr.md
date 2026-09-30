# sfs_mod_lr (Operator)

## Name

`sfs_mod_lr` — Reconstruct a surface from a gray value image.

## Signature

`sfs_mod_lr(Image : Height : Slant, Tilt, Albedo, Ambient : )`

## Description

`sfs_mod_lr` reconstructs a surface (i.e. the relative
height of each image point) using the modified algorithm of Lee and
Rosenfeld. The surface is reconstructed from the input image
*`Image`*, and the light source given by the parameters
*`Slant`*, *`Tilt`*, *`Albedo`* and
*`Ambient`*, and is assumed to lie infinitely far away in the
direction given by *`Slant`* and *`Tilt`*. The
parameter *`Albedo`* determines the albedo of the surface,
i.e. the percentage of light reflected in all directions.
*`Ambient`* determines the amount of ambient light falling
onto the surface. It can be set to values greater than zero if, for
example, the white balance of the camera was badly adjusted at the
moment the image was taken.

## Attention

`sfs_mod_lr` assumes that the heights are to be extracted on a
lattice with step width 1. If this is not the case, the calculated
heights must be multiplied with the step width after the call to
`sfs_mod_lr`. A Cartesian coordinate system with the origin
in the lower left corner of the image is used internally.
`sfs_mod_lr` can only handle byte-images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Shaded input image.

**`Height`** (output_object)  image(-array) `→` object (real)

Reconstructed height field.

**`Slant`** (input_control)  angle.deg `→`  (real / integer)

Angle between the light source and the positive z-axis
(in degrees).

Default:
45.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
Slant
≤
180.0` (lin)

Minimum increment:
0.01

Recommended increment:
10.0

**`Tilt`** (input_control)  angle.deg `→`  (real / integer)

Angle between the light source and the x-axis after
projection into the xy-plane (in degrees).

Default:
45.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
Tilt
≤
360.0` (lin)

Minimum increment:
0.01

Recommended increment:
10.0

**`Albedo`** (input_control)  number `→`  (real / integer)

Amount of light reflected by the surface.

Default:
1.0

Suggested values:
0.1, 0.5, 1.0, 5.0

Value range:
`0.0
≤
Albedo
≤
5.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Albedo >= 0.0`

**`Ambient`** (input_control)  number `→`  (real / integer)

Amount of ambient light.

Default:
0.0

Suggested values:
0.1, 0.5, 1.0

Value range:
`0.0
≤
Ambient
≤
1.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Ambient >= 0.0`

## Result

If all parameters are correct `sfs_mod_lr` returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`estimate_al_am`,
`estimate_sl_al_lr`,
`estimate_sl_al_zc`,
`estimate_tilt_lr`,
`estimate_tilt_zc`,
`optimize_fft_speed`

## Possible Successors

`shade_height_field`

## Module

3D Metrology
