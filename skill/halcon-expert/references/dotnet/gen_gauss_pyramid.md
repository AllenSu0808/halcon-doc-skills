# GenGaussPyramid (Operator)

## Name

`GenGaussPyramid` — Calculating a Gauss pyramid.

## Signature

`static void HOperatorSet.GenGaussPyramid(HObject image, out HObject imagePyramid, HTuple mode, HTuple scale)`

`HImage HImage.GenGaussPyramid(string mode, double scale)`

## Description

The operator `GenGaussPyramid` calculates a pyramid of
scaled down images. The scale by which the next image will be
reduced is determined by the parameter *`scale`*. For instance,
a value of 0.5 for *`scale`* will shorten the edge length of
*`image`* by 50%. This is exactly equivalent to the “normal”
pyramid.

The parameter *`mode`* determines the way of averaging. For a
more detailed description concerning this parameter see also
[`AffineTransImage`](affine_trans_image.md). In the case that *`scale`* is
equal 0.5 there are the additional modes *"min"* and
*"max"* available. In this case the minimum or the maximum
of the four neighboring pixels is selected.

Please note that each level will be returned as an individual image,
i.e., as one iconic object, with one matrix and its own domain.
Single or multiple levels can be selected by using
[`SelectObj`](select_obj.md) or [`CopyObj`](copy_obj.md), respectively.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`imagePyramid`** (output_object)  (multichannel-)image-array `→` [HImage](HImage.md) (byte / uint2 / real)

Output images.

Number of elements:
ImagePyramid > Image

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Kind of filter mask.

Default:
"weighted"

List of values:
"constant", "max", "min", "nearest_neighbor", "weighted"

**`scale`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

`ImageToChannels`,
`CountObj`,
`SelectObj`,
`CopyObj`

## Alternatives

`ZoomImageSize`,
`ZoomImageFactor`

## See also

`AffineTransImage`

## Module

Foundation
