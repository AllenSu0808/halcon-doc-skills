# GetTextureInspectionModelParam (Operator)

## Name

`GetTextureInspectionModelParam` — Query parameters of a texture inspection model.

## Signature

`static void HOperatorSet.GetTextureInspectionModelParam(HTuple textureInspectionModel, HTuple genParamName, out HTuple genParamValue)`

`HTuple HTextureInspectionModel.GetTextureInspectionModelParam(HTuple genParamName)`

`HTuple HTextureInspectionModel.GetTextureInspectionModelParam(string genParamName)`

## Description

The operator `GetTextureInspectionModelParam` is used to query the
values of the different parameters of a texture inspection model
(*`textureInspectionModel`*). The names of the desired parameters are
passed in the parameter *`genParamName`*, the corresponding values are
returned in *`genParamValue`*. It is possible to query multiple
parameters with a single call to
`GetTextureInspectionModelParam`. All parameters which can be
manipulated by [`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md) can be queried.
Please refer to the documentation of
[`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md) for an explanation of the
individual parameters. It is furthermore possible to query the following
parameters:

- ***"gmm_centers"*:** —

  Returns the number of Gaussian distributions
  which were determined as optimal within the training process. The value
  can be used as a reference for future texture inspection models.
  The range of the possible number of distributions is determined by the
  settings of the parameters *"gmm_pmincenters"* and
  *"gmm_pmaxcenters"*. Each image pyramid level can have a different
  number of Gaussian distributions. By adding an index, the number of
  Gaussian distributions for specific pyramid levels can be queried.
  For example, *"gmm_centers_3"* returns the number of Gaussian
  distributions for the third pyramid level.
- ***"image_indices"*:** —

  Returns the indices of the images that have been added to the texture
  inspection model using [`AddTextureInspectionModelImage`](add_texture_inspection_model_image.md).
  Only indices of images are returned that are currently in the texture
  inspection model and have not been deleted with
  [`RemoveTextureInspectionModelImage`](remove_texture_inspection_model_image.md).
- ***"trained_covartype"*:** —

  Returns the type of covariance matrix that was used during training.
  The user has the possibility to set the preferred type of covariance
  matrix by setting *"gmm_covartype"* with
  [`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md). However, if the training with
  the preferred covariance type fails, training is re-initialized with
  a less strict *"gmm_covartype"*. Hence, if training with
  *"diag"* fails, a further training with *"spherical"* is
  attempted.

In order to avoid confusions regarding the returned tuple length,
multivalued parameters, such as *"image_indices"*,
*"gmm_centers"*, *"levels"* and *"novelty_threshold"*
can only be queried alone i.e. without passing any other parameter to
`GetTextureInspectionModelParam`.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`textureInspectionModel`** (input_control)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection model.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the queried model parameter.

Default:
"novelty_threshold"

List of values:
"gen_result_handle", "gmm_centers", "gmm_covartype", "gmm_em_max_iter", "gmm_em_regularize", "gmm_em_threshold", "gmm_ncomp", "gmm_pmaxcenters", "gmm_pmincenters", "gmm_preprocessing", "gmm_randseed", "gmm_sigma", "image_indices", "levels", "novelty_threshold", "num_levels", "patch_normalization", "patch_rotational_robustness", "patch_size", "sensitivity", "trained_covartype"

**`genParamValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Value of the queried model parameter.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
* Make this short example fast:
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gmm_em_max_iter', 1)
* Get parameters
get_texture_inspection_model_param (TextureInspectionModel, 'patch_size', \
                                    PatchSize)
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

The operator `GetTextureInspectionModelParam` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateTextureInspectionModel`,
`TrainTextureInspectionModel`

## Possible Successors

`AddTextureInspectionModelImage`,
`TrainTextureInspectionModel`

## See also

`SetTextureInspectionModelParam`

## Module

Matching
