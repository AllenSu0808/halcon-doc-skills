# estimate_al_am (Operator)

## Name

`estimate_al_am` — Estimate the albedo of a surface and the amount of ambient light.

## Signature

`def estimate_al_am(image: HObject) -> Tuple[Sequence[float], Sequence[float]]`

`def estimate_al_am_s(image: HObject) -> Tuple[float, float]`

## Description

`estimate_al_am` estimates the *`albedo`* of a
surface, i.e. the percentage of light reflected by the surface, and
the amount of ambient light *`ambient`* by using the maximum
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

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Image for which albedo and ambient are to be estimated.

**`albedo`** (output_control)  real(-array) `→` Sequence[float]

Amount of light reflected by the surface.

**`ambient`** (output_control)  real(-array) `→` Sequence[float]

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
