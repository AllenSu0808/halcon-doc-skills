# create_deep_matching_3d (Operator)

## Name

`create_deep_matching_3d` — Create a Deep 3D Matching model.

## Signature

`def create_deep_matching_3d(object_model_3d: HHandle, symmetry: Union[HHandle, str], gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[str, float, int]]) -> HHandle`

## Description

`create_deep_matching_3d` creates a Deep 3D Matching model for
finding the poses of the 3D object model *`object_model_3d`* and returns
its handle in *`deep_3dmatching_model`*.

If the 3D object model is symmetric, symmetry information has to be set with the
parameter *`symmetry`*. It defines the symmetries of the 3D object model
*`object_model_3d`* in a dictionary. Currently discrete symmetries are supported
and set in the dictionary key *"symmetry_poses"* with the value consisting
of HALCON poses (see [`create_pose`](create_pose.md)). All poses that keep the model
identical under transformation have to be set, including the identity. By default,
this parameter is set to *"no_symmetry"* (as a string instead of a dictionary)
which means that no symmetry is active.

Internally `create_deep_matching_3d` reads pretrained backbone models and
creates the model components for object detection and 3D pose estimation.
The backbone for
3D pose estimation is filled with the 3D object model *`object_model_3d`*
and possibly its symmetry information for training.

The behavior of the operator can be influenced by setting *`gen_param_name`*
to the value passed in *`gen_param_value`*:

- ***"backbone_name_detector"*:** —

  Sets the backbone of the deep learning model for object detection.
  A list of possible backbones can be found in the documentation of
  [`create_dl_model_detection`](create_dl_model_detection.md).

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
    [`get_dl_model_param`](get_dl_model_param.md) and listed below:

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
    [`get_dl_model_param`](get_dl_model_param.md) and listed below:

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
  can be found in the documentation of [`create_dl_model_detection`](create_dl_model_detection.md).

The deep learning models used for Deep 3D Matching can be obtained by
[`get_deep_matching_3d_param`](get_deep_matching_3d_param.md) and trained using [`train_dl_model_batch`](train_dl_model_batch.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

3D model to search.

**`symmetry`** (input_control)  attribute.value `→` Union[HHandle, str]

Symmetries of the 3D model.

Default:
"no_symmetry"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of parameters.

Default:
[]

Suggested values:
"backbone_name_detector", "backbone_name_pose_estimation"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, float, int]]

Values of parameters.

Default:
[]

Suggested values:
"pretrained_dl_classifier_compact.hdl", "pretrained_dl_3d_pose_estimation_compact.hdl", "pretrained_dl_3d_pose_estimation_enhanced.hdl"

**`deep_3dmatching_model`** (output_control)  deep_matching_3d `→` HHandle

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
