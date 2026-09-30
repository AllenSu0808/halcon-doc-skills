# CreateDeepMatching3d (Operator)

## Name

`CreateDeepMatching3d` — Create a Deep 3D Matching model.

## Signature

`static void HOperatorSet.CreateDeepMatching3d(HTuple objectModel3D, HTuple symmetry, HTuple genParamName, HTuple genParamValue, out HTuple deep3DMatchingModel)`

`public HDeepMatching3D(HObjectModel3D objectModel3D, HTuple symmetry, HTuple genParamName, HTuple genParamValue)`

`public HDeepMatching3D(HObjectModel3D objectModel3D, string symmetry, string genParamName, string genParamValue)`

`void HDeepMatching3D.CreateDeepMatching3d(HObjectModel3D objectModel3D, HTuple symmetry, HTuple genParamName, HTuple genParamValue)`

`void HDeepMatching3D.CreateDeepMatching3d(HObjectModel3D objectModel3D, string symmetry, string genParamName, string genParamValue)`

## Description

`CreateDeepMatching3d` creates a Deep 3D Matching model for
finding the poses of the 3D object model *`objectModel3D`* and returns
its handle in *`deep3DMatchingModel`*.

If the 3D object model is symmetric, symmetry information has to be set with the
parameter *`symmetry`*. It defines the symmetries of the 3D object model
*`objectModel3D`* in a dictionary. Currently discrete symmetries are supported
and set in the dictionary key *"symmetry_poses"* with the value consisting
of HALCON poses (see [`CreatePose`](create_pose.md)). All poses that keep the model
identical under transformation have to be set, including the identity. By default,
this parameter is set to *"no_symmetry"* (as a string instead of a dictionary)
which means that no symmetry is active.

Internally `CreateDeepMatching3d` reads pretrained backbone models and
creates the model components for object detection and 3D pose estimation.
The backbone for
3D pose estimation is filled with the 3D object model *`objectModel3D`*
and possibly its symmetry information for training.

The behavior of the operator can be influenced by setting *`genParamName`*
to the value passed in *`genParamValue`*:

- ***"backbone_name_detector"*:** —

  Sets the backbone of the deep learning model for object detection.
  A list of possible backbones can be found in the documentation of
  [`CreateDlModelDetection`](create_dl_model_detection.md).

  Default:
   *"pretrained_dl_classifier_compact.hdl"*.
- ***"backbone_name_pose_estimation"*:** —

  Sets the backbone of the deep learning model for 3D pose estimation.

  HALCON provides pretrained backbones to be used for Deep 3D Matching.
  The following pretrained neural networks are provided:

  - ***"pretrained_dl_3d_pose_estimation_compact.hdl"*:** —

    This is a smaller neural network designed for easier tasks and is
    more memory and runtime efficient.

    This network expects the images to be of the type `byte`.
    Additionally, the network is designed for certain image properties.
    The corresponding values can be retrieved with
    [`GetDlModelParam`](get_dl_model_param.md) and listed below:

    - —

      *"image_width"*: 256
    - —

      *"image_height"*: 256
    - —

      *"image_num_channels"*: 3

    Restriction:
     The network architecture does not allow changes concerning the image dimensions.
  - ***"pretrained_dl_3d_pose_estimation_enhanced.hdl"*:** —

    This is a larger neural network designed for more difficult tasks and requires
    more memory and runtime.

    This network expects the images to be of the type `byte`.
    Additionally, the network is designed for certain image properties.
    The corresponding values can be retrieved with
    [`GetDlModelParam`](get_dl_model_param.md) and listed below:

    - —

      *"image_width"*: 256
    - —

      *"image_height"*: 256
    - —

      *"image_num_channels"*: 3

    Restriction:
     The network architecture does not allow changes concerning the image dimensions.

  List of values:
   *"pretrained_dl_3d_pose_estimation_compact.hdl"*,
  *"pretrained_dl_3d_pose_estimation_enhanced.hdl"*.

  Default:
   *"pretrained_dl_3d_pose_estimation_enhanced.hdl"*.
- ***"detector_params"*:** —

  Dictionary with parameters used to configure the backbone of the deep
  learning model for object detection. A list with the settable parameters
  can be found in the documentation of [`CreateDlModelDetection`](create_dl_model_detection.md).

The deep learning models used for Deep 3D Matching can be obtained by
[`GetDeepMatching3dParam`](get_deep_matching_3d_param.md) and trained using [`TrainDlModelBatch`](train_dl_model_batch.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

3D model to search.

**`symmetry`** (input_control)  attribute.value `→` [HTuple](HTuple.md) (*string* / HHandle)

Symmetries of the 3D model.

Default:
"no_symmetry"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of parameters.

Default:
[]

Suggested values:
"backbone_name_detector", "backbone_name_pose_estimation"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of parameters.

Default:
[]

Suggested values:
"pretrained_dl_classifier_compact.hdl", "pretrained_dl_3d_pose_estimation_compact.hdl", "pretrained_dl_3d_pose_estimation_enhanced.hdl"

**`deep3DMatchingModel`** (output_control)  deep_matching_3d `→` [HDeepMatching3D](HDeepMatching3D.md), [HTuple](HTuple.md) (*IntPtr*)

Deep 3D Matching model.

## Example (HDevelop)

```
* The following example demonstrates the setting of a discrete symmetry.
read_object_model_3d ('pipe_joint', 'm', [], [], ObjectModel3D, Status)
create_pose (0, 0, 0, 0, 0, 0, 'Rp+T', 'gba', 'point', OriginPose)
create_pose (0, 0, 0, 0, 0, 180, 'Rp+T', 'gba', 'point', SymmetryPose)
Symmetry := dict{symmetry_poses: [OriginPose, SymmetryPose]}
create_deep_matching_3d (ObjectModel3D, Symmetry, [], [], Deep3DMatchingModel)
```

## Module

3D Metrology
