# ApplyDeepMatching3d (Operator)

## Name

`ApplyDeepMatching3d` — Find the pose of objects using Deep 3D Matching.

## Signature

`static void HOperatorSet.ApplyDeepMatching3d(HObject images, HTuple deep3DMatchingModel, HTuple genParamName, HTuple genParamValue, out HTuple deepMatchingResults)`

`HDict HDeepMatching3D.ApplyDeepMatching3d(HImage images, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `ApplyDeepMatching3d` finds instances of the object
defined in *`deep3DMatchingModel`* in the images *`images`*
and returns the detected instances and their 3D poses in
*`deepMatchingResults`*.

### Input Images

*`images`* must be an image array with exactly as many images as
there are cameras set in the Deep 3D Matching model (see
[`SetDeepMatching3dParam`](set_deep_matching_3d_param.md)).
The image resolutions must match the resolution of the
corresponding camera parameters.
The images must be of type *"byte"*,
and they must have 1 or 3 channels.

### Parameters

Parameters specific to the Deep 3D Matching model can be set
using [`SetDeepMatching3dParam`](set_deep_matching_3d_param.md) before calling this operator.
Additional parameters that are only relevant for this call to
`ApplyDeepMatching3d` can be set using the generic parameters
*`genParamName`* and *`genParamValue`*.
Note that currently no such parameters are supported.
*`genParamName`* and *`genParamValue`* should thus be
set to the empty tuple *"[]"*.

### Deep Learning Models

`ApplyDeepMatching3d` uses deep learning technology for
detecting the object instances.
For an efficient execution, it is strongly recommended to use
appropriate hardware accelerators and to optimize the deep
learning models.
See [`GetDeepMatching3dParam`](get_deep_matching_3d_param.md) on how to obtain the
deep learning models in order to set the device on which they are
executed and [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md) for
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
  (*"min_score"*), the minimum number of cameras in which
  instances must be visible (*"min_num_views"*),
  as well es the maximum number of instances to return
  (*"num_matches"*).
  In case of duplicates, the instance with the higher score is
  kept, or (if *"sort_single_views_last"* is set
  to *"true"*) the instance seen from more than one camera.

### Result Format

The results are returned in *`deepMatchingResults`* as a dictionary.
The dictionary key *"results"* contains all detected results.
Each result has the following keys:

- ***"score"*:** —

  The score of the result instance.
- ***"pose"*:** —

  The pose of the result instance in world coordinate systems.
- ***"cameras"*:** —

  A tuple of integers containing the camera indices in which the
  instance was detected in.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`images`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / real)

Input images.

**`deep3DMatchingModel`** (input_control)  deep_matching_3d `→` [HDeepMatching3D](HDeepMatching3D.md), [HTuple](HTuple.md) (*IntPtr*)

Deep 3D Matching model.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Name of parameters.

Default:
[]

Suggested values:

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Value of parameters.

Default:
[]

Suggested values:

**`deepMatchingResults`** (output_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Results.

## Module

3D Metrology
