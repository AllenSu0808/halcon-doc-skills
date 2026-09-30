# GetDlModelParam (Operator)

## Name

`GetDlModelParam` — Return the parameters of a deep learning model.

## Signature

`static void HOperatorSet.GetDlModelParam(HTuple DLModelHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDlModel.GetDlModelParam(string genParamName)`

## Description

`GetDlModelParam` returns the parameter values
*`genParamValue`* of *`genParamName`* for the deep learning
model *`DLModelHandle`*.

For a deep learning model, parameters *`genParamName`* can be set using
[`SetDlModelParam`](set_dl_model_param.md) or [`CreateDlModelDetection`](create_dl_model_detection.md), depending
on the parameter and the model type.
With this operator, `GetDlModelParam`, you can retrieve
the parameter values *`genParamValue`*.
Below we give an overview of the different parameters and an explanation,
except of those you can only set. For latter ones, please see the
documentation of corresponding operator.
The parameters are listed corresponding to the deep learning model methods:

To mark which operators are available for the methods, we use the following
notations:

- `set`: The parameter can be set using [`SetDlModelParam`](set_dl_model_param.md).
- `get`: The parameter can be retrieved using
  `GetDlModelParam`.
- `create`: The parameter can be set using
  [`CreateDlModelDetection`](create_dl_model_detection.md).
- Certain parameters are set as non-optional parameters, the corresponding
  notation is given in brackets.

3D Gripping Point Detection

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"class_ids"* | `x` | `x` |
| *"class_names"* |  | `x` |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* |  | `x` |
| *"image_range_max"*, *"image_range_min"* | `x` | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Deep 3D Matching pose estimation component

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* |  | `x` |
| *"image_height"*, *"image_width"* |  | `x` |
| *"image_num_channels"* |  | `x` |
| *"image_range_max"*, *"image_range_min"* |  | `x` |
| *"image_size"* |  | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Anomaly Detection

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"batch_size"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"complexity"* | `x` | `x` |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* |  | `x` |
| *"image_range_max"*, *"image_range_min"* |  | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"num_trainable_params"* |  | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"standard_deviation_factor"* | `x` | `x` |
| *"type"* |  | `x` |

Classification

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"class_ids"* |  | `x` |
| *"class_names"* | `x` | `x` |
| *"class_weights"* | `x` | `x` |
| *"clear_ood"* | `x` |  |
| *"continual_learning_available"* |  | `x` |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"extract_feature_maps"* | `x` | `x` |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* |  | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"ood_available"* |  | `x` |
| *"ood_threshold"* | `x` | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Multi-Label Classification

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"class_ids"* | `x` | `x` |
| *"class_names"* | `x` | `x` |
| *"device"* | `x` | `x` |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* |  | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"min_confidence"* | `x` | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Deep Counting component

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"device"* | `x` | `x` |
| *"gpu"* | `x` | `x` |
| *"input_dimensions"* |  | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* |  | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"solver_type"* |  | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Deep OCR detection component

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* | `x` | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_character_score"* | `x` | `x` |
| *"min_link_score"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"min_word_area"* | `x` | `x` |
| *"min_word_score"* | `x` | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"orientation"* | `x` | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"sort_by_line"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"tiling"* | `x` | `x` |
| *"tiling_overlap"* | `x` | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Deep OCR recognition component

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"alignment"* | `x` | `x` |
| *"alignment_available"* |  | `x` |
| *"alphabet"* | `x` | `x` |
| *"alphabet_internal"* | `x` | `x` |
| *"alphabet_mapping"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* | `x` | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Global Context Anomaly Detection

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"anomaly_score_tolerance"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gc_anomaly_networks"* | `x` | `x` |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* |  | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* |  | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"patch_size"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Advanced Object Detection

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"bbox_heads_weight"*, *"class_heads_weight"* | `x` | `x` |
| *"class_ids"* | `x` | `x` |
| *"class_names"* | `x` | `x` |
| *"device"* | `x` | `x` |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* | `x` | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"instance_type"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"max_num_detections"* | `x` | `x` |
| *"max_num_gt"* | `x` | `x` |
| *"max_overlap"* | `x` | `x` |
| *"max_overlap_class_agnostic"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_confidence"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_classes"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

Instance Segmentation, Object Detection

| *`genParamName`* | `set` | `get` | `create` |
| --- | --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |  |
| *"adam_beta2"* | `x` | `x` |  |
| *"adam_epsilon"* | `x` | `x` |  |
| *"anchor_angles"* |  | `x` | `x` |
| *"anchor_aspect_ratios"* |  | `x` | `x` |
| *"anchor_num_subscales"* |  | `x` | `x` |
| *"backbone"* (`backbone`) |  | `x` | `x` |
| *"backbone_docking_layers"* | `x` | `x` | `x` |
| *"batch_size"* | `x` | `x` |  |
| *"batch_size_multiplier"* | `x` | `x` |  |
| *"batchnorm_momentum"* | `x` |  |  |
| *"bbox_heads_weight"*, *"class_heads_weight"* | `x` | `x` | `x` |
| *"capacity"* |  | `x` | `x` |
| *"class_ids"* | `x` | `x` | `x` |
| *"class_ids_no_orientation"* |  | `x` | `x` |
| *"class_names"* | `x` | `x` | `x` |
| *"class_weights"* |  | `x` |  |
| *"device"* | `x` | `x` |  |
| *"enable_resizing"* | `x` |  |  |
| *"freeze_backbone_level"* | `x` | `x` | `x` |
| *"fuse_bn_relu"* | `x` |  |  |
| *"fuse_conv_bn"* | `x` |  |  |
| *"fuse_conv_relu"* | `x` |  |  |
| *"gpu"* | `x` | `x` |  |
| *"ignore_direction"* |  | `x` | `x` |
| *"image_dimensions"* |  | `x` | `x` |
| *"image_height"*, *"image_width"* |  | `x` | `x` |
| *"image_num_channels"* |  | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* |  | `x` |  |
| *"image_size"* |  | `x` | `x` |
| *"input_dimensions"* |  | `x` |  |
| *"instance_segmentation"* |  | `x` | `x` |
| *"instance_type"* |  | `x` | `x` |
| *"layer_names"* |  | `x` |  |
| *"learning_rate"* | `x` | `x` |  |
| *"mask_head_weight"* | `x` | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |  |
| *"max_level"*, *"min_level"* |  | `x` | `x` |
| *"max_num_detections"* | `x` | `x` | `x` |
| *"max_overlap"* | `x` | `x` | `x` |
| *"max_overlap_class_agnostic"* | `x` | `x` | `x` |
| *"meta_data"* | `x` | `x` |  |
| *"min_confidence"* | `x` | `x` | `x` |

| *"min_version"* |  | `x` |  |
| --- | --- | --- | --- |
| *"momentum"* | `x` | `x` |  |
| *"num_classes"* (`numClasses`) |  | `x` | `x` |
| *"num_trainable_params"* |  | `x` |  |
| *"optimize_for_inference"* | `x` | `x` | `x` |
| *"precision"* |  | `x` |  |
| *"precision_is_converted"* |  | `x` |  |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |  |
| *"runtime_init"* | `x` |  |  |
| *"solver_type"* | `x` | `x` |  |
| *"summary"* |  | `x` |  |
| *"type"* |  | `x` |  |
| *"weight_decay"* | `x` | `x` |  |
| *"weight_prior"* | `x` | `x` |  |

Semantic Segmentation, Edge Extraction

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"adam_beta1"* | `x` | `x` |
| *"adam_beta2"* | `x` | `x` |
| *"adam_epsilon"* | `x` | `x` |
| *"batch_size"* | `x` | `x` |
| *"batch_size_multiplier"* | `x` | `x` |
| *"batchnorm_momentum"* | `x` |  |
| *"class_ids"* | `x` | `x` |
| *"class_names"* | `x` | `x` |
| *"device"* | `x` | `x` |
| *"enable_resizing"* | `x` |  |
| *"fuse_bn_relu"* | `x` |  |
| *"fuse_conv_bn"* | `x` |  |
| *"fuse_conv_relu"* | `x` |  |
| *"gpu"* | `x` | `x` |
| *"ignore_class_ids"* | `x` | `x` |
| *"image_dimensions"* | `x` | `x` |
| *"image_height"*, *"image_width"* | `x` | `x` |
| *"image_num_channels"* | `x` | `x` |
| *"image_range_max"*, *"image_range_min"* | `x` | `x` |
| *"image_size"* | `x` | `x` |
| *"input_dimensions"* | `x` | `x` |
| *"layer_names"* |  | `x` |
| *"learning_rate"* | `x` | `x` |
| *"max_gradient_norm"* | `x` | `x` |
| *"meta_data"* | `x` | `x` |
| *"min_version"* |  | `x` |
| *"momentum"* | `x` | `x` |
| *"num_classes"* |  | `x` |
| *"num_trainable_params"* |  | `x` |
| *"optimize_for_inference"* | `x` | `x` |
| *"precision"* |  | `x` |
| *"precision_is_converted"* |  | `x` |
| *"pretrained"* | `x` |  |
| *"runtime"* | `x` | `x` |
| *"runtime_init"* | `x` |  |
| *"solver_type"* | `x` | `x` |
| *"summary"* |  | `x` |
| *"tiling"* | `x` | `x` |
| *"tiling_overlap"* | `x` | `x` |
| *"type"* |  | `x` |
| *"weight_decay"* | `x` | `x` |
| *"weight_prior"* | `x` | `x` |

In the following we list and explain the parameters *`genParamName`*
for which you can retrieve their value using this operator,
`GetDlModelParam`.
Note, that only parameters that do not change the model architecture can be
set after the model has been optimized with
[`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md). A list of these parameters can be
found at [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md).
Thereby, the following symbols denote the model type for which the parameter
can be get:

- 'Any': any method
- '3D-GPD': *"type"*=*"3d_gripping_point_detection"*
- '3D-PE': *"type"*=*"3d_pose_estimation"*
- 'AD': *"type"*=*"anomaly_detection"*
- 'AOD': *"type"*=*"detection"*. Advanced Object Detection
- 'CL': *"type"*=*"classification"*
- 'MLC': *"type"*=*"multi_label_classification"*
- 'DC': *"type"*=*"counting"*
- 'OCR-D': *"type"*=*"ocr_detection"*
- 'OCR-R': *"type"*=*"ocr_recognition"*
- 'GC-AD': *"type"*=*"gc_anomaly_detection"*
- 'OD': *"type"*=*"detection"*
- 'SE': *"type"*=*"segmentation"*
- 'Gen': *"type"*=*"generic"*

- ***"adam_beta1"*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

  This value defines the moment for the linear term in Adam solver.
  For more information we refer to the documentation of
  [`TrainDlModelBatch`](train_dl_model_batch.md).

  Restriction:
   Only applicable for
  *"solver_type"* = *"adam"*.

  Default:
   *"adam_beta1"* = *0.9*
- ***"adam_beta2"*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

  This value defines the moment for the quadratic term in Adam solver.
  For more information we refer to the documentation of
  [`TrainDlModelBatch`](train_dl_model_batch.md).

  Restriction:
   Only applicable for
  *"solver_type"* = *"adam"*.

  Default:
   *"adam_beta2"* = *0.999*
- ***"adam_epsilon"*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

  This value defines the epsilon in the Adam solver formula and is
  purposed to guarantee the numeric stability.
  For more information we refer to the documentation of
  [`TrainDlModelBatch`](train_dl_model_batch.md).

  Restriction:
   Only applicable for
  *"solver_type"* = *"adam"*.

  Default:
   *"adam_epsilon"* = *1e-08*
- ***"alignment"*: OCR-R** —

  This parameter specifies whether word alignment is performed
  prior to recognizing the text. Enabling this feature (*"true"*)
  improves the recognition accuracy for inaccurately cropped words.
  Therefore, it can be used in scenarios where the position of the text
  within the image is only approximately known.

  The parameter *"alignment"* can only be set to *"true"*
  if the recognition component includes word alignment. To check whether
  the model supports alignment, use the parameter
  *"alignment_available"*.

  Note that in contrast to recognition of tightly cropped words,
  aligned recognition requires to be trained with samples containing
  real image backgrounds around the words. In this manner, the model
  learns to suppress false readings in the background which can be
  present after aligning inaccurately cropped words.

  List of values:
   *"true"*, *"false"*

  Default:
   *"false"*
- ***"alignment_available"*: OCR-R** —

  This parameter indicates whether the recognition component contains
  word alignment functionality. If it returns *"true"*, it means
  that word alignment can be enabled using the parameter
  *"alignment"*.

  List of values:
   *"true"*, *"false"*
- ***"alphabet"*: OCR-R** —

  The character set that can be recognized by the Deep OCR model.

  It contains all characters that are not mapped to the Blank character
  of the internal alphabet (see parameters
  *"alphabet_mapping"* and *"alphabet_internal"*).

  The alphabet can be changed or extended if needed. Changing the
  alphabet with this parameter will edit the internal alphabet and
  mapping in such a way that it tries to keep the length of the internal
  alphabet unchanged.
  After changing the alphabet, it is recommended to retrain the model on
  application specific data (see the HDevelop example
  `deep_ocr_recognition_training_workflow.hdev`).
  Previously unknown characters will need more training data.

  Note, that if the length of the internal alphabet changes, the last
  model layers have to be randomly initialized and thus the output of the
  model will be random strings (see *"alphabet_internal"*).
  In that case it is required to retrain the model.
- ***"alphabet_internal"*: OCR-R** —

  The full character set which the Deep OCR recognition component has
  been trained on.

  The first character of the internal alphabet is a special character.
  In the pretrained model this character is specified as Blank
  (U+2800) and is not to be confused with a space.
  The Blank is never returned in a word output but can occur in the
  reported character candidates. It is required and cannot be omitted.
  If the internal alphabet is changed, the first character has to be
  the Blank.
  Furthermore, if *"alphabet"* is used to change
  the alphabet, the Blank symbol is added automatically to the
  character set.

  The length of this tuple corresponds to the depth of the last
  convolution layer in the model. If the length changes, the last
  convolution layer and all layers after it have to be resized and
  potentially reinitialized randomly. After such a change, it is required
  to retrain the model (see HDevelop example
  `deep_ocr_recognition_training_workflow.hdev`).

  It is recommended to use the parameter *"alphabet"* to
  change the alphabet, as it will automatically try to preserve the
  length of the internal alphabet.
- ***"alphabet_mapping"*: OCR-R** —

  Tuple of integer indices.

  It is a mapping that is applied by the model during the decoding step
  of each word. The mapping overwrites a character of
  *"alphabet_internal"* with the character at the specified
  index in *"alphabet_internal"*.

  In the decoding step each prediction is mapped according to the index
  specified in this tuple.
  The tuple has to be of same length as the tuple
  *"alphabet_internal"*. Each integer index of the
  mapping has to be within *0* and
  |*"alphabet_internal"*|-1.

  In some applications it can be helpful to map certain characters onto
  other characters. E.g. if only numeric words occur in an application it
  might be helpful to map the character "O" to the "0" character
  without the need to retrain the model.

  If an entry contains a *0*, the corresponding character in
  *"alphabet_internal"* will not be decoded in the
  word.
- ***"anchor_angles"*: OD** —

  The parameter *"anchor_angles"* determines the orientation
  angle of the anchors for a model of
  *"instance_type"* = *"rectangle2"*.

  Thereby, the orientation is given in arc measure and indicates
  the angle between the horizontal axis and `length1`
  (mathematically positive).
  See the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for more
  explanations to anchors.

  You can set a tuple of values.
  A higher number of angles increases the number of anchors
  which might lead to a better localization but also increases the
  runtime and memory-consumption.

  Value range:
  *"anchor_angles"* $\in(-\pi,\pi]$
  for *"ignore_direction"* = *"false"*,
  *"anchor_angles"* $\in(-\pi/2,\pi/2]$
  for *"ignore_direction"* = *"true"*

  Default:
   *"anchor_angles"* = *[0.0]*
- ***"anchor_aspect_ratios"*
  (legacy: *"aspect_ratios"*): OD** —

  The parameter *"anchor_aspect_ratios"* determines the aspect
  ratio of the anchors. Thereby, the definition of the ratio depends on
  the *"instance_type"*:

  - *"rectangle1"*: height-to-width ratio
  - *"rectangle2"*: ratio length1 to length2

  E.g., for instance type *"rectangle1"* the ratio 2 gives
  a narrow and 0.5 a broad anchor.
  The size of the anchor is affected by the parameter
  *"anchor_num_subscales"* and with its explanation we give the
  formula for the sizes and lengths of the generated anchors.
  See the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for more
  explanations to anchors.

  You can set a tuple of values.
  A higher number of aspect ratios increases the number of anchors
  which might lead to a better localization but also increases the
  runtime and memory-consumption.

  For reasons of backward compatibility, the parameter name
  *"aspect_ratios"* can be used instead of
  *"anchor_aspect_ratios"*.

  Default:
   *"anchor_aspect_ratios"* =
  *[1.0, 2.0, 0.5]*
- ***"anchor_num_subscales"*
  (legacy: *"num_subscales"*): OD** —

  This parameter determines the number of different sizes with which
  the anchors are generated at the different levels used.

  In HALCON for every anchor point, thus every pixel of every feature
  map of the feature pyramid, a set of anchors is proposed.
  See the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for
  more explanations to anchors.
  Thereby the parameter *"anchor_num_subscales"* affects the size
  of the anchors.
  An example is shown in the figure below.

  ![figure](../assets/4e0787c79f9ff45a.svg)

  With *"anchor_num_subscales"*=2 we generate for every aspect
  ratio 2 anchors of different size on each level: One with the base
  length (solid line) and an additional, larger one (dotted line).
  Thereby, in the image these additional anchors of
  the lower level (orange) converge to the anchor of
  the next higher level (blue).

  An anchor of level $l$ has by default a edge lengths of
  $b\cdot2^{l}$ in the input image, whereby
  the parameter has the value $b=4$.
  With the parameter *"anchor_num_subscales"* additional anchors
  can be generated, which converge in size to the smallest anchor
  of the level $l+1$. More precisely, these anchors
  of level $l$ have in the input image the edge lengths
  $$scale_i = b \cdot 2^{l+i/\prime anchor_num_subscales'}$$ ![figure](../assets/ee989d73f3ea54ac.svg)
  where
  $i\in[0,^{\prime}\textit{anchor}\_\textit{num}\_\textit{subsc ales}^{\prime}-1]$.
  For subscale $i$, this results on level $l$ in an
  anchor of height $h$ and width $w$ equal
  $$h_{ij} = scale l_i \cdot \sqrt{r_j}, \nw_{lij} = scale l_i \cdot \frac{1}{\sqrt{r_j}}$$ ![figure](../assets/fb18e3c1f70df7d1.svg)
  where $r_{j}$ is the ratio of this anchor
  (see *"anchor_aspect_ratios"*).

  A larger number of subscales increases the number of anchors
  and will therefore increase the runtime and memory-consumption.

  For reasons of backward compatibility, the parameter name
  *"num_subscales"* can be used instead of
  *"anchor_num_subscales"*.

  Default:
   *"anchor_num_subscales"* = *3*
- ***"anomaly_score_tolerance"*: GC-AD** —

  The image-level anomaly score is calculated internally such that
  a certain fraction of the pixel-level anomaly scores in
  `anomaly_image` is greater or equal to the image-level
  anomaly score. The value of this fraction can be set by
  *"anomaly_score_tolerance"* and has to be in the interval
  *[0.0, 1.0]*.
  For example, for *"anomaly_score_tolerance"*=*0.01*,
  1 percent of the pixel anomaly scores are larger or equal to the
  image anomaly score. This can be used to suppress outliers
  that might appear in the pixel anomaly scores.

  Default:
   *"anomaly_score_tolerance"* = *0.0*
- ***"backbone"*: OD** —

  The parameter *"backbone"* is the name (together with the path)
  of the backbone network which is used to create the model. A list of
  the delivered backbone networks can be found under
  [`CreateDlModelDetection`](create_dl_model_detection.md).
- ***"backbone_docking_layers"*: CL** —

  The parameter *"backbone_docking_layers"* specifies which
  layers of the backbone are to be used as docking layers by the
  feature pyramid.
  Thereby the layers are referenced by their names.

  The docking layers can be specified for every classifier, also without
  using them as backbone.
  The specification is only considered for object detection backbones.
  When selecting the docking layers, consider that the feature map
  lengths have to be halved from one docking layer to the other.
  Rule of thumb: Use the deepest layers for every (lateral) resolution
  in the backbone (corresponding to one of the required levels for your
  object detection task).

  Information about the names and sizes of the layers in a model can be
  enquired using *"summary"*.

  Default:
   For the pretrained backbones delivered by HALCON
  the defaults depend on the classifier. Other classifiers do not have
  any docking layers set by default and therefore need to have this
  parameter set before they can be used as backbone.
- ***"batch_size"*: Any** —

  Number of input images (and corresponding labels) in a batch that
  is transferred to device memory.

  For a training using [`TrainDlModelBatch`](train_dl_model_batch.md), the batch of images
  which are processed simultaneously in a single training iteration
  contains a number of images which is equal to *"batch_size"*
  times *"batch_size_multiplier"*. Please refer to
  [`TrainDlModelBatch`](train_dl_model_batch.md) for further details.

  For inference, the *"batch_size"* can be generally set
  independently from the number of input images.
  See [`ApplyDlModel`](apply_dl_model.md) for details on how to set this parameter
  for greater efficiency.

  - **Models of *"type"*=*"classification"*:** —

    The parameter *"batch_size"* is stored in the pretrained
    classifier. Per default, the *"batch_size"* is set such
    that a training of the pretrained classifier with up to
    `100` classes can be easily performed on a device with
    `8` gigabyte of memory.

    For the pretrained classifiers, the default values are hence
    given as follows:

    | **pretrained classifier** | default value of *"batch_size"* |
    | --- | --- |
    | *"pretrained_dl_classifier_alexnet.hdl"* | *230* |
    | *"pretrained_dl_classifier_compact.hdl"* | *160* |
    | *"pretrained_dl_classifier_enhanced.hdl"* | *96* |
    | *"pretrained_dl_classifier_mobilenet_v2.hdl"* | *40* |
    | *"pretrained_dl_classifier_resnet18.hdl"* | *24* |
    | *"pretrained_dl_classifier_resnet50.hdl"* | *23* |
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"batch_size"* has no effect.
- ***"batch_size_multiplier"*: Any except AOD** —

  Multiplier for *"batch_size"* to enable training with larger
  numbers of images in one step which would otherwise not be possible
  due to GPU memory limitations. This model parameter does only affect
  [`TrainDlModelBatch`](train_dl_model_batch.md) and thus has no
  impact during evaluation and inference.
  For detailed information see [`TrainDlModelBatch`](train_dl_model_batch.md).

  - **Models of *"type"*=*"anomaly_detection"*:** —

    The parameter *"batch_size_multiplier"* has no effect.
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"batch_size_multiplier"* has no effect.
  - **Models of *"type"*=*"ocr_recognition"*:** —

    The parameter *"batch_size_multiplier"* has no effect.

  Default:
   *"batch_size_multiplier"* = *1*
- ***"bbox_heads_weight"*,
  *"class_heads_weight"*: AOD OD** —

  The parameters *"bbox_heads_weight"* and
  *"class_heads_weight"* are weighting factors for the
  calculation of the total loss.
  This means, when the losses of the individual networks are summed up,
  the contributions from the bounding box regression heads are weighted
  by a factor *"bbox_heads_weight"* and the contributions from
  the classification heads are weighted by a factor
  *"class_heads_weight"*.

  Default:
   for OD *"bbox_heads_weight"* = *1.0*,
  *"class_heads_weight"* = *1.0*

  Default:
   for AOD *"bbox_heads_weight"* = *7.5*,
  *"class_heads_weight"* = *0.5*
- ***"capacity"*: OD** —

  This parameter roughly determines the number of parameters
  (or filter weights) in the deeper sections of the object detection
  network (after the backbone). Its possible values are
  *"high"*, *"medium"*, and *"low"*.

  It can be used to trade-off between detection performance and
  speed. For simpler object detection tasks, the *"low"* or
  *"medium"* settings may be sufficient to achieve the same
  detection performance as with *"high"*.

  Default:
   *"capacity"* = *"high"*
- ***"class_ids"*: 3D-GPD CL MLC AOD OD SE** —

  Unique IDs of the classes the model shall distinguish.
  The tuple is of length *"num_classes"*.

  We stress out the slightly different meanings and restrictions
  depending on the model type:

  - **Models of *"type"*=*"3d_gripping_point_detection"*:** —

    Two classes, in fixed order [*"gripping_map"*, *"background"*],
    are supported for this model. Therefore, for such a model the tuple
    has a fixed length of 2. Thereby, you can set any integer within
    the interval $[0,65534]$ as class ID value.
  - **Models of *"type"*=*"classification"*:** —

    The IDs are unique identifiers, which are automatically assigned
    to each class. The ID of a class corresponds to the index within
    the tuple *"class_names"*.
  - **Models of *"type"*=*"multi_label_classification"*:** —

    The IDs are unique identifiers of the classes to be detected.
    Thereby, you can set any integer as class ID value.

    Value range:
     $[0,65534]$.
  - **Models of *"type"*=*"detection"*:** —

    Only the classes of the objects to be detected are included and
    therewith no background class.
    Thereby, you can set any integer within the interval
    $[0,65534]$ as class ID value.

    Note that the values of *"class_ids_no_orientation"* depend
    on *"class_ids"*. Thus if *"class_ids"* is changed
    after the creation of the model,
    *"class_ids_no_orientation"* is reset to an empty tuple.

    Default:
     *"class_ids"* =
    *"[0,...,num_classes-1]"*
  - **Models of *"type"*=*"segmentation"*:** —

    Every class used for training has to be included and therewith
    also the class ID of the 'background' class.
    Therefore, for such a model the tuple has a minimal length of 2.
    Thereby, you can set any integer within the interval
    $[0,65534]$ as class ID value.
- ***"class_ids_no_orientation"*: OD** —

  With this parameter you can declare classes, for which the orientation
  will not be considered,
  e.g., round or other point symmetrical objects.
  For each class, whose class ID is present in
  *"class_ids_no_orientation"*, the network returns
  axis-aligned bounding boxes.

  Note, this parameter only affects networks of
  *"instance_type"* = *"rectangle2"*.

  Note that the values of *"class_ids_no_orientation"* depend
  on *"class_ids"*. Thus if *"class_ids"* is changed
  after the creation of the model,
  *"class_ids_no_orientation"* is reset to an empty tuple.

  Default:
   *"class_ids_no_orientation"* = *[]*
- ***"class_names"*: 3D-GPD CL MLC AOD OD SE** —

  Unique names of the classes the model shall distinguish.
  The order of the class names remains unchanged after the setting.
  The tuple is of length *"num_classes"*.

  Restriction:
   For a *"3d_gripping_point_detection"* model,
  the *"class_names"* tuple has a fixed length of 2,
  with constant value [*"gripping_map"*, *"background"*].
- ***"class_weights"*: CL OD** —

  The parameter *"class_weights"* is a tuple
  of class specific weighting factors for the loss.
  Giving the unique classes a different weight, it is possible
  to force the network to learn the classes with different importance.
  This is useful in cases where a class dominates the dataset.
  The weighting factors have to be within the interval
  $(0,1)$. Thereby a class gets a stronger
  impact during the training the larger its weight is.
  The weights in the tuple *"class_weights"* are sorted the same
  way as the classes in the tuple *"class_ids"*.
  We stress out the slightly different meanings and restrictions
  depending on the model type:

  - **Models of *"type"*=*"classification"*:** —

    Default:
     *"class_weights"* = *1.0* for each class.
  - **Models of *"type"*=*"detection"*, OD:** —

    Default:
     *"class_weights"* = *0.25* for each class.
- ***"clear_ood"*: CL** —

  This parameter deactivates the out-of-distribution detection of a deep
  learning model. All related information will be deleted.
  [`FitDlOutOfDistribution`](fit_dl_out_of_distribution.md) can be called to fit the
  out-of-distribution detection again.

  Default:
   *"true"*
- ***"max_gradient_norm"*: Any** —

  This parameter controls the maximum L2 norm of the gradients during training,
  also known as gradient clipping.
  The default value *"max_gradient_norm"* = *0.0* disables
  gradient norm limiting. For *"max_gradient_norm"* > *0.0*,
  the total norm of the gradients is limited to this value, which can help
  stabilizing the training of a deep learning model.
  All gradients of the model's weights and biases are scaled as follows:
  $$g_i = g_i \cdot \frac{\max\_gradient\_norm}{\sqrt{\sum_j ||g_j||^2}}$$ ![figure](../assets/f82072e356b552c6.svg)
  where $\|g_{j}\|$ is the L2 norm of gradient $j$, which can be
  retrieved using the operator [`GetDlModelLayerWeights`](get_dl_model_layer_weights.md).
  For typical applications, we recommend testing the values for *"max_gradient_norm"*
  between $1.0,...,5.0$.

  Default:
   *0.0*
- ***"complexity"*: AD** —

  This parameter controls the capacity of the model to deal with more
  complex applications. A higher value allows for the model to represent
  images showing more complexity.
  Increasing the parameter leads to higher runtimes during training and
  inference.
  Please note that this parameter can only be set before the model is
  trained. Setting *"complexity"* on an already trained model
  would render this model useless. When trying to do so, an error is
  returned but the model itself is unchanged.

  Default:
   *"complexity"* = *15*
- ***"continual_learning_available"*: CL** —

  This parameter specifies whether a classification model has been initialized for
  Continual Learning.
  If the operator [`InitDlContinualLearning`](init_dl_continual_learning.md) has been called for
  the model, the value of *"continual_learning_available"* is *"true"*.
  Otherwise it is *"false"*.

  Default:
   *"false"*
- ***"device"*: Any** —

  Handle of the device on which the deep learning operators will be
  executed.

  If the model was already optimized for a device, setting *"device"*
  might not be necessary anymore, see
  [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md) for details.

  To get a tuple of handles of all available potentially deep-learning capable
  hardware devices use [`QueryAvailableDlDevices`](query_available_dl_devices.md).

  Default:
   Handle of the default device, thus the GPU with index
  *0*. If not available, this is an empty tuple.
- ***"extract_feature_maps"*: CL** —

  With this parameter value you can extract feature maps of the
  specified model layer for an inferred image.
  The selected layer must be part of the existing network. An overview of
  all existing layers of the model can be returned by the operator
  `GetDlModelParam` with the corresponding parameter
  *"summary"*.

  Note, using this option modifies the network architecture:
  The network is truncated after a selected layer.
  This modification can not be reversed.
  If the original network architecture should be used again
  it must be read in again with the operator [`ReadDlModel`](read_dl_model.md).
- ***"freeze_backbone_level"*: OD** —

  This parameter determines the backbone levels whose weights are
  kept (meaning not updated and thus frozen) during training.
  Thereby the given number signifies the highest level whose layers
  are frozen in the backbone. Setting *"freeze_backbone_level"*
  to *0*, for no level the weights are frozen and as a
  consequence the weights of all layers are updated. It is
  recommended to set this in case the weights have been randomly
  initialized (e.g., after certain changes of the number of image
  channels) or the in case the backbone is not pretrained.

  Default:
   *"freeze_backbone_level"* = *2*
- ***"gc_anomaly_networks"*: GC-AD** —

  This parameter is used to select the subnetworks of the model.
  The following values can be set:

  - *"local"*: The local subnetwork will be extracted.
  - *"global"*: The global subnetwork will be extracted.

  We refer to [Deep Learning / Anomaly Detection and Global Context Anomaly Detection](toc_deeplearning_anomalydetection.md)
  for more general information on the subnetworks and their properties.

  Note, the original model contains both a *"local"* and a
  *"global"* subnetwork. Once the model architecture is reduced
  to a single subnetwork, the original network is truncated. This cannot
  be undone. If the original model architecture is to be used again,
  it must be read in again with [`ReadDlModel`](read_dl_model.md).

  Default:
   *"gc_anomaly_networks"* =
  *["local", "global"]*
- ***"gpu"*: Any** —

  Identifier of the GPU where the training and inference operators
  ([`TrainDlModelBatch`](train_dl_model_batch.md) and [`ApplyDlModel`](apply_dl_model.md)) are executed.
  Per default, the first available GPU is used.
  [`GetSystem`](get_system.md) with *"cuda_devices"* can be used to
  retrieve a list of available GPUs. Pass the index in this list to
  *"gpu"*.

  Note that the parameter *"gpu"* is only taken into account for
  *"runtime"* = *"gpu"*.
  Therefore, it is preferable to set the GPU device, on which operators are
  run, using the parameter *"device"*.
  executed.

  Default:
   *"gpu"* = *0*
- ***"ignore_class_ids"*: SE** —

  With this parameter you can declare one or multiple classes as
  'ignore' classes, see the chapter
  [Deep Learning / Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md) for further information.
  These classes are declared over their ID (integers).

  Note, you can not set a class ID in *"ignore_class_ids"* and
  *"class_ids"* simultaneously.
- ***"ignore_direction"*: OD** —

  This parameter determines whether for the oriented bounding box
  also the direction of the object within the bounding box is considered
  or not.
  In case the direction within the bounding box is not to be considered
  you can set *"ignore_direction"* to *"true"*.
  In order to determine the bounding box unambiguously, in this case
  (but only in this case) the following conventions apply:

  - $-\pi/2<$ *"phi"* $\le\pi/2$
  - *"bbox_length1"* > *"bbox_length2"*

  This is consistent to [`SmallestRectangle2`](smallest_rectangle2.md).

  Note, this parameter only affects networks of
  *"instance_type"* = *"rectangle2"*.

  List of values:
   *"true"*, *"false"*

  Default:
   *"ignore_direction"* = *"false"*
- ***"image_dimensions"*: 3D-GPD 3D-PE AD CL MLC OCR-D OCR-R GC-AD AOD OD SE** —

  Tuple containing the input image dimensions *"image_width"*,
  *"image_height"*, and number of channels
  *"image_num_channels"*.

  The respective default values and possible value ranges depend on the
  model and model type.
  Please see the individual dimension parameter description for more
  details.
- ***"image_height"*,
  *"image_width"*: 3D-GPD 3D-PE AD CL MLC OCR-D OCR-R GC-AD AOD OD SE** —

  Height and width of the input images, respectively, that the network
  will process.

  This parameter can attain different values depending on the model type:

  - **Models of *"type"*=*"3d_gripping_point_detection"*:** —

    The network architectures allow changes of the image height and width.

    The default values are given by the network, see
    [`ReadDlModel`](read_dl_model.md).
  - **Models of *"type"*=*"3d_pose_estimation"*:** —

    The network architecture does not allow changes of the image height and width.

    The default values are given by the network, see
    [`CreateDeepMatching3d`](create_deep_matching_3d.md).
  - **Models of *"type"*=*"anomaly_detection"*:** —

    The default values depend on the specific pretrained network,
    see [`ReadDlModel`](read_dl_model.md).
    The network architectures allow changes of the image dimensions,
    which can be done using [`SetDlModelParam`](set_dl_model_param.md). Please also
    refer to [`ReadDlModel`](read_dl_model.md) for restrictions each of the
    delivered networks has on the input image size.
    Note that these parameters have to be set before training the model.
    Setting them on an already trained model would render this model
    useless. When trying to do so, an error is returned but the model
    itself is unchanged.
  - **Models of *"type"*=*"classification"*:** —

    The default values depend on the specific pretrained classifier,
    see [`ReadDlModel`](read_dl_model.md).
    The network architectures allow changes of the image dimensions,
    which can be done using [`SetDlModelParam`](set_dl_model_param.md).
    But for networks with at least one fully connected layer such a
    change makes a retraining necessary.
    Networks without fully connected layers are directly applicable to
    different image sizes. However, images with a size differing from
    the size with which the classifier has been trained are likely to
    show a reduced classification accuracy.
  - **Models of *"type"*=*"detection"*, OD:** —

    The network architectures allow changes of the image dimensions.
    But the image lengths are halved for every level, that is why the
    dimensions *"image_width"* and *"image_height"*
    need to be an integer multiple of
    $2^{level}$.
    $level$ depends on the *"backbone"*
    and the parameter *"max_level"*, see
    [`CreateDlModelDetection`](create_dl_model_detection.md) for further information.

    Default:
     *"image_height"* = *640*,
    *"image_width"* = *640*
  - **Models of *"type"*=*"detection"*, AOD:** —

    The network architectures allow changes of the image dimensions.
    The dimensions *"image_width"* and *"image_height"*
    need to be an integer multiple of 32.
  - **Models of *"type"*=*"gc_anomaly_detection"*:** —

    The network architecture allows changes of the image dimensions.
    Note that these parameters have to be set before training the model.
    Setting them on an already trained model would render this model
    useless.

    Restriction:
     The *"image_width"* and the
    *"image_height"* must be
    greater than or equal to the value of the *"patch_size"*
    parameter.

    Default:
     *"image_height"* = *256*,
    *"image_width"* = *256*
  - **Models of *"type"*=*"ocr_recognition"*:** —

    The network architectures allow changes of the image width.

    The default and minimal values are given by the network, see
    [`ReadDlModel`](read_dl_model.md).
  - **Models of *"type"*=*"segmentation"*:** —

    The network architectures allow changes of the image dimensions.

    The default and minimal values are given by the network, see
    [`ReadDlModel`](read_dl_model.md).
- ***"image_num_channels"*: 3D-GPD 3D-PE AD CL MLC OCR-D OCR-R GC-AD AOD OD SE** —

  Number of channels of the input images the network will process.
  The default value is given by the network, see
  [`ReadDlModel`](read_dl_model.md) and [`CreateDlModelDetection`](create_dl_model_detection.md).

  For models of *"type"*=*"anomaly_detection"* or
  *"type"*=*"gc_anomaly_detection"*, only the
  values *1* and *3* are supported.
  In addition, this parameter should be set before the model is
  trained.
  For models of *"type"*=*"anomaly_detection"*,
  setting *"image_num_channels"* on an already
  trained model would render this model useless. Therefore,
  an error is returned when trying to do so, but the model
  itself is unchanged.

  For Deep OCR detection and recognition components, the number
  of channels can only be set to the respective default value
  (*3* for*"type"*=*"ocr_detection"*
  and *1* for *"type"*=*"ocr_recognition"*).

  For models of *"type"*=*"3d_gripping_point_detection"*
  and of *"type"*=*"3d_pose_estimation"* the parameter
  *"image_num_channels"* cannot be set.

  For other models, any number of input image channels is possible.

  If number of channels is changed to a value >1,
  the weights of the first layers after the input image layer will
  be initialized with random values.
  Note, in this case more data for the retraining is needed.
  If the number of channels is changed to 1,
  the weights of the concerned layers are fused.

  - **Models of *"type"*=*"anomaly_detection"*:** —

    Default:
     *"image_num_channels"* = *3*
  - **Models of *"type"*=*"detection"*:** —

    Default:
     *"image_num_channels"* = *3*
- ***"image_range_max"*,
  *"image_range_min"*: 3D-GPD AD CL MLC OCR-D OCR-R GC-AD AOD OD SE** —

  Maximum and minimum gray value of the input images, respectively,
  the network will process.

  The default values are given by the network, see
  [`ReadDlModel`](read_dl_model.md) and [`CreateDlModelDetection`](create_dl_model_detection.md).
- ***"image_size"*: 3D-GPD 3D-PE AD CL MLC OCR-D OCR-R GC-AD AOD OD SE** —

  Tuple containing the input image size *"image_width"*,
  *"image_height"*.

  The respective default values and possible value ranges depend on the
  model and model type.
  Please see the individual dimension parameter description for more
  details.
- ***"inference_outputs"*: Any** —

  This parameter returns a tuple of strings containing the names of the
  outputs of the model that are available during inference.
  Depending on the model, the tuple may contain one or multiple strings.
- ***"input_dimensions"*: Any except 3D-PE** —

  This parameter returns a dictionary containing all input dimensions
  of the network. Examples for such inputs: input image,
  `weight_image` (for models of
  *"type"*=*"segmentation"*).

  These dimensions are given in the dictionary as a tuple
  [`width`, `height`, `depth`].
  In case this parameter is used to set the dimension, for every dimension
  a value of -1 may be set to keep the current value.
- ***"instance_segmentation"*: OD** —

  This parameter determines if the model is created for instance
  segmentation.
  If the parameter is set to *"true"* in
  [`CreateDlModelDetection`](create_dl_model_detection.md), the detection deep learning network
  is extended by additional layers for instance segmentation.

  List of values:
   *"true"*, *"false"*

  Default:
   *"instance_segmentation"* = *"false"*
- ***"instance_type"*: AOD OD** —

  The parameter *"instance_type"* determines, which instance type
  is used for the object model. The current implementations differ
  regarding the allowed orientations of the bounding boxes.
  See the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for more
  explanations to the different types and their bounding boxes.

  List of values:
   *"rectangle1"*, *"rectangle2"*

  Default:
   *"instance_type"* = *"rectangle1"*
- ***"layer_names"*: Any except 3D-GPD AOD** —

  This parameter returns a tuple containing the name for every layer
  of the model.
  This name is the same human-readable identifier as is returned by
  `GetDlModelParam` with *"summary"*.

  Note, for some networks distributed with HALCON, the network
  architecture is confidential. In this case
  `GetDlModelParam` returns an empty tuple with
  *"layer_names"*.
- ***"learning_rate"*: Any** —

  Value of the factor determining the gradient influence during
  training using [`TrainDlModelBatch`](train_dl_model_batch.md).
  Please refer to [`TrainDlModelBatch`](train_dl_model_batch.md) for further details.

  The default values depend on the model. Note that changing
  *"solver_type"* sets *"learning_rate"*
  back to its default value.

  - **Models of *"type"*=*"anomaly_detection"*:** —

    The parameter *"learning_rate"* has no effect.
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"learning_rate"* has no effect.
- ***"mask_head_weight"*: OD** —

  The parameter *"mask_head_weight"* is a weighting factor for the
  calculation of the total loss.
  This means, when the losses of the individual network heads are summed up,
  the contribution from the mask prediction head is weighted
  by a factor *"mask_head_weight"*.

  Restriction:
   Only applicable to models with
  *"instance_segmentation"*=*"true"*

  Default:
   *"mask_head_weight"* = *1.0*
- ***"max_level"*, *"min_level"*: OD** —

  These parameters determine on which levels the additional networks are
  attached on the feature pyramid.
  We refer to the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for
  further explanations to the feature pyramid and the attached networks.

  From these (*"max_level"* - *"min_level"* + 1) networks
  all predictions with a minimum confidence value are kept as long they
  do not strongly overlap
  (see *"min_confidence"* and *"max_overlap"*).

  The level declares how often the size of the feature map already has
  been scaled down.
  Thus, level 0 corresponds to the feature maps with size of the input
  image, level 1 to feature maps subscaled once, and so on.
  As a consequence, smaller objects are detected in the lower levels,
  whereas larger objects are detected in higher levels.

  The value for *"min_level"* needs to be at least 2.

  If *"max_level"* is larger than the number of levels the
  backbone can provide, the backbone is extended with additional
  (randomly initialized) convolutional layers in order to generate
  deeper levels.
  Further, *"max_level"* may have an influence on the minimal
  input image size.

  Note, for small input image dimensions, high levels might not be
  meaningful, as the feature maps could already be too small to contain
  meaningful information.

  A higher number of used levels might increase the runtime and
  memory-consumption, whereby especially lower levels carry weight.

  Default:
   *"max_level"* = *6*,
  *"min_level"* = *2*
- ***"max_num_detections"*: AOD OD** —

  This parameter determines the maximum number of detections
  (bounding boxes) per image proposed from the network.

  Default:
   *"max_num_detections"* = *100*
- ***"max_num_gt"*: AOD** —

  This parameter defines the upper limit for the number of annotated
  object bounding boxes (ground-truth boxes) considered per image.
  It is only available for advanced object detection.
- ***"max_overlap"*: AOD OD** —

  The maximum allowed intersection over union (IoU) for two predicted
  bounding boxes of the same class.
  Or, vice-versa, when two bounding boxes are classified into the same
  class and have an IoU higher than *"max_overlap"*, the one
  with lower confidence value gets suppressed.
  We refer to the chapter [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) for
  further explanations to the IoU.

  Default:
   *"max_overlap"* = *0.5*
- ***"max_overlap_class_agnostic"*: AOD OD** —

  The maximum allowed intersection over union (IoU) for two predicted
  bounding boxes independently of their predicted classes.
  Or, vice-versa, when two bounding boxes have an IoU higher than
  *"max_overlap_class_agnostic"*, the one with lower confidence
  value gets suppressed.
  As default, *"max_overlap_class_agnostic"* is set to 1.0, hence
  class agnostic bounding box suppression has no influence.

  Default:
   *"max_overlap_class_agnostic"* = *1.0*
- ***"meta_data"*: Any** —

  Dictionary with user defined meta data, whose entries can be set
  freely. The meta data may be used to store information such as
  the model author or a model version along with the model.

  Restriction:
   Dictionary values are limited to strings.
- ***"min_character_score"*: OCR-D** —

  The parameter *"min_character_score"* specifies the lower
  threshold used for the character score map to estimate the dimensions of
  the characters.
  By adjusting the parameter, suggested instances can be split up or
  neighboring instances can be merged.

  Value range:
   $\in[\textit{0},\textit{1}]$.

  Default:
   *0.5*
- ***"min_confidence"*: MLC AOD OD** —
- **Models of *"type"*=*"detection"*:** —

  This parameter determines the minimum confidence, when the image part
  within the bounding box is classified in order to keep the proposed
  bounding box.
  This means, when [`ApplyDlModel`](apply_dl_model.md) is called, all output bounding
  boxes with a confidence value smaller than *"min_confidence"*
  are suppressed.
- **Models of *"type"*=*"multi_label_classification"*:** —

  This parameter determines the minimum confidence level required for a
  class to be considered as detected. This means, classes with a confidence
  score below *"min_confidence"* are regarded as not detected,
  while classes with a confidence value equal to or exceeding
  *"min_confidence"* are deemed as detected.

  Default:
   *"min_confidence"* = *0.5*
- ***"min_link_score"*: OCR-D** —

  The parameter *"min_link_score"* defines the minimum link
  score required between two localized characters to recognize these
  characters as coherent word.

  Value range:
   $\in[\textit{0},\textit{1}]$.

  Default:
   *0.3*
- ***"min_version"*: Any** —

  The parameter *"min_version"* defines the minimum required
  HALCON version to use this model.
- ***"min_word_area"*: OCR-D** —

  The parameter *"min_word_area"* defines the minimum size
  that a localized word must have in order to be suggested.
  This parameter can be used to filter suggestions that are too small.

  Value range:
   $\ge\textit{0}$.

  Default:
   *10*.
- ***"min_word_score"*: OCR-D** —

  The parameter *"min_word_score"* defines the minimum
  score a localized instance must contain to be suggested as valid word.
  With this parameter uncertain words can be filtered out.

  Value range:
   $\in[\textit{0},\textit{1}]$.

  Default:
   *0.7*
- ***"momentum"*: Any** —

  When updating the weights of the network,
  the hyperparameter *"momentum"* specifies to which extent
  previous updating vectors will be added to the current updating
  vector.
  Only applicable for *"solver_type"* = *"sgd"*.

  Please refer to [`TrainDlModelBatch`](train_dl_model_batch.md) for further details.

  The default value is given by the model.

  - **Models of *"type"*=*"anomaly_detection"*:** —

    The parameter *"momentum"* has no effect.
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"momentum"* has no effect.
- ***"num_classes"*: AOD OD SE** —

  Number of distinct classes that the model is able to distinguish
  for its predictions.

  This parameter differs between the model types:

  - **Models of *"type"*=*"detection"*, OD:** —

    This parameter is set as `numClasses` over
    [`CreateDlModelDetection`](create_dl_model_detection.md). *"class_ids"* and
    *"class_names"* always need to have *"num_classes"*
    entries.
  - **Models of *"type"*=*"detection"*, AOD:** —

    This is where the behavior differs from object detection models.
    This parameter can be set directly or indirectly through
    *"class_ids"* or *"class_names"*.
  - **Models of *"type"*=*"segmentation"*:** —

    A model of *"type"*=*"segmentation"* does predict
    background and therefore in this case the 'background' class is
    included in *"num_classes"*. For these models,
    *"num_classes"* is determined implicitly by the length of
    *"class_ids"*.
- ***"num_trainable_params"*: Any** —

  Number of trainable parameters (weights and biases) of the model.
  This value is an indicator for the size of the model when it is serialized.
- ***"ood_available"*: CL** —

  This parameter specifies whether a classification model has been extended for
  Out-of-Distribution Detection.
  If one of the operators [`FitDlOutOfDistribution`](fit_dl_out_of_distribution.md) or
  [`InitDlContinualLearning`](init_dl_continual_learning.md) has been called for
  the model, the value of *"ood_available"* is *"true"*.
  Otherwise it is *"false"*.

  Default:
   *"false"*
- ***"ood_threshold"*: CL** —

  A threshold that determines when a sample is classified as
  Out-of-Distribution.
  After calling [`FitDlOutOfDistribution`](fit_dl_out_of_distribution.md) or
  [`InitDlContinualLearning`](init_dl_continual_learning.md) for a classification
  model, [`ApplyDlModel`](apply_dl_model.md) additionally returns an
  *"ood_score"* and an
  *"ood_result"* in the output dictionaries. If the
  value of *"ood_score"* is greater than or equal to
  *"ood_threshold"*, the value of
  *"ood_result"* is *"true"*. Otherwise it is
  *"false"*.
  *"ood_threshold"* is only available after
  [`FitDlOutOfDistribution`](fit_dl_out_of_distribution.md) or
  [`InitDlContinualLearning`](init_dl_continual_learning.md) has been called. These operators
  calculate a value for *"ood_threshold"* based on the provided
  dataset. When calling the operator [`ExtendDlContinualLearning`](extend_dl_continual_learning.md),
  *"ood_threshold"* will be updated to take into account the added
  dataset.

  Value range:
   $\ge\textit{0}$.
- ***"orientation"*: OCR-D** —

  This parameter allows to set a predefined orientation angle for the word
  detection. To revert to default behavior using the internal orientation
  estimation, *"orientation"* is set to *"auto"*.

  Value range:
   $(-\pi,\pi]$.

  Default:
   *"auto"*
- ***"optimize_for_inference"*: 3D-GPD 3D-PE CL MLC OCR-D OCR-R GC-AD AOD OD SE Gen** —

  Defines whether the model is optimized and only applicable for inference.

  The model remains executable on HALCON standard devices even after
  optimization (unlike [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md)).

  Setting this parameter to *"true"* frees model memory not needed
  for inference (e.g., memory of gradients).
  This can significantly reduce the amount of memory needed by the model.
  As a consequence, models with this characteristic have no gradients
  accessible (needed e.g., for training or calculations of heatmaps).
  Operators using values from freed memory (e.g.,
  [`TrainDlModelBatch`](train_dl_model_batch.md)) will automatically reset this parameter
  value to *"false"*.

  In case the value is reset to *"false"* (both, manually or
  automatically), memory needed by the model for training is reallocated.
  This implies, a following training behaves as if *"momentum"* is
  temporarily set to *0*
  (as possible updating vectors have to be accumulated again).

  Default:
   *"false"*

  Restriction:
   For models of *"type"*=*"counting"* the
  parameter *"optimize_for_inference"* cannot be set to *"true"*.
- ***"patch_size"*: GC-AD** —

  This parameter determines the size of the patches analyzed by the
  *"local"* subnetwork.
  The patch size should be chosen such that patches containing defects
  will differ clearly from patches without defects. This should
  cover all kinds of anomalies that might occur during
  inference. The patch size does not need to cover the defects as a
  whole. Note that the image is not divided into separate patches, but
  *"patch_size"* solely determines the scale on which the image
  is gradually analyzed by the *"local"* subnetwork.
  If the image size is changed *"patch_size"* should be
  adjusted accordingly.

  |  |  |
  | --- | --- |
  | ![figure](../assets/e9fb5c0a0cae9d2b.svg) | ![figure](../assets/c171a170fcd76d36.svg) |
  | ( 1) | ( 2) |

  (1) Examples of patches with a suitable size (green).
  (2) The example patches (red) are either too large or too small to
  work for all possible defect classes that could occur in the
  images.

  Restriction:
   The parameter *"patch_size"* must be
  smaller than or equal to *"image_width"* and
  *"image_height"*.

  Default:
   *"patch_size"* = *33*
- ***"precision"*: Any** —

  Defines the data type that is internally used for the calculation
  of a forward pass of a deep learning model.

  Default:
   *"float32"*
- ***"precision_is_converted"*: Any** —

  Indicates whether the model was subjected to a conversion
  process after training done by [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md).

  Default:
   *"false"*
- ***"pretrained"*: Any** —

  This parameter initializes the model’s weights randomly when set to
  *"false"*.
  A value of *"true"* denotes the state when the weights
  have not yet been randomized. Once randomized, setting it back to
  *"true"* will raise an exception.

  Attention:
   Once the weights have been randomized, the original
  weights cannot be restored unless the model was previously saved and
  reloaded.
- ***"runtime"*: Any** —

  Defines the device on which the deep learning operators will be executed.

  Note that the parameter *"device"* should be preferred to set the
  devices on which the deep learning operators will be executed.

  Default:
   *"runtime"* = *"gpu"*

  - ***"cpu"*:** —

    The training and inference operator will be executed on CPU.
    Note, training is only supported for specific platform types,
    please see the HALCON `“Installation Guide”`.

    In case the GPU has been used before, CPU memory is
    initialized, and if necessary values stored on the
    GPU memory are moved to the CPU memory.

    For parallelization:
    The runtime is highly dependent on the number of threads set.
    The use of all available threads does not necessarily create
    a faster performance.
    How many threads are currently set can be queried with the operator
    [`GetSystem`](get_system.md).

    The implemented CPU parallelization is dependent on the architecture:

    - Intel or AMD architecture: OpenMP.
      By default all available threads of the OpenMP runtime environment
      are used.
      The number of threads used can be specified with the parameter
      *"tsp_thread_num"* of the operator [`SetSystem`](set_system.md).
    - Arm architectures: Global Thread Pool.
      The number of threads can be set with the global parameter
      *"thread_num"* of the operator [`SetSystem`](set_system.md).

    For both architectures mentioned above, it is not possible
    to specify a thread-specific number of threads (via the parameter
    *"tsp_thread_num"* of the operator [`SetSystem`](set_system.md)).
  - ***"gpu"*:** —

    The GPU memory is initialized.
    The operators [`ApplyDlModel`](apply_dl_model.md), [`TrainDlModelBatch`](train_dl_model_batch.md), and
    [`TrainDlModelAnomalyDataset`](train_dl_model_anomaly_dataset.md) will be executed on the GPU.
    For the specific requirements please refer to the HALCON
    `“Installation Guide”`.
- ***"solver_type"*: Any** —

  This value defines the optimization algorithm with the goal to
  minimize the value of the total loss function.
  For more information we refer to the documentation of
  [`TrainDlModelBatch`](train_dl_model_batch.md).
  The following values can be set:

  - *"adam"*: Adaptive moment estimation
  - *"sgd"*: Stochastic gradient descent

  Note that changing *"solver_type"* sets *"learning_rate"*
  back to its default value.

  - **Models of *"type"*=*"anomaly_detection"*:** —

    The parameter *"solver_type"* has no effect.
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"solver_type"* has no effect.
- ***"sort_by_line"*: OCR-D** —

  The words are sorted line-wise based on the orientation of the localized
  word instances. If the parameter *"sort_by_line"* is
  set to *"false"*, the results will not be sorted.

  Default:
   *"true"*
- ***"standard_deviation_factor"*: AD** —

  The anomaly score is calculated internally as the mean of certain
  internal scores s plus lambda times their standard deviation.

  $$S_{Image}=\mu(s)+\lambda\sigma(s)$$

  Where *s* denotes a pixel value of the internal
  `anomaly_image`,
  $\mu(s)$ the mean value of *s* and
  $\sigma(s)$ the standard deviation of *s*.
  The parameter *"standard_deviation_factor"* sets the value
  $\lambda$ and thus controls how important the standard
  deviation is in comparison to the mean.

  Default:
   *"standard_deviation_factor"* = *3.0*
- ***"summary"*: Any** —

  This parameter returns information on the layers of the model.
  More precisely, it returns a tuple with a string for every layer.
  The string is as follows:
  `ID; NAME; TYPE; OUTPUT_SHAPE; CONNECTED_NODES`

  - `ID`: Index of the layer in the CNN graph.
  - `NAME`: Human-readable identifier (optional).
  - `TYPE`: Human-readable identifier
    representing the type of the layer (e.g., `input` or
    `convolution`).
  - `OUTPUT_SHAPE`: Size of the output, given in the form
    (`Width`, `Height`, `Depth`,
    *"batch_size"*).
    This means, the layer has feature maps of size `Width` times
    `Height` and therefrom `Depth` many.
    Together they form an iconic object with a channel for every
    feature map.
    The parameter *"batch_size"* determines, how many objects
    are returned together.
  - `CONNECTED_NODES`: Comma separated list with IDs
    of the layers using the output of the current layer as input

  E.g., `'3; conv1; convolution; (112, 112, 64, 160); 4'`.

  Note, for some networks distributed with HALCON, the network
  architecture is confidential. In this case
  `GetDlModelParam` returns an empty tuple with *"summary"*.
- ***"tiling"*: OCR-D SE** —

  The input image is automatically split into overlapping tile images of
  size *"image_size"*, which are processed separately by
  the model. This allows processing images that are much
  larger than the actual *"image_size"* without having to
  zoom the input image. Note that for best results, the model should be
  pretrained on tiled images.

  Default:
   *"false"*
- ***"tiling_overlap"*: OCR-D SE** —

  This parameter defines how much neighboring tiles overlap when input
  images are split (see *"tiling"*). The overlap
  is given in pixels.

  Value range:
   $\ge\textit{0}$.

  Default:
   *64*
- ***"type"*: Any** —

  This parameter returns the HALCON-specific model type.
  The following types are distinguished:

  - *"3d_gripping_point_detection"*
  - *"3d_pose_estimation"*
  - *"anomaly_detection"*
  - *"classification"*
  - *"counting"*
  - *"detection"*
  - *"gc_anomaly_detection"*
  - *"segmentation"*
  - *"ocr_recognition"*
  - *"ocr_detection"*
  - *"generic"* - for certain read in models or models created
    with the DL framework, see [`SetDlModelParam`](set_dl_model_param.md).
- ***"weight_decay"*: Any** —

  Regularization parameter $\alpha\ge0.0$ used to control
  the decay of the model's weights.
  Weight decay works by directly shrinking the magnitude of the weights by a
  small factor in each iteration of the training.
  For a detailed description of the weight decay mechanism, we refer to
  [`TrainDlModelBatch`](train_dl_model_batch.md).

  In contrast to the parameter *"weight_prior"*, this parameter leads
  to a weight decay that is decoupled from the gradient-based update.
  When the SGD solver is used, this parameter has the same effect as
  *"weight_prior"*.
  When the Adam solver is used with *"weight_decay"*, this is
  commonly referred to as AdamW.

  For typical applications, we recommend testing values for *"weight_decay"*
  between $0.1,...,0.01$.

  - **Models of *"type"*=*"anomaly_detection"*:** —

    The parameter *"weight_decay"* has no effect.
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"weight_decay"* has no effect.

  Default:
   *"weight_decay"* = *0.0*
- ***"weight_prior"*: Any** —

  Regularization parameter $\alpha\ge0.0$ used to control
  the L2 regularization of the model's weights.
  L2 regularization works by adding an extra term to the loss function, which
  penalizes the squared magnitude of the weights.
  For a detailed description of the regularization term, we refer to
  [`TrainDlModelBatch`](train_dl_model_batch.md).

  Simply put: Regularization favors simpler models that are less likely
  to learn noise in the data and generalize better.
  In case the classifier overfits the data, it is strongly
  recommended to try different values for the parameter
  *"weight_prior"* to improve the generalization properties of
  the neural network. Choosing its value is a trade-off between the
  model's ability to generalize, overfitting, and underfitting.
  If $\alpha$ is too small, the model might overfit, if its too
  large the model might loose its ability to fit the data, because all
  weights are pushed too close to zero. For finding an ideal value for
  $\alpha$, we recommend a cross-validation, i.e. to perform the
  training for a range of values and choose the value that results in
  the best validation error.

  For typical applications, we recommend
  testing the values for *"weight_prior"* on a logarithmic scale
  between $1.0,...,0.0001$. If the training
  takes a very long time, one might consider performing the
  hyperparameter optimization on a reduced amount of data.

  - **Models of *"type"*=*"anomaly_detection"*:** —

    The parameter *"weight_prior"* has no effect.
  - **Models of *"type"*=*"counting"*:** —

    The parameter *"weight_prior"* has no effect.

  Default:
   *"weight_prior"* = *0.0*,
  with exception of the pretrained classifiers

  - `pretrained_dl_classifier_resnet18`:
    *"weight_prior"* = *0.0001*
  - `pretrained_dl_classifier_resnet50`:
    *"weight_prior"* = *0.0001*
  - `pretrained_dl_classifier_alexnet`:
    *"weight_prior"* = *0.0005*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
"batch_size"

List of values:
"adam_beta1", "adam_beta2", "adam_epsilon", "alignment", "alignment_available", "alphabet", "alphabet_internal", "alphabet_mapping", "anchor_angles", "anchor_aspect_ratios", "anchor_num_subscales", "anomaly_score_tolerance", "backbone", "backbone_docking_layers", "batch_size", "batch_size_multiplier", "bbox_heads_weight", "capacity", "class_heads_weight", "class_ids", "class_ids_no_orientation", "class_names", "class_weights", "complexity", "continual_learning_available", "device", "extract_feature_maps", "freeze_backbone_level", "gc_anomaly_networks", "gpu", "ignore_class_ids", "ignore_direction", "image_dimensions", "image_height", "image_num_channels", "image_range_max", "image_range_min", "image_size", "image_width", "inference_outputs", "input_dimensions", "instance_segmentation", "instance_type", "layer_names", "learning_rate", "mask_head_weight", "max_gradient_norm", "max_level", "max_num_detections", "max_num_gt", "max_overlap", "max_overlap_class_agnostic", "meta_data", "min_character_score", "min_confidence", "min_level", "min_link_score", "min_version", "min_word_area", "min_word_score", "model_uid", "momentum", "num_classes", "num_trainable_params", "ood_available", "ood_threshold", "optimize_for_inference", "orientation", "patch_size", "precision", "precision_is_converted", "pretrained", "release_version", "runtime", "solver_type", "sort_by_line", "standard_deviation_factor", "summary", "tiling", "tiling_overlap", "type", "weight_decay", "weight_prior"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*int* / long / string / double)

Value of the generic parameter.

## Result

If the parameters are valid, the operator `GetDlModelParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`ReadDlModel`,
`SetDlModelParam`

## Possible Successors

`SetDlModelParam`,
`ApplyDlModel`,
`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`

## See also

`SetDlModelParam`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
