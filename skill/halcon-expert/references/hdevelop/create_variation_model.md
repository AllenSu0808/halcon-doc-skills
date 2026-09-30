# create_variation_model (Operator)

## Name

`create_variation_model` — Create a variation model for image comparison.

## Signature

`create_variation_model( : : Width, Height, Type, Mode : ModelID)`

## Description

`create_variation_model` creates a variation model that can be
used for image comparison. The handle for the variation model is
returned in *`ModelID`*.

Typically, the variation model is used to discriminate correctly
manufactured objects (“good objects”) from incorrectly
manufactured objects (“bad objects”). It is assumed that the
discrimination can be done solely based on the gray values of the
object.

The variation model consists of an ideal image of the object to
which the images of the objects to be tested are compared later on
with [`compare_variation_model`](compare_variation_model.md) or
[`compare_ext_variation_model`](compare_ext_variation_model.md), and an image that represents
the amount of gray value variation at every point of the object.
The size of the images with which the object model is trained and
with which the model is compared later on is passed in
*`Width`* and *`Height`*, respectively. The image type of
the images used for training and comparison is passed in
*`Type`*.

The variation model is trained using multiple images of good
objects. Therefore, it is essential that the training images show
the objects in the same position and rotation. If this cannot be
guaranteed by external means, the pose of the object can, for
example, be determined by using matching (see
[`find_generic_shape_model`](find_generic_shape_model.md)). The image can then be transformed to a
reference pose with [`affine_trans_image`](affine_trans_image.md).

The parameter *`Mode`* is used to determine how the image of
the ideal object and the corresponding variation image are computed.
For *`Mode`*=*'standard'*, the ideal image of the object
is computed as the mean of all training images at the respective
image positions. The corresponding variation image is computed as
the standard deviation of the training images at the respective
image positions. This mode has the advantage that the variation
model can be trained iteratively, i.e., as soon as an image of a
good object becomes available, it can be trained with
[`train_variation_model`](train_variation_model.md). The disadvantage of this mode is
that great care must be taken to ensure that only images of good
objects are trained, because the mean and standard deviation are not
robust against outliers, i.e., if an image of a bad object is
trained inadvertently, the accuracy of the ideal object image and
that of the variation image might be degraded.

If it cannot be avoided that the variation model is trained with
some images of objects that can contain errors, *`Mode`* can be
set to *'robust'*. In this mode, the image of the ideal
object is computed as the median of all training images at the
respective image positions. The corresponding variation image is
computed as a suitably scaled median absolute deviation of the
training images and the median image at the respective image
positions. This mode has the advantage that it is robust against
outliers. It has the disadvantage that it cannot be trained
iteratively, i.e., all training images must be accumulated using
[`concat_obj`](concat_obj.md) and be trained with [`train_variation_model`](train_variation_model.md)
in a single call.

In some cases, it is impossible to acquire multiple training images.
In this case, a useful variation image cannot be trained from the
single training image. To solve this problem, variations of the
training image can be created synthetically, e.g., by shifting the
training image by $\pm1$ pixel in the row and column
directions or by using gray value morphology (e.g.,
[`gray_erosion_shape`](gray_erosion_shape.md) and [`gray_dilation_shape`](gray_dilation_shape.md)), and
then training the synthetically modified images. A different
possibility to create the variation model from a single image is to
create the model with *`Mode`*=*'direct'*. In this
case, the variation model can only be trained by specifying the
ideal image and the variation image directly with
[`prepare_direct_variation_model`](prepare_direct_variation_model.md). Since the variation
typically is large at the edges of the object, edge operators like
[`sobel_amp`](sobel_amp.md), [`edges_image`](edges_image.md), or [`gray_range_rect`](gray_range_rect.md)
should be used to create the variation image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the images to be compared.

Default:
640

Suggested values:
160, 192, 320, 384, 640, 768

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the images to be compared.

Default:
480

Suggested values:
120, 144, 240, 288, 480, 576

**`Type`** (input_control)  string `→`  (string)

Type of the images to be compared.

Default:
'byte'

Suggested values:
'byte', 'int2', 'uint2'

**`Mode`** (input_control)  string `→`  (string)

Method used for computing the variation model.

Default:
'standard'

Suggested values:
'standard', 'robust', 'direct'

**`ModelID`** (output_control)  variation_model `→`  (handle)

ID of the variation model.

## Complexity

A variation model created with `create_variation_model`
requires 12**`Width`***`Height`* bytes of memory for
*`Mode`* = *'standard'* and *`Mode`* =
*'robust'* for *`Type`* = *'byte'*. For
*`Type`* = *'uint2'* and *`Type`* =
*'int2'*, 14**`Width`***`Height`* are required.
For *`Mode`* = *'direct'* and after the training data
has been cleared with [`clear_train_data_variation_model`](clear_train_data_variation_model.md),
2**`Width`***`Height`* bytes are required for
*`Type`* = *'byte'* and
4**`Width`***`Height`* for the other image types.

## Result

`create_variation_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Successors

`train_variation_model`,
`prepare_direct_variation_model`

## See also

`prepare_variation_model`,
`clear_variation_model`,
`clear_train_data_variation_model`,
`find_generic_shape_model`,
`affine_trans_image`

## Module

Matching
