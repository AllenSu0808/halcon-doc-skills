# apply_dl_model (Operator)

## Name

`apply_dl_model` — Apply a deep-learning-based network on a set of images for inference.

## Signature

`def apply_dl_model(dlmodel_handle: HHandle, dlsample_batch: Sequence[HHandle], outputs: Sequence[str]) -> Sequence[HHandle]`

## Description

`apply_dl_model` applies the deep-learning-based network given
by *`dlmodel_handle`* on the batch of input images
handed over through the tuple of dictionaries *`dlsample_batch`*.
The operator returns *`dlresult_batch`*, a tuple with a result
dictionary `dlresult` for every input image.

Please see the chapter [Deep Learning / Model](toc_deeplearning_model.md)
for more information on the concept and the dictionaries of the deep
learning model in HALCON.

In order to apply the network on images, you have to hand them over
through a tuple of dictionaries *`dlsample_batch`*, where a dictionary
refers to a single image. You can create such a dictionary conveniently
using the procedure `gen_dl_samples_from_images`. The tuple
*`dlsample_batch`* can contain an arbitrary number of
dictionaries. The operator `apply_dl_model` always processes
a batch with up to *"batch_size"* images simultaneously.
In case the tuple contains more images, `apply_dl_model` iterates
over the necessary number of batches internally. For a
*`dlsample_batch`* with less than *"batch_size"* images,
the tuple is padded to a full batch which means that the time required
to process a *`dlsample_batch`* is independent of whether the
batch is filled up or just consists of a single image. This also means
that if fewer images than *"batch_size"* are processed in one
operator call, the network still requires the same amount of memory as
for a full batch. The current value of *"batch_size"* can be
retrieved using [`get_dl_model_param`](get_dl_model_param.md).

Note that the images might have to be preprocessed before feeding them into
the operator `apply_dl_model` in order to fulfill the network
requirements. You can retrieve the current requirements of your network,
such as e.g., the image dimensions, using [`get_dl_model_param`](get_dl_model_param.md).
The procedure `preprocess_dl_dataset` provides guidance on how to
implement such a preprocessing stage.

The results are returned in *`dlresult_batch`*, a tuple with a
dictionary `dlresult` for every input image.
Please see the chapter [Deep Learning / Model](toc_deeplearning_model.md)
for more information to the output dictionaries in *`dlresult_batch`*
and their keys.
In *`outputs`* you can specify, which output data is returned in
`dlresult`.
*`outputs`* can be a single string, a tuple of strings, or
an empty tuple with which you retrieve all possible outputs.
If `apply_dl_model` is used with an AI
2-interface, it might be
required to set *"is_inference_output"* = *"true"* for all
requested layers in *`outputs`* before the model is optimized for the
AI
2-interface, see [`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md) and
[`set_dl_model_layer_param`](set_dl_model_layer_param.md) for further details.
The values for *`outputs`* depend on the model type of your network:

- **Models of *"type"*=*"3d_gripping_point_detection"*** —
  - *`outputs`*=*"[]"*: `dlresult` containing:

    - `'gripping_map'`: Binary image, indicating for each pixel of
      the scene whether the model predicted a gripping point
      (pixel value = *1.0*) or not (*0.0*).
    - `'gripping_confidence'`: Image, containing raw, uncalibrated
      confidence values for every point in the scene.
- **Models of *"type"*=*"3d_pose_estimation"*** —

  This model type cannot be run with the operator `apply_dl_model`.
- **Models of *"type"*=*"anomaly_detection"*** —
  - *`outputs`*=*"[]"*: `dlresult`
    contains an image where each pixel has the score of the according input
    image pixel. Additionally it contains a score for the entire image.
- **Models of *"type"*=*"counting"*** —

  This model type cannot be run with the operator `apply_dl_model`.
- **Models of *"type"*=*"gc_anomaly_detection"*** —

  For each value of *`outputs`*, `dlresult`
  contains an image where each pixel has the score of the according input
  image pixel.
  Additionally it contains a score for the entire image.

  - *`outputs`*=*"[]"*:
    The scores of each input image pixel are calculated as a combination of
    all available networks.
  - *`outputs`*=*"anomaly_image_local"*:
    The scores of each input image pixel are calculated from the
    *"local"* network only. If the *"local"* network is not
    available, an error is raised.
  - *`outputs`*=*"anomaly_image_global"*:
    The scores of each input image pixel are calculated from the
    *"global"* network only. If the *"global"* network is not
    available, an error is raised.
  - *`outputs`*=*"anomaly_image_combined"*:
    The scores of each input image pixel are calculated by combining the
    *"global"* and the *"local"* networks.
    If one or both of the networks are not available, an error is raised.
- **Models of *"type"*=*"classification"*** —
  - *`outputs`*=*"[]"*: `dlresult` contains a
    tuple with confidence values in descending order and tuples with the
    class names and class IDs sorted accordingly. If Out-of-Distribution
    Detection is available, `dlresult` additionally contains the
    out-of-distribution score, the out-of-distribution result and the
    threshold that was used for the prediction.
- **Models of *"type"*=*"multi_label_classification"*** —
  - *`outputs`*=*"[]"*: `dlresult` contains a
    tuple with the selected class names, class IDs and the corresponding
    confidence values according to the model parameter *"min_confidence"*.
    Additionally, it contains tuples with all class names, class IDs and
    corresponding confidence values.
- **Models of *"type"*=*"detection"*, OD** —
  - *`outputs`*=*"[]"*: `dlresult` contains
    the bounding box coordinates as well as the inferred classes and their
    confidence values resulting from all levels.
  - *`outputs`*=
    *"[bboxhead + level + _prediction, classhead + level + _prediction]"*,
    where *"level"* stands for the selected level which lies
    between *"min_level"* and *"max_level"*:
    `dlresult` contains the bounding box coordinates as well
    as the inferred classes and their confidence values resulting from
    specific levels.
- **Models of *"type"*=*"detection"*, AOD** —
  - *`outputs`*=*"[]"*: `dlresult` contains
    the bounding box coordinates as well as the inferred classes and their
    confidence values.
- **Models of *"type"*=*"ocr_recognition"*** —
  - *`outputs`*=*"[]"*: `dlresult`
    contains the recognized word.
    Additionally it contains candidates for each character of the
    word and their confidences.
- **Models of *"type"*=*"ocr_detection"*** —
  - *`outputs`*=*"[]"*: `dlresult`
    contains the bounding boxes coordinates of localized words.
- **Models of *"type"*=*"segmentation"*** —
  - *`outputs`*=*"segmentation_image"*:
    `dlresult` contains an image where each pixel has a value
    corresponding to the class
    its corresponding pixel has been assigned to.
  - *`outputs`*=*"segmentation_confidence"*:
    `dlresult` contains an image where each pixel has the
    confidence value out of the classification of the according pixel.
  - *`outputs`*=*"[]"*:
    `dlresult` contains all output values.

## Attention

System requirements:
To run this operator on GPU by setting *"device"* to *"gpu"*
(see [`get_dl_model_param`](get_dl_model_param.md)), cuDNN and cuBLAS are required.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

This operator supports breaking timeouts and interrupts.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of the deep learning model.

**`dlsample_batch`** (input_control)  dict-array `→` Sequence[HHandle]

Input data.

**`outputs`** (input_control)  string-array `→` Sequence[str]

Requested outputs.

Default:
[]

List of values:
[], "bboxhead2_prediction", "classhead2_prediction", "segmentation_confidence", "segmentation_image"

**`dlresult_batch`** (output_control)  dict-array `→` Sequence[HHandle]

Result data.

## Result

If the parameters are valid, the operator `apply_dl_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`read_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`,
`set_dl_model_param`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Enhanced, Deep Learning Professional
