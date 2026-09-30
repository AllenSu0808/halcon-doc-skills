# set_dl_model_param (Operator)

## Name

`set_dl_model_param` — Set the parameters of a deep learning model.

## Signature

`set_dl_model_param( : : DLModelHandle, GenParamName, GenParamValue : )`

## Description

`set_dl_model_param` sets the parameters and hyperparameters
*`GenParamName`* of the deep learning model *`DLModelHandle`*
to the values *`GenParamValue`*.

The values *`GenParamName`* can attain, depend on the model type:
There are parameters which can be set for any deep learning model while
others can only be set for specific model types.
A description of the parameters whose value you can only set but not
retrieve is given below. For all other parameters the specific description
is given in [`get_dl_model_param`](get_dl_model_param.md).
In [`get_dl_model_param`](get_dl_model_param.md) we also give an overview,
for which type of model and using which operator a parameter can be set.

In the following we list the parameters *`GenParamName`* you can set
using this operator, `set_dl_model_param`.
Thereby, the following symbols denote the model type for which the parameter
can be set and has a possible influence:

- 'Any': any method
- '3D-GPD': *'type'*=*'3d_gripping_point_detection'*
- '3D-PE': *'type'*=*'3d_pose_estimation'*
- 'AD': *'type'*=*'anomaly_detection'*
- 'AOD': *'type'*=*'detection'*. Advanced Object Detection
- 'CL': *'type'*=*'classification'*
- 'MLC': *'type'*=*'multi_label_classification'*
- 'DC': *'type'*=*'counting'*
- 'OCR-D': *'type'*=*'ocr_detection'*
- 'OCR-R': *'type'*=*'ocr_recognition'*
- 'GC-AD': *'type'*=*'gc_anomaly_detection'*
- 'OD': *'type'*=*'detection'*
- 'SE': *'type'*=*'segmentation'*
- 'Gen': *'type'*=*'generic'*

- ***'adam_beta1'*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

  Moment for linear term in Adam solver. Only applicable if
  *'solver_type'* = *'adam'*.
- ***'adam_beta2'*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

  Moment for quadratic term in Adam solver. Only applicable if
  *'solver_type'* = *'adam'*.
- ***'adam_epsilon'*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

  Epsilon for numeric stability in Adam solver. Only applicable if
  *'solver_type'* = *'adam'*.
- ***'alignment'*: OCR-R** —
- ***'alphabet'*: OCR-R** —
- ***'alphabet_internal'*: OCR-R** —
- ***'alphabet_mapping'*: OCR-R** —
- ***'anomaly_score_tolerance'*: GC-AD** —
- ***'backbone_docking_layers'*: CL** —

  The docking layers can be specified for every classifier, also without
  using them as backbone.
  The specification is only considered for object detection backbones.
- ***'batch_size'*: Any** —
- ***'batch_size_multiplier'*: 3D-GPD 3D-PE CL MLC OCR-D OCR-R GC-AD OD SE Gen** —
- ***'batchnorm_momentum'*: Any except DC** —

  Calling this option sets the momentum of all batch normalization layers
  within the network. The settable values are the same as described in
  [`create_dl_layer_batch_normalization`](create_dl_layer_batch_normalization.md) for the parameter
  `Momentum`.

  Note, if the network has no such layer, nothing is done and therewith
  the operation is regarded as successful.
- ***'bbox_heads_weight'*, *'class_heads_weight'*: AOD OD** —
- ***'class_ids'*: 3D-GPD MLC AOD OD SE** —
- ***'class_names'*: CL MLC AOD OD SE** —
- ***'class_weights'*: CL** —
- ***'complexity'*: AD** —
- ***'device'*: Any** —
- ***'enable_resizing'*: Any except DC AOD** —

  Calling this option converts certain pooling layers within the
  network. More precisely, every non-global pooling layer with a
  resulting feature map of size 1x1 is converted into a global pooling
  layer. This means, a pooling layer performing e.g., average pooling is
  converted into one performing global average pooling.
  For more information about pooling layer and possible modes of operation,
  see the `“Solution Guide on Classification”`.

  Note, if this operation is performed, it can not be undone.
  Accordingly, you can only call it with the value *'true'*.
  Also, if the network has no such layer, nothing is done and therewith
  the operation is regarded as successful.
- ***'extract_feature_maps'*: CL** —
- ***'freeze_backbone_level'*: OD** —
- ***'fuse_bn_relu'*: Any except DC** —

  Calling this option fuses layer pairs consisting of a batch normalization
  layer without activation and a directly connected activation layer
  with ReLU activation.
  To do so, the output of the batch normalization layer must be used exclusively
  as input for the activation layer.
  As a result, a batch normalization layer with activation mode ReLU is obtained.
  For more information about layers and possible modes of operation,
  see the `“Solution Guide on Classification”`.

  Please note that if this operation is performed, it cannot be undone.
  Accordingly, it can only be called with the value *'true'*.
  Also, if the network contains no such fusible layers, no changes are made
  and the operation is still considered successful.

  Restriction:
   Leaky ReLU layers cannot be fused with
  batch normalization layers.
- ***'fuse_conv_bn'*: Any except DC** —

  Calling this option fuses layer pairs consisting of a convolution
  layer without activation and a directly connected batch normalization layer.
  To do so, the output of the convolution layer must be used exclusively
  as input for the batch normalization layer.
  As a result, a single convolution layer is obtained that produces
  the same output as the original layer pair.
  This fusion can improve the runtime performance and memory consumption
  of the network during inference.
  For more information about layers and possible modes of operation,
  see the `“Solution Guide on Classification”`.

  Please note that if this operation is performed, it cannot be undone.
  Accordingly, it can only be called with the value *'true'*.
  Also, if the network contains no such fusible layers, no changes are made
  and the operation is still considered successful.
- ***'fuse_conv_relu'*: Any except DC** —

  Calling this option fuses layer pairs consisting of a convolution
  layer without activation and a directly connected activation layer
  with ReLU activation.
  To do so, the output of the convolution layer must be used exclusively
  as input for the activation layer.
  As a result, a convolution layer with activation mode ReLU is obtained.
  For more information about layers and possible modes of operation,
  see the `“Solution Guide on Classification”`.

  Please note that if this operation is performed, it cannot be undone.
  Accordingly, it can only be called with the value *'true'*.
  Also, if the network contains no such fusible layers, no changes are made
  and the operation is still considered successful.

  Restriction:
   Leaky ReLU layers cannot be fused with
  convolution layers.
- ***'gc_anomaly_networks'*: GC-AD** —
- ***'gpu'*: Any** —
- ***'ignore_class_ids'*: SE** —
- ***'image_dimensions'*: 3D-GPD AD CL MLC OCR-D OCR-R GC-AD SE AOD** —
- ***'image_height'*, *'image_width'*: 3D-GPD AD CL MLC OCR-D OCR-R GC-AD SE AOD** —
- ***'image_num_channels'*: AD CL MLC OCR-D OCR-R GC-AD SE AOD** —
- ***'image_range_max'*, *'image_range_min'*: 3D-GPD OCR-D OCR-R SE AOD** —
- ***'image_size'*: 3D-GPD AD CL MLC OCR-D OCR-R GC-AD SE AOD** —
- ***'input_dimensions'*: AD CL MLC OCR-D OCR-R SE AOD Gen** —
- ***'learning_rate'*: 3D-GPD 3D-PE CL MLC OCR-D OCR-R GC-AD AOD OD SE Gen** —
- ***'mask_head_weight'*: OD** —

  This parameter is only available for models with
  *'instance_segmentation'*=*'true'*.
- ***'max_gradient_norm'*: Any** —
- ***'max_num_detections'*: AOD OD** —
- ***'max_num_gt'*: AOD** —
- ***'max_overlap'*: AOD OD** —
- ***'max_overlap_class_agnostic'*: AOD OD** —
- ***'meta_data'*: Any** —
- ***'min_character_score'*: OCR-D** —
- ***'min_confidence'*: MLC AOD OD** —
- ***'min_link_score'*: OCR-D** —
- ***'min_word_area'*: OCR-D** —
- ***'min_word_score'*: OCR-D** —
- ***'momentum'*: 3D-GPD 3D-PE CL MLC OCR-D OCR-R GC-AD AOD OD SE Gen** —

  Momentum for SGD solver.

  Restriction:
   Only applicable for *'solver_type'* =
  *'sgd'*.
- ***'ood_threshold'*: CL** —
- ***'optimize_for_inference'*: 3D-GPD 3D-PE CL MLC OCR-D OCR-R GC-AD AOD OD SE Gen** —
- ***'orientation'*: OCR-D** —
- ***'patch_size'*: GC-AD** —
- ***'pretrained'*: Any** —
- ***'runtime'*: Any** —
- ***'runtime_init'*: Any except DC** —

  If called with *'immediately'*, the GPU memory is initialized
  and the corresponding handle created. Otherwise this is done on
  demand, which may result in significantly larger execution times for
  the first call of [`apply_dl_model`](apply_dl_model.md) or
  [`train_dl_model_batch`](train_dl_model_batch.md).

  If the network architecture is changed subsequently, the GPU memory
  is reinitialized.
  This can happen e.g., for changes of *'batch_size'*,
  *'image_dimensions'* or *'input_dimensions'* with
  subsequent calls of `set_dl_model_param`.

  Note, this parameter has no effect if:

  - Running on CPUs, thus if *'runtime'* is set to *'cpu'*.
  - Running with an AI
    2-interface.
  - The device has been set before using *'device'*.
- ***'solver_type'*: 3D-GPD 3D-PE CL MLC OCR-D OCR-R GC-AD AOD OD SE Gen** —
- ***'sort_by_line'*: OCR-D** —
- ***'standard_deviation_factor'*: AD** —
- ***'tiling'*: OCR-D SE** —
- ***'tiling_overlap'*: OCR-D SE** —
- ***'type'*: Gen** —

  This parameter returns the HALCON-specific model type.

  Models of *'generic'* fulfill all model functions. But several
  deep learning procedures rely a specific *'type'*.
  The value of *'type'* can be set from *'generic'* to the
  following values:

  - *'classification'*
  - *'segmentation'*
  - *'detection'*

  Setting a value for *'type'*, it is checked if the model has all
  layers necessary for inference and training. In case of
  *'detection'*, the model must have a BoxProposals-layer. The
  resulting model is an object detection model, not advanced object detection.
  For other values for *'type'* missing necessary layers are added,
  if possible.
- ***'weight_decay'*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —
- ***'weight_prior'*: 3D-GPD 3D-PE CL OCR-D OCR-R GC-AD AOD OD SE Gen** —

## Attention

System requirements:
To successfully set *'gpu'* parameters, cuDNN and cuBLAS are
required, i.e., to set the parameter *`GenParamName`*
*'runtime'* to *'gpu'*.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Handle of the deep learning model.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter.

Default:
'batch_size'

List of values:
'adam_beta1', 'adam_beta2', 'adam_epsilon', 'alignment', 'alphabet', 'alphabet_internal', 'alphabet_mapping', 'anchor_angles', 'anchor_aspect_ratios', 'anchor_num_subscales', 'anomaly_score_tolerance', 'backbone', 'backbone_docking_layers', 'batch_size', 'batch_size_multiplier', 'batchnorm_momentum', 'bbox_heads_weight', 'capacity', 'class_heads_weight', 'class_ids', 'class_names', 'class_weights', 'complexity', 'device', 'enable_resizing', 'extract_feature_maps', 'freeze_backbone_level', 'fuse_bn_relu', 'fuse_conv_bn', 'fuse_conv_relu', 'gc_anomaly_networks', 'gpu', 'ignore_class_ids', 'ignore_direction', 'image_dimensions', 'image_height', 'image_num_channels', 'image_range_max', 'image_range_min', 'image_size', 'image_width', 'input_dimensions', 'instance_type', 'learning_rate', 'mask_head_weight', 'max_gradient_norm', 'max_level', 'max_num_detections', 'max_num_gt', 'max_overlap', 'max_overlap_class_agnostic', 'meta_data', 'min_character_score', 'min_confidence', 'min_level', 'min_link_score', 'min_word_area', 'min_word_score', 'momentum', 'num_classes', 'ood_threshold', 'optimize_for_inference', 'orientation', 'patch_size', 'pretrained', 'runtime', 'runtime_init', 'solver_type', 'sort_by_line', 'standard_deviation_factor', 'summary', 'tiling', 'tiling_overlap', 'type', 'weight_decay', 'weight_prior'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (integer / string / real)

Value of the generic parameter.

Default:
1

Suggested values:
1, 2, 3, 50, [80,60], 80, 60, 0.001, -127, 128, 'adam', 'cpu', 'gpu', 'immediately', 'sgd'

## Result

If the parameters are valid, the operator
`set_dl_model_param` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_dl_model`,
`get_dl_model_param`

## Possible Successors

`get_dl_model_param`,
`apply_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`

## See also

`get_dl_model_param`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
