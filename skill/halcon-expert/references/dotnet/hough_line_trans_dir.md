# HoughLineTransDir (Operator)

## Name

`HoughLineTransDir` — Compute the Hough transform for lines using local gradient direction.

## Signature

`static void HOperatorSet.HoughLineTransDir(HObject imageDir, out HObject houghImage, HTuple directionUncertainty, HTuple angleResolution)`

`HImage HImage.HoughLineTransDir(int directionUncertainty, int angleResolution)`

## Description

The operator `HoughLineTransDir` calculates the Hough transform for
lines in those regions passed in the domain of *`imageDir`*.
To do so, the angles and the lengths of the lines' normal vectors are
registered in the parameter space (the so-called Hough or accumulator
space).

In contrast to [`HoughLineTrans`](hough_line_trans.md), additionally the edge direction in
*`imageDir`* (e.g., returned by [`SobelDir`](sobel_dir.md) or
[`EdgesImage`](edges_image.md)) is taken into account. This results in a more efficient
computation and in a reduction of the noise in the Hough space.

The parameter *`directionUncertainty`* describes how much the edge
direction of the individual points within a line is allowed to vary. For
example, with *`directionUncertainty`* = *10* a horizontal
line (i.e., edge direction = 0 degrees) may contain points with an edge
direction between -10 and +10 degrees. The higher
*`directionUncertainty`* is chosen, the higher the computation time
will be. For *`directionUncertainty`* = *180*
`HoughLineTransDir` shows the same behavior as
[`HoughLineTrans`](hough_line_trans.md), i.e., the edge direction is ignored.
*`directionUncertainty`* should be chosen at least as high as the
step width of the edge direction stored in *`imageDir`*. The minimum
step width is 2 degrees (defined by the image type 'direction').

The result is stored in a newly generated UINT2-Image
(*`houghImage`*), where the x-axis (i.e., columns) represents the
angle between the normal vector and the x-axis of the original image, and the
y-axis (i.e., rows) represents the distance of the line from the origin.

The angle ranges from -90 to 180 degrees and will be stored with a
resolution of 1 / *`angleResolution`*, which means that one pixel
in x-direction is equivalent to 1 / *`angleResolution`* degrees
and that the *`houghImage`* has a width of
270 * *`angleResolution`*
+ 1 pixels. The height of the *`houghImage`* corresponds to the
distance between the lower right corner of the surrounding rectangle
of the input region and the origin.

The local maxima in the result image are equivalent to the parameter
values of the lines in the original image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageDir`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (direction)

Image containing the edge direction. The edges must be
described by the image domain.

**`houghImage`** (output_object)  image `→` [HImage](HImage.md) (uint2)

Hough transform.

**`directionUncertainty`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*int* / long)

Uncertainty of the edge direction (in degrees).

Default:
2

Value range:
`2
≤
directionUncertainty
≤
180`

Minimum increment:
2

**`angleResolution`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Resolution in the angle area (in 1/degrees).

Default:
4

List of values:
1, 2, 4, 8

## Result

The operator `HoughLineTransDir` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`EdgesImage`,
`SobelDir`,
`Threshold`,
`HysteresisThreshold`,
`NonmaxSuppressionDir`,
`ReduceDomain`

## Possible Successors

`BinomialFilter`,
`GaussFilter`,
`Threshold`,
`LocalMax`,
`PlateausCenter`

## See also

`HoughLineTrans`,
`HoughLines`,
`HoughLinesDir`

## Module

Foundation
