# hough_line_trans_dir (Operator)

## Name

`hough_line_trans_dir` — Compute the Hough transform for lines using local gradient direction.

## Signature

`hough_line_trans_dir(ImageDir : HoughImage : DirectionUncertainty, AngleResolution : )`

## Description

The operator `hough_line_trans_dir` calculates the Hough transform for
lines in those regions passed in the domain of *`ImageDir`*.
To do so, the angles and the lengths of the lines' normal vectors are
registered in the parameter space (the so-called Hough or accumulator
space).

In contrast to [`hough_line_trans`](hough_line_trans.md), additionally the edge direction in
*`ImageDir`* (e.g., returned by [`sobel_dir`](sobel_dir.md) or
[`edges_image`](edges_image.md)) is taken into account. This results in a more efficient
computation and in a reduction of the noise in the Hough space.

The parameter *`DirectionUncertainty`* describes how much the edge
direction of the individual points within a line is allowed to vary. For
example, with *`DirectionUncertainty`* = *10* a horizontal
line (i.e., edge direction = 0 degrees) may contain points with an edge
direction between -10 and +10 degrees. The higher
*`DirectionUncertainty`* is chosen, the higher the computation time
will be. For *`DirectionUncertainty`* = *180*
`hough_line_trans_dir` shows the same behavior as
[`hough_line_trans`](hough_line_trans.md), i.e., the edge direction is ignored.
*`DirectionUncertainty`* should be chosen at least as high as the
step width of the edge direction stored in *`ImageDir`*. The minimum
step width is 2 degrees (defined by the image type 'direction').

The result is stored in a newly generated UINT2-Image
(*`HoughImage`*), where the x-axis (i.e., columns) represents the
angle between the normal vector and the x-axis of the original image, and the
y-axis (i.e., rows) represents the distance of the line from the origin.

The angle ranges from -90 to 180 degrees and will be stored with a
resolution of 1 / *`AngleResolution`*, which means that one pixel
in x-direction is equivalent to 1 / *`AngleResolution`* degrees
and that the *`HoughImage`* has a width of
270 * *`AngleResolution`*
+ 1 pixels. The height of the *`HoughImage`* corresponds to the
distance between the lower right corner of the surrounding rectangle
of the input region and the origin.

The local maxima in the result image are equivalent to the parameter
values of the lines in the original image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageDir`** (input_object)  singlechannelimage `→` object (direction)

Image containing the edge direction. The edges must be
described by the image domain.

**`HoughImage`** (output_object)  image `→` object (uint2)

Hough transform.

**`DirectionUncertainty`** (input_control)  angle.deg `→`  (integer)

Uncertainty of the edge direction (in degrees).

Default:
2

Value range:
`2
≤
DirectionUncertainty
≤
180`

Minimum increment:
2

**`AngleResolution`** (input_control)  integer `→`  (integer)

Resolution in the angle area (in 1/degrees).

Default:
4

List of values:
1, 2, 4, 8

## Result

The operator `hough_line_trans_dir` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`edges_image`,
`sobel_dir`,
`threshold`,
`hysteresis_threshold`,
`nonmax_suppression_dir`,
`reduce_domain`

## Possible Successors

`binomial_filter`,
`gauss_filter`,
`threshold`,
`local_max`,
`plateaus_center`

## See also

`hough_line_trans`,
`hough_lines`,
`hough_lines_dir`

## Module

Foundation
