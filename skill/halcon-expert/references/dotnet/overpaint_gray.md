# OverpaintGray (Operator)

## Name

`OverpaintGray` — Overpaint the gray values of an image.

## Signature

`static void HOperatorSet.OverpaintGray(HObject imageDestination, HObject imageSource)`

`void HImage.OverpaintGray(HImage imageSource)`

## Description

`OverpaintGray` copies the gray values of the image given
in *`imageSource`* into the image in
*`imageDestination`*. Only the gray values of the domain of
*`imageSource`* are copied (see [`ReduceDomain`](reduce_domain.md)).

If you do not want to modify *`imageDestination`* itself, you can use
the operator [`PaintGray`](paint_gray.md), which returns the result in a newly created
image.

## Attention

`OverpaintGray` modifies the content of an already existing image
(*`imageDestination`*). Besides, even other image objects may be
affected: For example, if you created *`imageDestination`* via
[`CopyObj`](copy_obj.md) from another image object (or vice versa),
`OverpaintGray` will also modify the image matrix of this other image
object. Therefore, `OverpaintGray` should only be used to overpaint
newly created image objects. Typical operators for this task are, e.g.,
[`GenImageConst`](gen_image_const.md) (creates a new image with a specified size),
[`GenImageProto`](gen_image_proto.md) (creates an image with the size of a specified
prototype image) or [`CopyImage`](copy_image.md) (creates an image as the copy of
a specified image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- imageDestination

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`imageDestination`** (input_object, state is modified)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image to be painted over.

**`imageSource`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image containing the desired gray values.

## Example (HDevelop)

```
* Copy a circular part of the image 'monkey' into a new image (New1):

read_image(Image,'monkey')
gen_circle(Circle,200,200,150)
reduce_domain(Image,Circle,Mask)
* New image with black (0) background
gen_image_proto(Image,New1,0.0)
* Copy a part of the image 'monkey' into New1
overpaint_gray(New1,Mask)
```

## Result

`OverpaintGray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadImage`,
`GenImageConst`,
`GenImageProto`

## Alternatives

`GetImagePointer1`,
`PaintGray`,
`SetGrayval`,
`CopyImage`

## See also

`PaintRegion`,
`OverpaintRegion`

## Module

Foundation
