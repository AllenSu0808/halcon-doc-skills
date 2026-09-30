# EstimateAlAm (Operator)

## Name

`EstimateAlAm` — Estimate the albedo of a surface and the amount of ambient light.

## Signature

`static void HOperatorSet.EstimateAlAm(HObject image, out HTuple albedo, out HTuple ambient)`

`HTuple HImage.EstimateAlAm(out HTuple ambient)`

`double HImage.EstimateAlAm(out double ambient)`

## Description

`EstimateAlAm` estimates the *`albedo`* of a
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

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Image for which albedo and ambient are to be estimated.

**`albedo`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Amount of light reflected by the surface.

**`ambient`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Amount of ambient light.

## Result

`EstimateAlAm` always returns the value 2 (
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
