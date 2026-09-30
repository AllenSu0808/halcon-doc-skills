# PaintRegion (Operator)

## Name

`PaintRegion` — Paint regions into an image.

## Signature

`static void HOperatorSet.PaintRegion(HObject region, HObject image, out HObject imageResult, HTuple grayval, HTuple type)`

`HImage HImage.PaintRegion(HRegion region, HTuple grayval, string type)`

`HImage HImage.PaintRegion(HRegion region, double grayval, string type)`

`HImage HRegion.PaintRegion(HImage image, HTuple grayval, string type)`

`HImage HRegion.PaintRegion(HImage image, double grayval, string type)`

## Description

`PaintRegion` paints the regions given in *`region`* with a
constant gray value into the image given in *`image`* and returns the
result in *`imageResult`*. These gray values can either be specified
for each channel once, valid for all regions, or for each region
separately. To define the latter, group the channel gray values g of each region and concatenate them to a tuple according to the regions'
order, e.g., for a three channel image:

[g(channel1,region1), g(channel2,region1), g(channel3,region1), g(channel1,region2), ... ].
If the input image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.
The parameter *`type`* determines whether the region should be painted
filled (*"fill"*) or whether only its boundary should be painted
(*"margin"*).

As an alternative to `PaintRegion`, you can use the operator
[`OverpaintRegion`](overpaint_region.md), which directly paints the regions into
*`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be painted into the input image.

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image in which the regions are to be painted.

**`imageResult`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image containing the result.

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
* Paint a rectangle into the image 'monkey'

read_image(Image,'monkey')
gen_rectangle1(Rectangle,100.0,100.0,300.0,300.0)
* paint a white rectangle
paint_region(Rectangle,Image,ImageResult,255.0,'fill')
```

## Result

`PaintRegion` returns 2 (
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
`OverpaintRegion`,
`PaintXld`

## See also

`ReduceDomain`,
`PaintGray`,
`OverpaintGray`,
`SetDraw`,
`GenImageConst`

## Module

Foundation
