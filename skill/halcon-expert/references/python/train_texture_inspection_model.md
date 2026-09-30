# train_texture_inspection_model (Operator)

## Name

`train_texture_inspection_model` — Train a texture inspection model.

## Signature

`def train_texture_inspection_model(texture_inspection_model: HHandle) -> None`

## Description

`train_texture_inspection_model` trains a texture inspection model
with all training images which were added by
[`add_texture_inspection_model_image`](add_texture_inspection_model_image.md).

The complete texture inspection process works with image pyramids. The
depth of the pyramid is determined by the parameter *"num_levels"*
(or *"levels"* if the levels have been set explicitly).
In the first step of the training, texture features are extracted and added
to the set of training samples for each pyramid level.
For each pyramid level a Gaussian Mixture Model (GMM) classifier is
determined with all training samples of the corresponding pyramid level.
In a third step, the training samples are used to determine a novelty
threshold for each pyramid level. In the following, the three training
steps are explained in detail:

1. **Feature extraction** extracts a feature for each pixel within
   the training images. The texture features are calculated according to the
   settings of the *"patch_*"* parameters, which can be manipulated
   with [`set_texture_inspection_model_param`](set_texture_inspection_model_param.md). Each texture feature
   is added to the training data of the GMM.
2. **During the training** of the GMMs, the optimal *"gmm_*"*
   parameters are calculated from the training data. The dimension of the
   single GMMs is determined by the size of the feature patches. Please refer to
   [`set_texture_inspection_model_param`](set_texture_inspection_model_param.md) for details. For large patch
   sizes, it can be extremely difficult to obtain a good approximation of the
   optimal GMM parameters. Also, the run time and memory usage rises
   significantly. Therefore we recommend to alter the default patch size with
   care.

   More information on GMM classifiers can be found in the description of the
   operator [`create_class_gmm`](create_class_gmm.md).
3. **The calculation of the novelty thresholds** is required
   to be able to distinguish between defective and non-defective
   texture. First, the novelty score of each training sample is
   determined with the GMMs determined in step 2. Then, based on
   the resulting novelty scores, novelty thresholds are determined for each
   pyramid level. The automatic determination of the novelty thresholds
   can be influenced with the parameter *"sensitivity"* that can
   be set with [`set_texture_inspection_model_param`](set_texture_inspection_model_param.md).

After the training was successful it is possible to classify images
with [`apply_texture_inspection_model`](apply_texture_inspection_model.md). Each pixel is
assigned a *novelty score* that is compared to the novelty
threshold, which was determined within the third step of the training. For
optimal results it is possible to adapt the novelty threshold of the single
pyramid levels with [`set_texture_inspection_model_param`](set_texture_inspection_model_param.md).

In general, the manipulation of all parameters, with the exception of
*"gen_result_handle"* and *"sensitivity"*, requires a retraining
of the texture inspection model. Depending on which part of the training is
affected by the corresponding parameter, either the whole training or only
single steps have to be recalculated. This can lead to strong variations in
the time required for retraining a texture inspection model. A precise
description which parameters influence which parts of the algorithm are
illustrated in [`set_texture_inspection_model_param`](set_texture_inspection_model_param.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- texture_inspection_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`texture_inspection_model`** (input_control, state is modified)  texture_inspection_model `→` HHandle

Handle of the texture inspection model.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
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

The operator `train_texture_inspection_model` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`add_texture_inspection_model_image`,
`set_texture_inspection_model_param`

## Possible Successors

`apply_texture_inspection_model`,
`clear_texture_inspection_model`,
`remove_texture_inspection_model_image`,
`write_texture_inspection_model`,
`serialize_texture_inspection_model`

## References

X. Xianghua, M. Mirmehdi: “TEXEMS: Texture Exemplars for Defect Detection
on Random Textured Surfaces”; IEEE Transactions on Pattern Analysis and
Machine Intelligence, Vol. 29, No. 8; August 2007.
  
T. Boettger, M. Ulrich: “Real-time Texture Detection on Textured
Surfaces with Compressed Sensing”; Pattern Recognition and Image
Analysis, Vol. 26, No. 1, pp. 88-94; January 2016.

## Module

Matching
