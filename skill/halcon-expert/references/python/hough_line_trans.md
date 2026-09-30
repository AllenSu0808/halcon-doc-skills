# hough_line_trans (Operator)

## Name

`hough_line_trans` — Produce the Hough transform for lines within regions.

## Signature

`def hough_line_trans(region: HObject, angle_resolution: int) -> HObject`

## Description

The operator `hough_line_trans` calculates the Hough transform for
lines in those regions transmitted by *`region`*. Thereby the angles
and the lengths of the lines' normal vectors are registered in the parameter
space (the Hough- or accumulator space respectively). This means that the
parametrization is executed according to the HNF.

The result is registered in a newly generated Int2-Image
(*`hough_image`*), whereby the x-axis is equivalent to the angle between
the normal vector and the x-axis (in the original image), and the y-axis is
equivalent to the distance of the line from the origin.

The angle ranges from -90 to 180 degrees and will be registered with a
resolution of 1 / *`angle_resolution`*, which means that one pixel
in x-direction is equivalent to 1 / *`angle_resolution`* and that
the *`hough_image`* has a width of 270 * *`angle_resolution`*
+ 1 pixel. The height of the *`hough_image`* corresponds to the
distance between the lower right corner of the surrounding rectangle
of the input region and the origin.

The maxima in the result image are equivalent to the parameter values of
the lines in the original image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Binary edge image in which lines are to be detected.

**`hough_image`** (output_object)  image `→` HObject (int2)

Hough transform for lines.

**`angle_resolution`** (input_control)  integer `→` int

Adjusting the resolution in the angle area.

Default:
4

List of values:
1, 2, 4, 8

## Result

The operator `hough_line_trans` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`skeleton`

## Possible Successors

`threshold`,
`local_max`

## See also

`hough_circle_trans`,
`gen_region_hline`

## Module

Foundation
