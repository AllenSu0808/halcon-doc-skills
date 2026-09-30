# remove_texture_inspection_model_image (Operator)

## Name

`remove_texture_inspection_model_image` — Clear all or a user-defined subset of the images of a
texture inspection model.

## Signature

`def remove_texture_inspection_model_image(texture_inspection_model: MaybeSequence[HHandle], indices: Sequence[int]) -> Sequence[int]`

## Description

`remove_texture_inspection_model_image` clears all or certain selected
images that have been stored in a texture inspection model
*`texture_inspection_model`*.

On the one hand, the usage of `remove_texture_inspection_model_image`
is recommended to reduce the storage space of a saved texture inspection
model. This is especially of advantage if the texture inspection model has
been trained in an offline process and written with
[`write_texture_inspection_model`](write_texture_inspection_model.md). In this case, test images
can still be classified using [`apply_texture_inspection_model`](apply_texture_inspection_model.md),
while the required storage space is reduced to a minimum.
On the other hand, it offers a simple way to delete certain selected images
of the texture inspection model that are not needed (anymore) for a
subsequent classification process.
This allows the user to proceed with an entirely configured model, while
only the used image data has to be tuned to solve the underlying inspection
problem. Please note that after removing images from the model a retraining
is required.

In order to specifically delete images from the texture inspection model,
the indices of the respective images have to be specified in the
parameter *`indices`*. A validation of all images that are still in the
texture inspection model can be made using the value *"image_indices"*
in [`get_texture_inspection_model_param`](get_texture_inspection_model_param.md).
If the user still passes unassigned indices to delete images, these indices
are ignored.
Besides the above mentioned option,
`remove_texture_inspection_model_image` also allows to set the
parameter *`indices`* to the value *"all"*. In this case,
all images of the texture inspection model are deleted.

It should be noted that after deleting all images, the model can only be
(re)trained, if new images are added using
[`add_texture_inspection_model_image`](add_texture_inspection_model_image.md).
In the case that only a subset of all images has been deleted, a call of
[`train_texture_inspection_model`](train_texture_inspection_model.md) requires all steps of the training to
be executed, since potentially still available training data does not match
the used data.

After calling `remove_texture_inspection_model_image`, the remaining
indices of the images that are still in the texture inspection model are
returned in the parameter *`remaining_indices`*.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- texture_inspection_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`texture_inspection_model`** (input_control, state is modified)  texture_inspection_model(-array) `→` MaybeSequence[HHandle]

Handle of the texture inspection model.

**`indices`** (input_control)  integer-array `→` Sequence[int]

Indices of the images to be deleted from the
texture inspection model.

**`remaining_indices`** (output_control)  integer-array `→` Sequence[int]

Indices of the images that remain in the
texture inspection model.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
* Read and add training images
read_image (TrainImage, 'carpet/carpet_01')
add_texture_inspection_model_image (TrainImage, TextureInspectionModel, \
                                    Indices)
* Get added training images
get_texture_inspection_model_image (TrainImageOut, TextureInspectionModel)
* Remove training images
remove_texture_inspection_model_image (TextureInspectionModel, Indices, \
                                       RemainingIndices)
```

## Result

If the parameters are valid, the operator
`remove_texture_inspection_model_image` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`train_texture_inspection_model`

## See also

`create_texture_inspection_model`,
`clear_texture_inspection_model`,
`set_texture_inspection_model_param`,
`get_texture_inspection_model_param`,
`add_texture_inspection_model_image`

## Module

Matching
