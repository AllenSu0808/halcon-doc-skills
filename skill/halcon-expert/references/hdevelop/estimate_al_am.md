# estimate_al_am (Operator)

## Name

`estimate_al_am` — Estimate the albedo of a surface and the amount of ambient light.

## Signature

`estimate_al_am(Image : : : Albedo, Ambient)`

## Description

`estimate_al_am` estimates the *`Albedo`* of a
surface, i.e. the percentage of light reflected by the surface, and
the amount of ambient light *`Ambient`* by using the maximum
and minimum gray values of the image.

## Attention

It is assumed that the image contains at least one point for which
the reflection function assumes its minimum, e.g., points in
shadows. Furthermore, it is assumed that the image contains at
least one point for which the reflection function assumes its
maximum. If this is not the case, wrong values will be
estimated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Image for which albedo and ambient are to be estimated.

**`Albedo`** (output_control)  real(-array) `→`  (real)

Amount of light reflected by the surface.

**`Ambient`** (output_control)  real(-array) `→`  (real)

Amount of ambient light.

## Result

`estimate_al_am` always returns the value 2 (
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
