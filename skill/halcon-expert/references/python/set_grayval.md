# set_grayval (Operator)

## Name

`set_grayval` — Set single gray values in an image.

## Signature

`def set_grayval(image: HObject, row: MaybeSequence[int], column: MaybeSequence[int], grayval: MaybeSequence[Union[int, float]]) -> None`

## Description

`set_grayval` sets the gray values of the input image
*`image`* at the positions (*`row`*,*`column`*) to
the values specified by *`grayval`*. If *`image`* is a
multi-channel image, you can either set a single gray value for a
pixel and thus set it for all available channels, or you can set the
gray values g for all channels individually by
concatenating them within *`grayval`*. For example, for a
three-channel image three gray values (according to the order of the
channels) are specified for each pixel:
[g(channel0,pixel0), g(channel1,pixel0), g(channel2,pixel0), g(channel0,pixel1), ... ].
Please note that for complex or vector field images, two gray values
per pixel must be specified (per channel).

If the image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.

## Attention

The operator `set_grayval` produces quite some overhead.
Typically, it is used to set single gray values of an image. It is
not suitable for programming image processing operations such as
filters. In this case it is more useful to use the operator
[`get_image_pointer1`](get_image_pointer1.md) and to directly use the C or C++
interface for integrating own procedures.

Note also that `set_grayval` modifies the content of an
already existing image (*`image`*). Besides, even other image
objects may be affected: For example, if you created *`image`*
via [`copy_obj`](copy_obj.md) from another image object, `set_grayval`
will also modify the image matrix of this other image
object. Therefore, `set_grayval` should only be used to
overpaint newly created image objects.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- image

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object, state is modified)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be modified.

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[int]

Row coordinates of the pixels to be modified.

Default:
0

Suggested values:
0, 10, 50, 127, 255, 511

Value range:
`0
≤
row`

Restriction:
`0 <= Row && Row < height(Image)`

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[int]

Column coordinates of the pixels to be modified.

Default:
0

Suggested values:
0, 10, 50, 127, 255, 511

Value range:
`0
≤
column`

Restriction:
`0 <= Column && Column < width(Image)`

**`grayval`** (input_control)  grayval(-array) `→` MaybeSequence[Union[int, float]]

Gray values to be used.

Default:
255.0

Suggested values:
0.0, 1.0, 10.0, 128.0, 255.0

## Result

`set_grayval` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`read_image`,
`get_image_pointer1`,
`gen_image_proto`,
`gen_image1`

## Alternatives

`get_image_pointer1`,
`paint_gray`,
`paint_region`

## See also

`get_grayval`,
`gen_image_const`,
`gen_image1`,
`gen_image_proto`

## Module

Foundation
