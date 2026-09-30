# gray_histo (Operator)

## Name

`gray_histo` — Calculate the gray value distribution.

## Signature

`gray_histo(Region, Image : : : AbsoluteHisto, RelativeHisto)`

## Description

The operator `gray_histo` calculates for the image
(*`Image`*) within *`Region`* the absolute
(*`AbsoluteHisto`*) and relative (*`RelativeHisto`*)
histogram of the gray values.

Both histograms are tuples of 256 values, which --- beginning at 0
--- contain the frequencies of the individual gray values of the
image.

*`AbsoluteHisto`* indicates the absolute frequencies of the
gray values in integers, and *`RelativeHisto`* indicates the
relative, i.e. the absolute frequencies divided by the area of the
image as floating point numbers.

*'real'*-, *'int2'*-, *'uint2'*-, and *'int4'*-images
are transformed into *'byte'*-images (first the largest and smallest
gray value in the image are determined, and then the original gray values are
mapped linearly into the area 0..255) and then processed as
mentioned above.

## Attention

Note that the operator `gray_histo` only considers
the given *`Region`* and ignores any previously set domain
of the input image *`Image`*.

Real, int2, uint2, and int4 images are reduced to 256 gray values.

`gray_histo` can be executed on OpenCL devices for byte, int1,
directional and cyclic images if the OpenCL device supports the
cl_khr_local_int32_base_atomics and cl_khr_global_int32_base_atomics
extensions (which are optional in OpenCL 1.0). Unlike most other HALCON
operators, `gray_histo` can be substantially slower on an OpenCL
device if the *`Image`* is not completely included in the
*`Region`*.

OpenCL support is not available in HALCON XL, as 64 bit atomic integer
arithmetic would be required.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Region`** (input_object)  region `→` object

Region in which the histogram is to be calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte* / cyclic* / direction* / int1* / int2 / uint2 / int4 / real) **allowed for compute devices*

Image the gray value distribution of which is
to be calculated.

**`AbsoluteHisto`** (output_control)  histogram-array `→`  (integer)

Absolute frequencies of the gray values.

**`RelativeHisto`** (output_control)  histogram-array `→`  (real)

Frequencies, normalized to the area of the region.

## Complexity

If F is the area of the region the runtime complexity is
O(F + 255).

## Result

The operator `gray_histo` returns the value 2 (
H_MSG_TRUE)
if the image
has defined gray values and the parameters are correct. The
behavior in case of empty input (no input images available) is set
via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`histo_to_thresh`,
`gen_region_histo`

## Alternatives

`min_max_gray`,
`intensity`,
`gray_histo_abs`,
`gray_histo_range`

## See also

`set_paint`,
`histo_2dim`,
`scale_image_max`,
`entropy_gray`

## Module

Foundation
