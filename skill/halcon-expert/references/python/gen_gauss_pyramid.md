# gen_gauss_pyramid (Operator)

## Name

`gen_gauss_pyramid` — Calculating a Gauss pyramid.

## Signature

`def gen_gauss_pyramid(image: HObject, mode: str, scale: float) -> HObject`

## Description

The operator `gen_gauss_pyramid` calculates a pyramid of
scaled down images. The scale by which the next image will be
reduced is determined by the parameter *`scale`*. For instance,
a value of 0.5 for *`scale`* will shorten the edge length of
*`image`* by 50%. This is exactly equivalent to the “normal”
pyramid.

The parameter *`mode`* determines the way of averaging. For a
more detailed description concerning this parameter see also
[`affine_trans_image`](affine_trans_image.md). In the case that *`scale`* is
equal 0.5 there are the additional modes *"min"* and
*"max"* available. In this case the minimum or the maximum
of the four neighboring pixels is selected.

Please note that each level will be returned as an individual image,
i.e., as one iconic object, with one matrix and its own domain.
Single or multiple levels can be selected by using
[`select_obj`](select_obj.md) or [`copy_obj`](copy_obj.md), respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2 / real)

Input image.

**`image_pyramid`** (output_object)  (multichannel-)image-array `→` HObject (byte / uint2 / real)

Output images.

Number of elements:
ImagePyramid > Image

**`mode`** (input_control)  string `→` str

Kind of filter mask.

Default:
"weighted"

List of values:
"constant", "max", "min", "nearest_neighbor", "weighted"

**`scale`** (input_control)  real `→` float

Factor for scaling down.

Default:
0.5

Suggested values:
0.2, 0.3, 0.4, 0.5, 0.6

Value range:
`0.001
≤
scale
≤
0.9`

Recommended increment:
0.1

## Example (C)

```
gen_gauss_pyramid(Image,Pyramid,"weighted",0.5);
count_obj(Pyramid,&num);
for (i=1; i<=num; i++)
{
  select_obj(Pyramid,&Single,i);
  disp_image(Single,WindowHandle);
  clear(Single);
}
```

## Possible Successors

`image_to_channels`,
`count_obj`,
`select_obj`,
`copy_obj`

## Alternatives

`zoom_image_size`,
`zoom_image_factor`

## See also

`affine_trans_image`

## Module

Foundation
