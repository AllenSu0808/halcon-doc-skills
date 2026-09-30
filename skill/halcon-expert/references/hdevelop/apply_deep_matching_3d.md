# apply_deep_matching_3d (Operator)

## Name

`apply_deep_matching_3d` — Find the pose of objects using Deep 3D Matching.

## Signature

`apply_deep_matching_3d(Images : : Deep3DMatchingModel, GenParamName, GenParamValue : DeepMatchingResults)`

## Description

The operator `apply_deep_matching_3d` finds instances of the object
defined in *`Deep3DMatchingModel`* in the images *`Images`*
and returns the detected instances and their 3D poses in
*`DeepMatchingResults`*.

### Input Images

*`Images`* must be an image array with exactly as many images as
there are cameras set in the Deep 3D Matching model (see
[`set_deep_matching_3d_param`](set_deep_matching_3d_param.md)).
The image resolutions must match the resolution of the
corresponding camera parameters.
The images must be of type *'byte'*,
and they must have 1 or 3 channels.

### Parameters

Parameters specific to the Deep 3D Matching model can be set
using [`set_deep_matching_3d_param`](set_deep_matching_3d_param.md) before calling this operator.
Additional parameters that are only relevant for this call to
`apply_deep_matching_3d` can be set using the generic parameters
*`GenParamName`* and *`GenParamValue`*.
Note that currently no such parameters are supported.
*`GenParamName`* and *`GenParamValue`* should thus be
set to the empty tuple *'[]'*.

### Deep Learning Models

`apply_deep_matching_3d` uses deep learning technology for
detecting the object instances.
For an efficient execution, it is strongly recommended to use
appropriate hardware accelerators and to optimize the deep
learning models.
See [`get_deep_matching_3d_param`](get_deep_matching_3d_param.md) on how to obtain the
deep learning models in order to set the device on which they are
executed and [`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md) for
optimizing the models for a particular hardware.

### Detection Steps

- **1. Object Detection** —

  The object detection deep learning model is used to find instances
  of the target object in all images.
- **2. 3D pose estimation** —

  The pose estimation deep learning model is used to estimate the
  3D pose of all instances found in the previous step.
  Poses of the same object found in different images are combined
  into a single instance.
- **3. Pose Refinement** —

  The poses found in the previous step are further refined using
  edges visible in the image. Additionally, their score is
  computed.
- **4. Filter Results** —

  The detected instances are filtered using the minimum score
  (*'min_score'*), the minimum number of cameras in which
  instances must be visible (*'min_num_views'*),
  as well es the maximum number of instances to return
  (*'num_matches'*).
  In case of duplicates, the instance with the higher score is
  kept, or (if *'sort_single_views_last'* is set
  to *'true'*) the instance seen from more than one camera.

### Result Format

The results are returned in *`DeepMatchingResults`* as a dictionary.
The dictionary key *'results'* contains all detected results.
Each result has the following keys:

- ***'score'*:** —

  The score of the result instance.
- ***'pose'*:** —

  The pose of the result instance in world coordinate systems.
- ***'cameras'*:** —

  A tuple of integers containing the camera indices in which the
  instance was detected in.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Images`** (input_object)  (multichannel-)image(-array) `→` object (byte / real)

Input images.

**`Deep3DMatchingModel`** (input_control)  deep_matching_3d `→`  (handle)

Deep 3D Matching model.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Name of parameters.

Default:
[]

Suggested values:

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer / handle)

Value of parameters.

Default:
[]

Suggested values:

**`DeepMatchingResults`** (output_control)  dict `→`  (handle)

Results.

## Module

3D Metrology
