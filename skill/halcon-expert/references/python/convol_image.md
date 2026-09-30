# convol_image (Operator)

## Name

`convol_image` — Calculate the correlation between an image and an arbitrary filter mask

## Signature

`def convol_image(image: HObject, filter_mask: MaybeSequence[Union[int, float, str]], margin: Union[int, float, str]) -> HObject`

## Description

`convol_image` calculates the correlation between the input
image *`image`* and an arbitrary linear filter mask. The used
filter mask, which is given in *`filter_mask`*, can be either
loaded from a file or passed as a tuple. Several options for the
treatment at the image's borders can be chosen (*`margin`*):

- **gray value** —

  Pixels outside of the image border are assumed to be
  constant (with the indicated gray value).
- ***"continued"*** —

  Continuation of the gray values at the image
  border.
- ***"cyclic"*** —

  Cyclic continuation at the image borders.
- ***"mirrored"*** —

  Reflection of pixels at the image borders.

At all image positions, the correlation between the image and the
filter mask is calculated. If an overflow
or underflow occurs, the resulting gray value is clipped. Hence, if
filters that result in negative output values are used (e.g.,
derivative filters), the input image should be of type int2 or real.

The reference pixel of the mask, i.e., the pixel that lies at the
current image position for which the correlation is calculated,
is determined as follows: First, the region of all
mask pixels with a weight other than 0 is computed. Then, the center of this
region is computed and rounded. This is the reference point of the mask.

If a file name is given in *`filter_mask`*, the filter mask is read from
a text file with the following structure:
<Mask size>
<Inverse weight of the mask>
<Matrix>
The first line contains the size of the filter mask, given as two
numbers separated by white space (e.g., 3 3 for 3 x 3).
Here, the first number defines the height (rows) of the filter mask, while
the second number defines its width (columns). The next line contains the
inverse weight of the mask, i.e., the number by which the
correlation at a particular image position is divided. The remaining
lines contain the filter mask as integer or floating point numbers
(separated by white space), one line of the mask per line in the file.
The default HALCON file extension for the filter mask is 'fil'.
It is not necessary to pass this extension to the operator.
If the filter mask is to be computed from a tuple, the
tuple given in *`filter_mask`* must also satisfy the structure
described above. However, in this case the line feed is omitted.

For example, lets assume we want to use the following filter mask:
$$\frac{1}{16}\begin{bmatrix}1 & 2 & 1\\2 & 4 & 2\\1 & 2 & 1\end{bmatrix}$$ ![figure](../assets/1a129378c6079fb5.svg)

If the filter mask should be generated from a file, then the file
should look like this:

3 3
16
1 2 1
2 4 2
1 2 1

In contrast, if the filter mask should be generated from a tuple,
then the following tuple must be passed in *`filter_mask`*:

[3,3,16,1,2,1,2,4,2,1,2,1]

For convenience, it is possible to pass two vectors instead of a matrix
in *`filter_mask`*:

[MaskHeight,MaskWidth,Weight,V1,V2]

The outer product of those two vectors forms the filter matrix:

$$Mask:=V1\ast V1^{T}$$

E.g., the matrix above can also be passed as:

[3,3,16,1,2,1,1,2,1]

If *`filter_mask`* is separable (which is detected automatically),
`convol_image` uses a special implementation that is significantly
faster than the filtering with non separable masks.

If *"sse2_enable"* is set to *"true"* (and the SIMD
instruction set is available), the internal calculations for `byte` and
`real` images are performed using SIMD technology.
If *"sse41_enable"* is set to *"true"* (and the SIMD
instruction set is available), the internal calculations for `int2` and
`uint2` images are performed using SIMD technology.
If *"avx_enable"* is set to *"true"* (and the SIMD
instruction set is available), the internal calculations for `real`
images are performed using AVX SIMD technology for separable filter
with *"mirrored"* mask and non-separable filters.

## Attention

Note that `convol_image` does not compute a convolution of the
image with the given filter mask but a correlation, i.e., it uses the
given filter mask directly, not a mirrored version of the filter mask.

When using a 3x3 or 5x5 rectangular filter mask and the border treatment
*"mirrored"*, `convol_image` can be executed on OpenCL devices.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Images for which the correlation will be calculated.

**`image_result`** (output_object)  multichannel-image(-array) `→` HObject (byte / int2 / uint2 / real)

Result of the correlation.

**`filter_mask`** (input_control)  filename.read(-array) `→` MaybeSequence[Union[int, float, str]]

Filter mask as file name or tuple.

Default:
"sobel"

Suggested values:
"sobel", "laplace4", "lowpas_3_3"

File extension:
.`fil`

**`margin`** (input_control)  string `→` Union[int, float, str]

Border treatment.

Default:
"mirrored"

List of values (for compute devices):
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Module

Foundation
