# estimate_tilt_lr (Operator)

## Name

`estimate_tilt_lr` — Estimate the tilt of a light source.

## Signature

`def estimate_tilt_lr(image: HObject) -> Sequence[float]`

`def estimate_tilt_lr_s(image: HObject) -> float`

## Description

`estimate_tilt_lr` estimates the tilt of a light source,
i.e. the angle between the light source and the x-axis after
projection into the xy-plane, from the image *`image`* using
the algorithm of Lee and Rosenfeld.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Image for which the tilt is to be estimated.

**`tilt`** (output_control)  angle.deg(-array) `→` Sequence[float]

Angle between the light source and the x-axis after
projection into the xy-plane (in degrees).

## Result

`estimate_tilt_lr` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`sfs_mod_lr`,
`sfs_orig_lr`,
`sfs_pentland`,
`photometric_stereo`,
`shade_height_field`

## Module

3D Metrology
