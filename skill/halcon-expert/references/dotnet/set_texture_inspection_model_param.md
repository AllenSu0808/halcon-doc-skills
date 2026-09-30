# SetTextureInspectionModelParam (Operator)

## Name

`SetTextureInspectionModelParam` — Set parameters of a texture inspection model.

## Signature

`static void HOperatorSet.SetTextureInspectionModelParam(HTuple textureInspectionModel, HTuple genParamName, HTuple genParamValue)`

`void HTextureInspectionModel.SetTextureInspectionModelParam(HTuple genParamName, HTuple genParamValue)`

`void HTextureInspectionModel.SetTextureInspectionModelParam(string genParamName, int genParamValue)`

## Description

The operator `SetTextureInspectionModelParam` is used to
manipulate the parameters of a texture inspection model
*`textureInspectionModel`*. The current parameter settings
can be queried with the operator [`GetTextureInspectionModelParam`](get_texture_inspection_model_param.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

### General parameters:

- ***"num_levels"*:** —

  Determines the number of pyramid levels
  generated for the texture inspection process. The number
  of pyramid levels affects the inspection results as well as the runtime of
  [`TrainTextureInspectionModel`](train_texture_inspection_model.md) and
  [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md). Per default the number of
  levels is estimated by the size of the training images. It should be noted,
  that no more than 5 pyramid levels are used by the estimation process.

  Changing this parameter can require a complete new training of the texture
  inspection model. No retraining is required if the number of levels of a
  trained texture inspection model are merely reduced.

  If the texture in your images is very coarse, the lower pyramid levels
  may not be needed for a successful inspection. Then you can save
  a lot of runtime by setting the levels of interest explicitly with
  *"levels"*.

  Value range:
   integer values larger or equal to *1* or *"auto"*

  Default:
   *"auto"*
- ***"levels"*:** —

  Determines the specific pyramid levels
  used within the texture inspection process. The number
  of pyramid levels affects the inspection results as well as the runtime of
  [`TrainTextureInspectionModel`](train_texture_inspection_model.md) and
  [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md). Per default the pyramid levels
  are determined by the value of *"num_levels"*. If for example
  *"num_levels"* is set to four, then the texture inspection is
  performed for levels 1 to 4.
  If all available levels should be trained, the value has to be set to
  *"auto"*.

  Changing this parameter can require a complete new training of the texture
  inspection model. No retraining is required if the number of levels of a
  trained texture inspection model are merely reduced.

  If the texture in your images is very coarse, the lower pyramid levels
  may not be needed for a successful inspection. Then you can save
  a lot of runtime by excluding unwanted levels by setting the pyramid
  levels with *"levels"* explicitly.

  In order to avoid confusions regarding the returned tuple length,
  *"levels"* can only be set alone i.e. without passing any other
  parameter to `SetTextureInspectionModelParam`.

  Value range:
   a monotonically increasing tuple of integer values larger
  or equal to *1*, or *"auto"*

  Default:
   *"auto"*
- ***"gen_result_handle"*:** —

  This parameter determines whether or
  not a result handle is returned by [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md).
  If set to *"true"*, the individual pyramid level results can be
  queried from the texture result handle with
  [`GetTextureInspectionResultObject`](get_texture_inspection_result_object.md).
  This is useful for debugging and fine tuning.

  If set to *"false"*,
  [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md) only returns a novelty region.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*

### Parameters which influence the automatic novelty threshold calculation:

- ***"novelty_threshold"*:** —

  This parameter sets the values of the novelty thresholds, which
  distinguish between defective and non-defective texture. The
  novelty thresholds are passed as a tuple and are set for all
  pyramid levels at once. Therefore, the number of elements must be equal
  to the number of used pyramid levels *"num_levels"* (or
  *"levels"*, if specified).

  Setting the novelty thresholds prior to training
  has no effect since the training automatically determines novelty
  thresholds. Hence the novelty thresholds should be adapted after the
  training. A typical use case is the fine tuning to optimize the results of
  [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md). Please note, if the novelty
  thresholds have been set explicitly, a new call of
  [`TrainTextureInspectionModel`](train_texture_inspection_model.md) will re-estimate the
  novelty thresholds automatically and overwrite any explicitly set novelty
  thresholds.

  It is possible to add an index to set the novelty threshold of a
  specific pyramid level. For example, *"novelty_threshold_3"* sets the
  novelty threshold for the third pyramid level.

  Value range:
   integer or float values larger or equal to *0* and smaller
  or equal to *710*

  Default:
   Is determined by [`TrainTextureInspectionModel`](train_texture_inspection_model.md)
- ***"sensitivity"*:** —

  This parameter influences the sensitivity
  of the novelty thresholds which are determined during the training with
  [`TrainTextureInspectionModel`](train_texture_inspection_model.md). Per default
  *"sensitivity"* is set to 0.0, which means the novelty thresholds
  from the training are used directly when calling
  [`ApplyTextureInspectionModel`](apply_texture_inspection_model.md). If a negative value for the
  parameter *"sensitivity"* is used, the value is added to the novelty
  boundaries.
  Hence, a sensitivity value below 0.0 increments the novelty thresholds and
  therefore leads to potentially fewer detected errors. If instead a positive
  value is set, the novelty thresholds are decremented which leads to
  potentially more detected errors.

  The automatically determined novelty thresholds can be changed
  after the training with the parameter *"novelty_threshold"*.

  List of values:
   float or integer value

  Default:
   *0.0*

### Parameters that influence the texture features:

- ***"patch_normalization"*:** —

  Determines the method used to
  normalize the texture features. A normalization is required if the
  lighting between different images is not consistent. If set to
  *"weber"*, the patches are normalized in accordance with
  the Weber-Fechner law. If the parameter is set to
  *"none"*, no feature normalization is performed.

  Changing this parameter requires a complete new training of the texture
  inspection model.

  List of values:
   *"none"*, *"weber"*

  Default:
   *"none"*
- ***"patch_rotational_robustness"*:** —

  If set to *"true"*,
  the texture features are sorted in a way to obtain a certain amount of
  rotational invariance. Sorting the features leads to a loss of feature
  information and generally makes the texture inspection less
  sensitive. Also, the runtime is slightly increased. If the parameter is
  set to *"false"*, the texture features are not sorted.

  Alternatively, it is possible to capture all possible rotations within
  the training images. Increasing the training images leads to an increase
  of the training time.

  Changing this parameter requires a complete new training of the texture
  inspection model.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*
- ***"patch_size"*:** —

  This parameter determines the diameter of
  the extracted texture feature patches in pixels.
  Higher patch sizes increase the runtime significantly. Therefore this
  parameter should only be changed with great care.
  First try to change the image resolution or the number of pyramids used.

  Changing this parameter requires a complete new training of the texture
  inspection model.

  Value range:
   odd integer values between *1* and *11*

  Default:
   *5*

### Advanced parameters that influence the GMM classifiers:

Internally, the texture inspection model uses a Gaussian Mixture Model
(GMM) classifier. In general, it is recommended not to change the GMM
parameters, but for experienced users this is still possible.

Changing these parameters requires a new training of the texture
inspection model.

In the following, the parameters which influence the GMM classifiers are
described. For more information on classification with GMM classifiers, see
[`CreateClassGmm`](create_class_gmm.md) and [`TrainClassGmm`](train_class_gmm.md).

- ***"gmm_sigma"*:** —

  This parameter determines the standard
  deviation of the Gaussian noise which is added to the training samples
  (see [`AddSampleClassGmm`](add_sample_class_gmm.md)).

  Value range:
   integer or float values larger or equal to *0.0*

  Default:
   *0.0*
- ***"gmm_pmincenters"*:** —

  This parameter determines the minimum
  number of Gaussian distributions per class. *"gmm_pmincenters"*
  cannot be set to a value larger than the current value of
  *"gmm_pmaxcenters"*.

  Value range:
   integer value larger or equal to *1* and less or equal
  to *"gmm_pmaxcenters"*

  Default:
   *12*
- ***"gmm_pmaxcenters"*:** —

  This parameter determines the maximum
  number of Gaussian distributions per class. *"gmm_pmaxcenters"*
  cannot be set to a value smaller than the current value of
  *"gmm_pmincenters"*.

  Value range:
   integer value larger or equal to *"gmm_pmincenters"*

  Default:
   *12*
- ***"gmm_preprocessing"*:** —

  This parameter determines the type of
  preprocessing used to transform the feature vectors.

  List of values:
   *"principal_components"*, *"normalization"*,
  *"none"*

  Default:
   *"normalization"*
- ***"gmm_ncomp"*:** —

  This parameter manipulates the preprocessing
  in case *"principal_components"* is chosen as the preprocessing
  method. More specifically, it determines the dimension of the transformed
  feature vectors. It needs to be chosen such that it is
  smaller than the feature dimension, which is
  *"patch_size"* $\times$ *"patch_size"*.
  If the *"patch_size"* is changed such that
  *"patch_size"* $\times$ *"patch_size"* $<$
  *"gmm_ncomp"*, the parameter is manipulated accordingly.

  Value range:
   integer value larger or equal to *1*

  Default:
   *15*
- ***"gmm_randseed"*:** —

  This parameter determines the
  initialization value for the random number generator, which is required to
  initialize the GMM with random values.

  List of values:
   integer value

  Default:
   *42*
- ***"gmm_em_max_iter"*:** —

  This parameter determines the maximum
  number of iterations of the expectation maximization algorithm.

  Value range:
   integer values larger or equal to *0*

  Default:
   *100*
- ***"gmm_em_threshold"*:** —

  This parameter determines the
  threshold for the relative change of the error for the expectation
  maximization algorithm to terminate.

  Value range:
   integer or float value larger or equal to *0* and smaller
  than *1.0*

  Default:
   *0.001*
- ***"gmm_em_regularize"*:** —

  This parameter determines the
  regularization value for preventing covariance matrix singularity within
  the training process.

  Value range:
   integer or float values larger or equal to *0* and smaller
  than *1.0*

  Default:
   *0.0001*
- ***"gmm_covartype"*:** —

  This parameter determines the type of
  covariance matrix that is used internally.

  List of values:
   *"spherical"*, *"diag"*, *"full"*

  Default:
   *"diag"*

### Changing the parameters of a trained texture inspection model

If parameters of a texture inspection model are manipulated after a
successful call of [`TrainTextureInspectionModel`](train_texture_inspection_model.md), the texture
inspection model usually needs to be retrained. Depending on which parameters
are changed, different parts of the training need to be recalculated.

A manipulation of the parameters *"gmm_*"*
requires a new training of the classifiers. Since a new classifier yields
different novelty scores, the novelty thresholds also need to be
recalculated. The parameter *"patch_*"*
requires a complete new training of the texture inspection model. The
parameters *"num_levels"* and *"levels"* require a retraining
if the number of levels is increased or levels are set which were not trained
beforehand. For example, setting *"levels"* from [1,2,3] to [1,3]
does not require a retraining.
The operator *"gen_result_handle"* has no effect on a trained
texture inspection model and can be manipulated without requiring any
retraining.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- textureInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`textureInspectionModel`** (input_control, state is modified)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the model parameter to be adjusted.

Default:
"gen_result_handle"

List of values:
"gen_result_handle", "gmm_covartype", "gmm_em_max_iter", "gmm_em_regularize", "gmm_em_threshold", "gmm_ncomp", "gmm_pmaxcenters", "gmm_pmincenters", "gmm_preprocessing", "gmm_randseed", "gmm_sigma", "levels", "novelty_threshold", "num_levels", "patch_normalization", "patch_rotational_robustness", "patch_size", "sensitivity"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

New value of the model parameter.

Default:
"true"

List of values:
5, "auto", "false", "none", "normalization", "principal_components", "true", "weber"

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

The operator `SetTextureInspectionModelParam` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateTextureInspectionModel`

## Possible Successors

`AddTextureInspectionModelImage`,
`TrainTextureInspectionModel`

## See also

`GetTextureInspectionModelParam`

## Module

Matching
