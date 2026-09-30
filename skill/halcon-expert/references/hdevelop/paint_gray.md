# paint_gray (Operator)

## Name

`paint_gray` — Paint the gray values of an image into another image.

## Signature

`paint_gray(ImageSource, ImageDestination : MixedImage : : )`

## Description

`paint_gray` paints the gray values of the image given in
*`ImageSource`* into the image in *`ImageDestination`* and returns
the resulting image in *`MixedImage`*. Only the gray values of the
domain of *`ImageSource`* are copied (see [`reduce_domain`](reduce_domain.md)).

As an alternative to `paint_gray`, you can use the operator
[`overpaint_gray`](overpaint_gray.md), which directly paints the gray values into
*`ImageDestination`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageSource`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image containing the desired gray values.

**`ImageDestination`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image to be painted over.

**`MixedImage`** (output_object)  image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

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

`paint_gray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`gen_image_const`,
`gen_image_proto`

## Alternatives

`get_image_pointer1`,
`set_grayval`,
`copy_image`,
`overpaint_gray`

## See also

`paint_region`,
`overpaint_region`

## Module

Foundation
