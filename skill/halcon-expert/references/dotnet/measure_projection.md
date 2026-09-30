# MeasureProjection (Operator)

## Name

`MeasureProjection` — Extract a gray value profile perpendicular to a rectangle or annular arc.

## Signature

`static void HOperatorSet.MeasureProjection(HObject image, HTuple measureHandle, out HTuple grayValues)`

`HTuple HMeasure.MeasureProjection(HImage image)`

`HTuple HImage.MeasureProjection(HMeasure measureHandle)`

## Description

`MeasureProjection` extracts a one-dimensional gray value
profile perpendicular to a rectangle or annular arc. This is done by
averaging the
gray values in “slices” perpendicular to the major axis of the
rectangle or arc. The sampling is done at subpixel positions in the image
*`image`* at integer row and column distances (in the
coordinate frame of the rectangle) from the center of the rectangle.
Since this involves some calculations which can be used repeatedly
in several projections, the operator [`GenMeasureRectangle2`](gen_measure_rectangle2.md)
is used to perform these calculations only once, thus increasing
the speed of `MeasureProjection` significantly.
Since there is a trade-off between accuracy and speed in the
subpixel calculations of the gray values, different interpolation
schemes can be selected in [`GenMeasureRectangle2`](gen_measure_rectangle2.md) (the
interpolation only influences rectangles not aligned with the image
axes). The measure object generated with
[`GenMeasureRectangle2`](gen_measure_rectangle2.md) is passed in *`measureHandle`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Attention

It should be kept in mind that `MeasureProjection` ignores
the domain of *`image`* for efficiency reasons. If certain
regions in the image should be excluded from the measurement a new
measure object with appropriately modified parameters should be
generated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`measureHandle`** (input_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

**`grayValues`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Gray value profile.

## Result

If the parameter values are correct the operator `MeasureProjection`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`

## Possible Successors

`CloseMeasure`

## Alternatives

`GrayProjections`

## Module

1D Metrology
