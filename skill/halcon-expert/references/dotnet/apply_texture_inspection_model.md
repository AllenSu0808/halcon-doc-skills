# ApplyTextureInspectionModel (Operator)

## Name

`ApplyTextureInspectionModel` — Inspection of the texture within an image.

## Signature

`static void HOperatorSet.ApplyTextureInspectionModel(HObject image, out HObject noveltyRegion, HTuple textureInspectionModel, out HTuple textureInspectionResultID)`

`HRegion HImage.ApplyTextureInspectionModel(HTextureInspectionModel textureInspectionModel, out HTextureInspectionResult textureInspectionResultID)`

`HRegion HTextureInspectionModel.ApplyTextureInspectionModel(HImage image, out HTextureInspectionResult textureInspectionResultID)`

`public HTextureInspectionResult(HImage image, out HRegion noveltyRegion, HTextureInspectionModel textureInspectionModel)`

`HRegion HTextureInspectionResult.ApplyTextureInspectionModel(HImage image, HTextureInspectionModel textureInspectionModel)`

## Description

The operator `ApplyTextureInspectionModel` compares
*`image`* with the trained texture inspection model
*`textureInspectionModel`*. *`image`* can either be a single
image or a tuple of images. It is possible to pass either gray-scale
or multichannel images. Hereby, the operator expects that the passed
*`image`* has the same number of channels than the model was trained
with. The runtime of the `ApplyTextureInspectionModel` scales
roughly linearly with the number of image channels. However, models
using colored images are generally better at detecting colored
texture defects.

Pixels that do not fit to the texture inspection model are returned
in *`noveltyRegion`*. Furthermore, if *"gen_result_handle"* has
been set to *"true"* with [`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md),
the operator also returns the result handle
*`textureInspectionResultID`* with more detailed information on
the texture classification. If *"gen_result_handle"* is
set to *"false"*, *`textureInspectionResultID`* is empty.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

For each pyramid level texture features are extracted and classified
with the corresponding GMM classifier. The resulting novelty score is
then compared to
the novelty threshold of the current pyramid level and classified as
defective or not. The defective pixels are collected in a novelty region for
each pyramid level. These novelty regions are then combined to the
final novelty region returned in *`noveltyRegion`*. The novelty
regions of adjacent levels in the image pyramid are intersected with each
other. This step helps to improve the robustness towards noise within the
single pyramid level responses. The intersected novelty regions are then
added to the returned *"novelty_region"*. If a pyramid level has no
adjacent pyramid level the region itself is added to the
*"novelty_region"*. If, for example, *"num_levels"* is set to 1,
no adjacent pyramid level exists and the *"novelty_region"* is the
novelty region of the first pyramid level.

If *"gen_result_handle"* is set to *"true"*, the result handle
*`textureInspectionResultID`* contains
novelty score images and the resulting novelty regions for each pyramid level.

This information is useful for debugging and fine tuning of the model
parameters (e.g., the novelty thresholds) and can be accessed with
[`GetTextureInspectionResultObject`](get_texture_inspection_result_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator modifies the state of the following input parameter:

- textureInspectionResultID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image-array `→` [HImage](HImage.md) (byte / uint2 / real)

Image of the texture to be inspected.

**`noveltyRegion`** (output_object)  region-array `→` [HRegion](HRegion.md)

Novelty regions.

**`textureInspectionModel`** (input_control)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection model.

**`textureInspectionResultID`** (output_control, state is modified)  texture_inspection_result `→` [HTextureInspectionResult](HTextureInspectionResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the inspection results.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
* Set parameters
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gen_result_handle', 'true')
* Make this short example fast:
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gmm_em_max_iter', 1)
* Read and add training images
read_image (TrainImage, 'carpet/carpet_01')
add_texture_inspection_model_image (TrainImage, TextureInspectionModel, \
                                    Indices)
* Train the model
train_texture_inspection_model (TextureInspectionModel)
* Read and apply a test image
read_image (TestImage, 'carpet/carpet_02')
apply_texture_inspection_model (TestImage, DefectCandidates, \
                                TextureInspectionModel, \
                                TextureInspectionResultID)
```

## Result

The operator `ApplyTextureInspectionModel` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`TrainTextureInspectionModel`

## Possible Successors

`GetTextureInspectionResultObject`,
`GetTextureInspectionModelParam`,
`ClearTextureInspectionResult`,
`ClearTextureInspectionModel`

## Module

Matching
