# trimmed_mean (Operator)

## Name

`trimmed_mean` — Smooth an image with an arbitrary rank mask.

## Signature

`def trimmed_mean(image: HObject, mask: HObject, number: int, margin: Union[int, float, str]) -> HObject`

## Description

The operator `trimmed_mean` carries out a non-linear
smoothing of the gray values of all input images
(*`image`*). The filter mask (*`mask`*) is passed
in the form of a region. The average of *`number`* gray
values located near the median is calculated. Several border
treatments can be chosen for filtering (*`margin`*):

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

The indicated mask (= region of the mask image) is put over the
image to be filtered in such a way that the center of the mask
touches all pixels once. For each of these pixels all neighboring
pixels covered by the mask are sorted in an ascending sequence
according to their gray values. Thus, each of these sorted gray
value sequences contains exactly as many gray values as the mask has
pixels. If F is the area of the mask the average of these
sequences is calculated as follows: The first (F - Number)/2 gray
values are ignored. Then the following *`number`* gray
values are summed up and divided by *`number`*. Again the
remaining (F - *`number`*)/2 gray values are ignored.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`mask`** (input_object)  region `→` HObject

Image whose region serves as filter mask.

**`image_tmean`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Filtered output image.

**`number`** (input_control)  integer `→` int

Number of averaged pixels.
Typical value: Surface(Mask) / 2.

Default:
5

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31

Value range:
`1
≤
number
≤
401`

Minimum increment:
1

Recommended increment:
2

**`margin`** (input_control)  string `→` Union[int, float, str]

Border treatment.

Default:
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Result

If the parameter values are correct the operator
`trimmed_mean` returns the value 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no input images available) is set via the
operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`,
`draw_region`,
`gen_circle`,
`gen_rectangle1`

## Possible Successors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`sigma_image`,
`median_weighted`,
`median_image`

## See also

`gen_circle`,
`gen_rectangle1`,
`gray_erosion_rect`,
`gray_dilation_rect`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 320

## Module

Foundation
