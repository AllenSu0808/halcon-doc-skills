# estimate_sl_al_lr (Operator)

## Name

`estimate_sl_al_lr` — Estimate the slant of a light source and the albedo of a surface.

## Signature

`def estimate_sl_al_lr(image: HObject) -> Tuple[Sequence[float], Sequence[float]]`

`def estimate_sl_al_lr_s(image: HObject) -> Tuple[float, float]`

## Description

`estimate_sl_al_lr` estimates the *`slant`* of a
light source, i.e., the angle between the light source and the positive
z-axis, and the albedo of the surface in the input image
*`image`*, i.e. the percentage of light reflected by the
surface, using the algorithm of Lee and Rosenfeld.

## Attention

The *`albedo`* is assumed constant for the entire surface
depicted in the image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Image for which slant and albedo are to be estimated.

**`slant`** (output_control)  angle.deg(-array) `→` Sequence[float]

Angle between the light sources and the positive z-axis
(in degrees).

**`albedo`** (output_control)  real(-array) `→` Sequence[float]

Amount of light reflected by the surface.

## Result

`estimate_sl_al_lr` always returns the value 2 (
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
