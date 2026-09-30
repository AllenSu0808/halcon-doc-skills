# FindGenericShapeModel (Operator)

## Name

`FindGenericShapeModel` — Find the best matches of one or multiple shape models in an image.

## Signature

`static void HOperatorSet.FindGenericShapeModel(HObject searchImage, HTuple modelID, out HTuple matchResultID, out HTuple numMatchResult)`

`static HGenericShapeModelResult HShapeModel.FindGenericShapeModel(HObject searchImage, HShapeModel[] modelID, out int numMatchResult)`

`HGenericShapeModelResult HShapeModel.FindGenericShapeModel(HObject searchImage, out int numMatchResult)`

`int HGenericShapeModelResult.FindGenericShapeModel(HObject searchImage, HShapeModel[] modelID)`

`int HGenericShapeModelResult.FindGenericShapeModel(HObject searchImage, HShapeModel modelID)`

`HGenericShapeModelResult HImage.FindGenericShapeModel(HShapeModel[] modelID, out int numMatchResult)`

`HGenericShapeModelResult HImage.FindGenericShapeModel(HShapeModel modelID, out int numMatchResult)`

## Description

The operator `FindGenericShapeModel` finds the best instances of
one or multiple shape models passed in *`modelID`* in the input image
*`searchImage`*. The found matches are returned in
*`matchResultID`* and can be queried using
[`GetGenericShapeModelResult`](get_generic_shape_model_result.md) and
[`GetGenericShapeModelResultObject`](get_generic_shape_model_result_object.md). The number of found matches
is returned in *`numMatchResult`*. The model can be parameterized using
[`SetGenericShapeModelParam`](set_generic_shape_model_param.md) and
[`SetGenericShapeModelObject`](set_generic_shape_model_object.md), through which one can control
the search.

The input image *`searchImage`* may be a multichannel image.
Which channels of a multichannel image are used depends on the
model parameter *"metric"* (see
[`SetGenericShapeModelParam`](set_generic_shape_model_param.md)).
The domain of *`searchImage`* sets the ROI for the
search. It limits the search space as it is considered as boundary for the
center of gravity of *`modelID`* in order to accelerate the matching
process. For information on passing a tuple of images to
*`searchImage`* see below.
Furthermore, the search space is limited by the size of *`searchImage`*.
By default, *`modelID`* is only searched within those points of the
domain, in which *`modelID`* fits completely. Hence, *`modelID`*
will not be found if it exceeds the border of the image. This holds
for all levels of the used image pyramid.

In rare cases which typically occur for artificial images, instances of
*`modelID`* cannot be found in an image, if they touch the border of the
domain on any level of the image pyramid.
As a rule of thumb, *`modelID`* might not be found if its distance to
an image border is smaller than $2^{NumLevels-1}$
pixels (where $NumLevels$ is the number of pyramid levels).
This behavior can be changed with *"border_shape_models"*, see
[`SetGenericShapeModelParam`](set_generic_shape_model_param.md).
When searching multiple models *"border_shape_models"* is treated
as *"true"* for all models even if *"border_shape_models"*
only evaluates to *"true"* for one of the models in a search.

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/b7723e73fc5bf5ab.svg) | ![figure](../assets/3bd12107a54a2340.svg) | ![figure](../assets/6169370fb6223059.svg) |
| ( 1) | ( 2) | ( 3) |

(1) Search image with reduced domain (yellow) and the shape model (cyan).
(2) Instances that will be returned (green) or not returned (red)
in case *"border_shape_models"* is set to *"false"*.
(3) Instances that will be returned (green) or not returned (red)
in case *"border_shape_models"* is set to *"true"*.

### Applying multiple models

When searching multiple models, the search space can be restricted for all
models simultaneously by passing a single image with reduced domain in
*`searchImage`*.

Alternatively, the search space can be restricted for each model
individually by passing an object containing multiple image objects, one for
each model in *`modelID`*.
The search space is determined by the domain of the corresponding image.
Except the domain, the images have to be identical, i.e.,
the pointers of the image objects need to refer to the same
image (thus they need to be identical).
The pointers can be checked using [`GetImagePointer1`](get_image_pointer1.md).

For each model, different identifiers (*"model_identifier"*)
have to be set, so that each instance can be assigned to the shape model
it has been found with. Otherwise an exception is raised.

Different models should have been created with the same value of
*"min_contrast"*.
If different *"min_contrast"* values are set for the individual
models, `FindGenericShapeModel` will use the smallest of these
values on the highest pyramid level for all models.
During tracking (and therefore on all pyramid levels below), the individual
*"min_contrast"* value of each model is used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`searchImage`** (input_object)  (multichannel-)object(-array) `→` [HObject](HObject.md)

Image in which the model is searched.

**`modelID`** (input_control, state is modified)  shape_model(-array) `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the shape model.

**`matchResultID`** (output_control)  generic_shape_model_result `→` [HGenericShapeModelResult](HGenericShapeModelResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle with the found matches.

**`numMatchResult`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of found matches.

## Result

If the parameters are valid, the operator
`FindGenericShapeModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`TrainGenericShapeModel`,
`SetGenericShapeModelParam`

## Module

Matching
