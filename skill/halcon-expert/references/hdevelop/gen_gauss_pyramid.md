# gen_gauss_pyramid (Operator)

## Name

`gen_gauss_pyramid` — Calculating a Gauss pyramid.

## Signature

`gen_gauss_pyramid(Image : ImagePyramid : Mode, Scale : )`

## Description

The operator `gen_gauss_pyramid` calculates a pyramid of
scaled down images. The scale by which the next image will be
reduced is determined by the parameter *`Scale`*. For instance,
a value of 0.5 for *`Scale`* will shorten the edge length of
*`Image`* by 50%. This is exactly equivalent to the “normal”
pyramid.

The parameter *`Mode`* determines the way of averaging. For a
more detailed description concerning this parameter see also
[`affine_trans_image`](affine_trans_image.md). In the case that *`Scale`* is
equal 0.5 there are the additional modes *'min'* and
*'max'* available. In this case the minimum or the maximum
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

**`Image`** (input_object)  (multichannel-)image `→` object (byte / uint2 / real)

Input image.

**`ImagePyramid`** (output_object)  (multichannel-)image-array `→` object (byte / uint2 / real)

Output images.

Number of elements:
ImagePyramid > Image

**`Mode`** (input_control)  string `→`  (string)

Kind of filter mask.

Default:
'weighted'

List of values:
'constant', 'max', 'min', 'nearest_neighbor', 'weighted'

**`Scale`** (input_control)  real `→`  (real)

Factor for scaling down.

Default:
0.5

Suggested values:
0.2, 0.3, 0.4, 0.5, 0.6

Value range:
`0.001
≤
Scale
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
