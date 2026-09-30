# EstimateSlAlLr (Operator)

## Name

`EstimateSlAlLr` — Estimate the slant of a light source and the albedo of a surface.

## Signature

`static void HOperatorSet.EstimateSlAlLr(HObject image, out HTuple slant, out HTuple albedo)`

`HTuple HImage.EstimateSlAlLr(out HTuple albedo)`

`double HImage.EstimateSlAlLr(out double albedo)`

## Description

`EstimateSlAlLr` estimates the *`slant`* of a
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

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Image for which slant and albedo are to be estimated.

**`slant`** (output_control)  angle.deg(-array) `→` [HTuple](HTuple.md) (*double*)

Angle between the light sources and the positive z-axis
(in degrees).

**`albedo`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Amount of light reflected by the surface.

## Result

`EstimateSlAlLr` always returns the value 2 (
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
