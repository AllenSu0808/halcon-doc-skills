# midrange_image (Operator)

## Name

`midrange_image` — Calculate the average of maximum and minimum inside any mask.

## Signature

`midrange_image(Image, Mask : ImageMidrange : Margin : )`

## Description

The operator `midrange_image` forms the average of maximum and
minimum inside the indicated mask in the whole image. Several
border treatments (*`Margin`*) can be chosen for filtering:

- **gray value** —

  Pixels outside of the image border are assumed to be
  constant (with the indicated gray value).
- ***'continued'*** —

  Continuation of the gray values at the image
  border.
- ***'cyclic'*** —

  Cyclic continuation at the image borders.
- ***'mirrored'*** —

  Reflection of pixels at the image borders.

The indicated mask (= region of the mask image) is put over the
image to be filtered in such a way that the center of the mask
touches all pixels once.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`Mask`** (input_object)  region `→` object

Filter mask.

**`ImageMidrange`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / real)

Filtered image.

**`Margin`** (input_control)  string `→`  (string / integer / real)

Border treatment.

Default:
'mirrored'

Suggested values:
'mirrored', 'cyclic', 'continued', 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Example (HDevelop)

```
read_image(Image,'fabrik')
draw_region(Region,WindowHandle)
midrange_image(Image,Region,Midrange,'mirrored')
dev_display(Midrange)
```

## Complexity

For each pixel: O(sqrt(F) * 5) with F = area of *`Mask`*.

## Result

If the parameter values are correct the operator
`midrange_image` returns the value 2 (
H_MSG_TRUE)
. The behavior in case
of empty input (no input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
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

`sigma_image`

## See also

`gen_circle`,
`gen_rectangle1`,
`gray_erosion_rect`,
`gray_dilation_rect`,
`gray_range_rect`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 319

## Module

Foundation
