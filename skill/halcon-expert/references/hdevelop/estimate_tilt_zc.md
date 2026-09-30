# estimate_tilt_zc (Operator)

## Name

`estimate_tilt_zc` — Estimate the tilt of a light source.

## Signature

`estimate_tilt_zc(Image : : : Tilt)`

## Description

`estimate_tilt_zc` estimates the tilt of a light source,
i.e. the angle between the light source and the x-axis after
projection into the xy-plane, from the image *`Image`* using
the algorithm of Zheng and Chellappa.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Image for which the tilt is to be estimated.

**`Tilt`** (output_control)  angle.deg(-array) `→`  (real)

Angle between the light source and the x-axis after
projection into the xy-plane (in degrees).

## Result

`estimate_tilt_zc` always returns the value 2 (
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
