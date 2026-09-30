# EstimateSlAlZc (Operator)

## Name

`EstimateSlAlZc` — Estimate the slant of a light source and the albedo of a surface.

## Signature

`static void HOperatorSet.EstimateSlAlZc(HObject image, out HTuple slant, out HTuple albedo)`

`HTuple HImage.EstimateSlAlZc(out HTuple albedo)`

`double HImage.EstimateSlAlZc(out double albedo)`

## Description

`EstimateSlAlZc` estimates the *`slant`* of a
light source, i.e. the angle between the light source and the positive
z-axis, and the albedo of the surface in the input image
*`image`*, i.e. the percentage of light reflected by the
surface, using the algorithm of Zheng and Chellappa.

## Attention

The *`albedo`* is assumed constant for the entire surface
depicted in the image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Image for which slant and albedo are to be estimated.

**`slant`** (output_control)  angle.deg(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the light sources and the positive z-axis
(in degrees).

**`albedo`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Amount of light reflected by the surface.

## Result

`EstimateSlAlZc` always returns the value 2 (
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
