# estimate_sl_al_zc (Operator)

## Name

`estimate_sl_al_zc` — Estimate the slant of a light source and the albedo of a surface.

## Signature

`estimate_sl_al_zc(Image : : : Slant, Albedo)`

## Description

`estimate_sl_al_zc` estimates the *`Slant`* of a
light source, i.e. the angle between the light source and the positive
z-axis, and the albedo of the surface in the input image
*`Image`*, i.e. the percentage of light reflected by the
surface, using the algorithm of Zheng and Chellappa.

## Attention

The *`Albedo`* is assumed constant for the entire surface
depicted in the image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Image for which slant and albedo are to be estimated.

**`Slant`** (output_control)  angle.deg(-array) `→`  (real)

Angle of the light sources and the positive z-axis
(in degrees).

**`Albedo`** (output_control)  real(-array) `→`  (real)

Amount of light reflected by the surface.

## Result

`estimate_sl_al_zc` always returns the value 2 (
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
