# GrayHisto (Operator)

## Name

`GrayHisto` — Calculate the gray value distribution.

## Signature

`static void HOperatorSet.GrayHisto(HObject region, HObject image, out HTuple absoluteHisto, out HTuple relativeHisto)`

`HTuple HImage.GrayHisto(HRegion region, out HTuple relativeHisto)`

`HTuple HRegion.GrayHisto(HImage image, out HTuple relativeHisto)`

## Description

The operator `GrayHisto` calculates for the image
(*`image`*) within *`region`* the absolute
(*`absoluteHisto`*) and relative (*`relativeHisto`*)
histogram of the gray values.

Both histograms are tuples of 256 values, which --- beginning at 0
--- contain the frequencies of the individual gray values of the
image.

*`absoluteHisto`* indicates the absolute frequencies of the
gray values in integers, and *`relativeHisto`* indicates the
relative, i.e. the absolute frequencies divided by the area of the
image as floating point numbers.

*"real"*-, *"int2"*-, *"uint2"*-, and *"int4"*-images
are transformed into *"byte"*-images (first the largest and smallest
gray value in the image are determined, and then the original gray values are
mapped linearly into the area 0..255) and then processed as
mentioned above.

## Attention

Note that the operator `GrayHisto` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

Real, int2, uint2, and int4 images are reduced to 256 gray values.

`GrayHisto` can be executed on OpenCL devices for byte, int1,
directional and cyclic images if the OpenCL device supports the
cl_khr_local_int32_base_atomics and cl_khr_global_int32_base_atomics
extensions (which are optional in OpenCL 1.0). Unlike most other HALCON
operators, `GrayHisto` can be substantially slower on an OpenCL
device if the *`image`* is not completely included in the
*`region`*.

OpenCL support is not available in HALCON XL, as 64 bit atomic integer
arithmetic would be required.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Region in which the histogram is to be calculated.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte* / cyclic* / direction* / int1* / int2 / uint2 / int4 / real) **allowed for compute devices*

Image the gray value distribution of which is
to be calculated.

**`absoluteHisto`** (output_control)  histogram-array `→` [HTuple](HTuple.md) (*int* / long)

Absolute frequencies of the gray values.

**`relativeHisto`** (output_control)  histogram-array `→` [HTuple](HTuple.md) (*double*)

Frequencies, normalized to the area of the region.

## Complexity

If F is the area of the region the runtime complexity is
O(F + 255).

## Result

The operator `GrayHisto` returns the value 2 (
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

`HistoToThresh`,
`GenRegionHisto`

## Alternatives

`MinMaxGray`,
`Intensity`,
`GrayHistoAbs`,
`GrayHistoRange`

## See also

`SetPaint`,
`Histo2dim`,
`ScaleImageMax`,
`EntropyGray`

## Module

Foundation
