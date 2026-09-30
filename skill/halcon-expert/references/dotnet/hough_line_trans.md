# HoughLineTrans (Operator)

## Name

`HoughLineTrans` — Produce the Hough transform for lines within regions.

## Signature

`static void HOperatorSet.HoughLineTrans(HObject region, out HObject houghImage, HTuple angleResolution)`

`HImage HRegion.HoughLineTrans(int angleResolution)`

## Description

The operator `HoughLineTrans` calculates the Hough transform for
lines in those regions transmitted by *`region`*. Thereby the angles
and the lengths of the lines' normal vectors are registered in the parameter
space (the Hough- or accumulator space respectively). This means that the
parametrization is executed according to the HNF.

The result is registered in a newly generated Int2-Image
(*`houghImage`*), whereby the x-axis is equivalent to the angle between
the normal vector and the x-axis (in the original image), and the y-axis is
equivalent to the distance of the line from the origin.

The angle ranges from -90 to 180 degrees and will be registered with a
resolution of 1 / *`angleResolution`*, which means that one pixel
in x-direction is equivalent to 1 / *`angleResolution`* and that
the *`houghImage`* has a width of 270 * *`angleResolution`*
+ 1 pixel. The height of the *`houghImage`* corresponds to the
distance between the lower right corner of the surrounding rectangle
of the input region and the origin.

The maxima in the result image are equivalent to the parameter values of
the lines in the original image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Binary edge image in which lines are to be detected.

**`houghImage`** (output_object)  image `→` [HImage](HImage.md) (int2)

Hough transform for lines.

**`angleResolution`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Adjusting the resolution in the angle area.

Default:
4

List of values:
1, 2, 4, 8

## Result

The operator `HoughLineTrans` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Skeleton`

## Possible Successors

`Threshold`,
`LocalMax`

## See also

`HoughCircleTrans`,
`GenRegionHline`

## Module

Foundation
