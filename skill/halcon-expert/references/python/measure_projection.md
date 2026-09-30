# measure_projection (Operator)

## Name

`measure_projection` — Extract a gray value profile perpendicular to a rectangle or annular arc.

## Signature

`def measure_projection(image: HObject, measure_handle: HHandle) -> Sequence[float]`

## Description

`measure_projection` extracts a one-dimensional gray value
profile perpendicular to a rectangle or annular arc. This is done by
averaging the
gray values in “slices” perpendicular to the major axis of the
rectangle or arc. The sampling is done at subpixel positions in the image
*`image`* at integer row and column distances (in the
coordinate frame of the rectangle) from the center of the rectangle.
Since this involves some calculations which can be used repeatedly
in several projections, the operator [`gen_measure_rectangle2`](gen_measure_rectangle2.md)
is used to perform these calculations only once, thus increasing
the speed of `measure_projection` significantly.
Since there is a trade-off between accuracy and speed in the
subpixel calculations of the gray values, different interpolation
schemes can be selected in [`gen_measure_rectangle2`](gen_measure_rectangle2.md) (the
interpolation only influences rectangles not aligned with the image
axes). The measure object generated with
[`gen_measure_rectangle2`](gen_measure_rectangle2.md) is passed in *`measure_handle`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

## Attention

It should be kept in mind that `measure_projection` ignores
the domain of *`image`* for efficiency reasons. If certain
regions in the image should be excluded from the measurement a new
measure object with appropriately modified parameters should be
generated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Input image.

**`measure_handle`** (input_control)  measure `→` HHandle

Measure object handle.

**`gray_values`** (output_control)  number-array `→` Sequence[float]

Gray value profile.

## Result

If the parameter values are correct the operator `measure_projection`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`

## Possible Successors

`close_measure`

## Alternatives

`gray_projections`

## Module

1D Metrology
