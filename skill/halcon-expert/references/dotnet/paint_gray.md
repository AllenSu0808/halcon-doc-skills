# PaintGray (Operator)

## Name

`PaintGray` — Paint the gray values of an image into another image.

## Signature

`static void HOperatorSet.PaintGray(HObject imageSource, HObject imageDestination, out HObject mixedImage)`

`HImage HImage.PaintGray(HImage imageDestination)`

## Description

`PaintGray` paints the gray values of the image given in
*`imageSource`* into the image in *`imageDestination`* and returns
the resulting image in *`mixedImage`*. Only the gray values of the
domain of *`imageSource`* are copied (see [`ReduceDomain`](reduce_domain.md)).

As an alternative to `PaintGray`, you can use the operator
[`OverpaintGray`](overpaint_gray.md), which directly paints the gray values into
*`imageDestination`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageSource`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image containing the desired gray values.

**`imageDestination`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image to be painted over.

**`mixedImage`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Result image.

## Example (HDevelop)

```
* Copy a circular part of the image 'monkey' into the image 'fabrik':

read_image(Image,'monkey')
gen_circle(Circle,200,200,150)
reduce_domain(Image,Circle,Mask)
read_image(Image2,'fabrik')
* Copy a part of the image 'monkey' into 'fabrik'
paint_gray(Mask,Image2,MixedImage)
```

## Result

`PaintGray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadImage`,
`GenImageConst`,
`GenImageProto`

## Alternatives

`GetImagePointer1`,
`SetGrayval`,
`CopyImage`,
`OverpaintGray`

## See also

`PaintRegion`,
`OverpaintRegion`

## Module

Foundation
