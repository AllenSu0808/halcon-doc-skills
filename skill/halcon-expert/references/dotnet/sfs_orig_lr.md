# SfsOrigLr (Operator)

## Name

`SfsOrigLr` — Reconstruct a surface from a gray value image.

## Signature

`static void HOperatorSet.SfsOrigLr(HObject image, out HObject height, HTuple slant, HTuple tilt, HTuple albedo, HTuple ambient)`

`HImage HImage.SfsOrigLr(HTuple slant, HTuple tilt, HTuple albedo, HTuple ambient)`

`HImage HImage.SfsOrigLr(double slant, double tilt, double albedo, double ambient)`

## Description

`SfsOrigLr` reconstructs a surface (i.e. the relative
height of each image point) using the original algorithm of Lee and
Rosenfeld. The surface is reconstructed from the input image
*`image`*. The light source is to be given by the parameters
*`slant`*, *`tilt`*, *`albedo`* and
*`ambient`*, and is assumed to lie infinitely far away in the
direction given by *`slant`* and *`tilt`*. The
parameter *`albedo`* determines the albedo of the surface,
i.e. the percentage of light reflected in all directions.
*`ambient`* determines the amount of ambient light falling
onto the surface. It can be set to values greater than zero if, for
example, the white balance of the camera was badly adjusted at the
moment the image was taken.

## Attention

`SfsOrigLr` assumes that the heights are to be extracted on
a lattice with step width 1. If this is not the case, the
calculated heights must be multiplied with the step width after the
call to `SfsOrigLr`. A Cartesian coordinate system with the
origin in the lower left corner of the image is used internally.
`SfsOrigLr` can only handle byte-images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Shaded input image.

**`height`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Reconstructed height field.

**`slant`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Angle between the light source and the positive z-axis
(in degrees).

Default:
45.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
slant
≤
90.0`

Minimum increment:
0.01

Recommended increment:
10.0

**`tilt`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Angle between the light source and the x-axis after
projection into the xy-plane (in degrees).

Default:
45.0

Suggested values:
1.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
tilt
≤
360.0`

Minimum increment:
0.01

Recommended increment:
10.0

**`albedo`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`ambient`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

## Result

If all parameters are correct `SfsOrigLr` returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`EstimateAlAm`,
`EstimateSlAlLr`,
`EstimateSlAlZc`,
`EstimateTiltLr`,
`EstimateTiltZc`,
`OptimizeFftSpeed`

## Possible Successors

`ShadeHeightField`

## Module

3D Metrology
