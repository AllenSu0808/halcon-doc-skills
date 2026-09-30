# OverpaintRegion (Operator)

## Name

`OverpaintRegion` — Overpaint regions in an image.

## Signature

`static void HOperatorSet.OverpaintRegion(HObject image, HObject region, HTuple grayval, HTuple type)`

`void HImage.OverpaintRegion(HRegion region, HTuple grayval, string type)`

`void HImage.OverpaintRegion(HRegion region, double grayval, string type)`

`void HRegion.OverpaintRegion(HImage image, HTuple grayval, string type)`

`void HRegion.OverpaintRegion(HImage image, double grayval, string type)`

## Description

`OverpaintRegion` paints the regions given in
*`region`* with a constant gray value into the image given in
*`image`*. These gray values can either
be specified for each channel once, valid for all regions, or for each
region separately. To define the latter, group the channel gray values
g of each region and concatenate them to a tuple according to
the regions' order, e.g., for a three channel image:
[g(channel1,region1), g(channel2,region1), g(channel3,region1), g(channel1,region2), ... ].
If the input image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.
The parameter *`type`* determines whether
the region should be painted filled (*"fill"*) or whether
only its boundary should be painted (*"margin"*).

If you do not want to modify *`image`* itself, you can use the operator
[`PaintRegion`](paint_region.md), which returns the result in a newly created image.

## Attention

`OverpaintRegion` modifies the content of an already existing image
(*`image`*). Besides, even other image objects may be affected: For
example, if you created *`image`* via [`CopyObj`](copy_obj.md) from another
image object (or vice versa), `OverpaintRegion` will also modify the
image matrix of this other image object. Therefore, `OverpaintRegion`
should only be used to overpaint newly created image objects. Typical
operators for this task are, e.g., [`GenImageConst`](gen_image_const.md) (creates a new
image with a specified size), [`GenImageProto`](gen_image_proto.md) (creates an image with
the size of a specified prototype image) or [`CopyImage`](copy_image.md) (creates an
image as the copy of a specified image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- image

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object, state is modified)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image in which the regions are to be painted.

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be painted into the input image.

**`grayval`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Desired gray values of the regions.

Default:
255.0

Suggested values:
0.0, 1.0, 2.0, 5.0, 10.0, 16.0, 32.0, 64.0, 128.0, 253.0, 254.0, 255.0

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Paint regions filled or as boundaries.

Default:
"fill"

List of values:
"fill", "margin"

## Example (HDevelop)

```
* Paint a rectangle into a new image (New1)

gen_rectangle1(Rectangle,100.0,100.0,300.0,300.0)
* generate a black image
gen_image_const(New1,'byte', 768, 576)
* paint a white rectangle
overpaint_region(New1,Rectangle,255.0,'fill')
```

## Result

`OverpaintRegion` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`ReadImage`,
`GenImageConst`,
`GenImageProto`,
`ReduceDomain`

## Alternatives

`SetGrayval`,
`PaintRegion`,
`PaintXld`

## See also

`ReduceDomain`,
`SetDraw`,
`PaintGray`,
`OverpaintGray`,
`GenImageConst`

## Module

Foundation
