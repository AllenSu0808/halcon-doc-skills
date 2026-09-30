# EstimateTiltZc (Operator)

## Name

`EstimateTiltZc` — Estimate the tilt of a light source.

## Signature

`static void HOperatorSet.EstimateTiltZc(HObject image, out HTuple tilt)`

`HTuple HImage.EstimateTiltZc()`

## Description

`EstimateTiltZc` estimates the tilt of a light source,
i.e. the angle between the light source and the x-axis after
projection into the xy-plane, from the image *`image`* using
the algorithm of Zheng and Chellappa.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Image for which the tilt is to be estimated.

**`tilt`** (output_control)  angle.deg(-array) `→` [HTuple](HTuple.md) (*double*)

Angle between the light source and the x-axis after
projection into the xy-plane (in degrees).

## Result

`EstimateTiltZc` always returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`SfsModLr`,
`SfsOrigLr`,
`SfsPentland`,
`PhotometricStereo`,
`ShadeHeightField`

## Module

3D Metrology
