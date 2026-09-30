# gray_projections (Operator)

## Name

`gray_projections` — Calculate horizontal and vertical gray-value projections.

## Signature

`gray_projections(Region, Image : : Mode : HorProjection, VertProjection)`

## Description

`gray_projections` calculates the horizontal and vertical
gray-value projections, i.e., the mean values in the horizontal and
vertical direction of the gray values of the input image
*`Image`* within the input region *`Region`*.

If *`Mode`* = *'simple'* is selected the projection is
performed in the direction of the coordinate axes of the image,
i.e.:
$$HorProjection(r) = \frac{1}{n(r + r')} \sum_{(r + r', c + c') \in Region} Image(r + r', c + c') VertProjection(c) = \frac{1}{n(c + c')} \sum_{(r + r', c + c') \in Region} Image(r + r', c + c')$$ ![figure](../assets/5b87d2b15aef9ba9.svg)
Here, (r',c') denotes the upper left corner of the smallest
enclosing axis-parallel rectangle of the input region (see
[`smallest_rectangle1`](smallest_rectangle1.md)), and n(x) denotes the number of region
points in the corresponding row r+r' or column c+c'. Hence,
the horizontal projection
returns a one-dimensional function that reflects the vertical gray
value changes. Likewise, the vertical projection returns a function
that reflects the horizontal gray value changes.

If *`Mode`* = *'rectangle'*is selected the projection is
performed in the direction of the major axes of the smallest
enclosing rectangle of arbitrary orientation of the input region
(see [`smallest_rectangle2`](smallest_rectangle2.md)). Here, the horizontal projection
direction corresponds to the larger axis, while the vertical
direction corresponds to the smaller axis. In this mode, all gray
values within the smallest enclosing rectangle of arbitrary
orientation of the input region are used to compute the
projections.

## Attention

The operator `gray_projections` only considers the given
*`Region`* and ignores any previously set domain of the input
image *`Image`*.

If n(x) = 0, i.e., if there are no region points in the
corresponding row r+r' or column c+c', the respective value of
*`HorProjection`* or *`VertProjection`* is set to -1.

`gray_projections` can be executed on an OpenCL device for the
*'simple'* mode if the OpenCL device supports the
cl_khr_global_int32_base_atomics OpenCL extension. For processing images of
type real, the OpenCL device must support the cl_khr_fp64 and
cl_khr_int64_base_atomics extensions.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

Region to be processed.

**`Image`** (input_object)  singlechannelimage `→` object (byte* / int2* / uint2* / real*) **allowed for compute devices*

Grayvalues for projections.

**`Mode`** (input_control)  string `→`  (string)

Method to compute the projections.

Default:
'simple'

List of values:
'rectangle', 'simple'

List of values (for compute devices):
'simple'

**`HorProjection`** (output_control)  real-array `→`  (real)

Horizontal projection.

**`VertProjection`** (output_control)  real-array `→`  (real)

Vertical projection.

## Module

1D Metrology
