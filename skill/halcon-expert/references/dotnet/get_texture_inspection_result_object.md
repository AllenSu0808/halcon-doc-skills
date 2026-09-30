# GetTextureInspectionResultObject (Operator)

## Name

`GetTextureInspectionResultObject` — Query iconic results of a texture inspection.

## Signature

`static void HOperatorSet.GetTextureInspectionResultObject(out HObject objectVal, HTuple textureInspectionResultID, HTuple resultName)`

`HObject HTextureInspectionResult.GetTextureInspectionResultObject(HTuple resultName)`

`HObject HTextureInspectionResult.GetTextureInspectionResultObject(string resultName)`

## Description

`GetTextureInspectionResultObject` queries the iconic result
*`resultName`* of the handle *`textureInspectionResultID`* returned
by [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md). The
result handle *`textureInspectionResultID`* was only created when
*"gen_result_handle"* was set to *"true"* with
[`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

In the following the possible parameter values for *`resultName`*
are listed:

- ***"novelty_region"*:** —

  Returns the novelty regions of all pyramid levels in an object tuple.
  To query the novelty regions of single pyramid levels the corresponding
  index has to be added, e.g., *"novelty_region_1"*. Please note that
  if a tuple of images was passed to [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md),
  it is only possible to query the novelty regions
  for the first image within the tuple.
- ***"novelty_score_image"*:** —

  Returns the novelty score images of all pyramid levels in an object tuple.
  To query the novelty regions of single pyramid levels the corresponding
  index has to be added, e.g., *"novelty_score_image_1"*. Please
  note that if a tuple of images was passed to
  [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md), it is only possible to query the
  novelty score images for the first image within the tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Returned iconic object.

**`textureInspectionResultID`** (input_control)  texture_inspection_result `→` [HTextureInspectionResult](HTextureInspectionResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection result.

**`resultName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Name of the iconic object to be returned.

Default:
"novelty_region"

List of values:
"novelty_region", "novelty_score_image"

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
* Get result objects
get_texture_inspection_result_object (Object, TextureInspectionResultID, \
                                      'novelty_score_image')
```

## Result

The operator `GetTextureInspectionResultObject` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`ApplyTextureInspectionModel`

## Possible Successors

`ClearTextureInspectionResult`,
`ClearTextureInspectionModel`

## Module

Matching
