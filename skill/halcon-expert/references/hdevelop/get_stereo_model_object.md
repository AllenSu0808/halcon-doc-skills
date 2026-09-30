# get_stereo_model_object (Operator)

## Name

`get_stereo_model_object` — Get intermediate iconic results of a stereo reconstruction.

## Signature

`get_stereo_model_object( : Object : StereoModelID, PairIndex, ObjectName : )`

## Description

With the operator `get_stereo_model_object` you can
access and inspect intermediate iconic results of a surface
reconstruction performed with [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) for
the stereo model *`StereoModelID`*. In particular, this is
useful for troubleshooting the reconstruction process.
Note that to collect the
iconic results, you must enable the *'persistence'* mode for
the stereo model (see [`set_stereo_model_param`](set_stereo_model_param.md)) *before*
performing the reconstruction.
Iconic results are then associated with each image pair that was
processed during the reconstruction (see
[`get_stereo_model_image_pairs`](get_stereo_model_image_pairs.md)).

You select the image pair of interest by specifying the
corresponding camera indices `[From, To]` in *`PairIndex`*.
By setting one of the following values in *`ObjectName`*,
the corresponding iconic objects are then returned in *`Object`*:

- ***'from_image_rect'*, *'to_image_rect'*:** —

  Rectified image corresponding to the *from* and
  *to* camera, respectively. Both images can be used to inspect
  the quality of the internal binocular stereo image rectification.
- ***'disparity_image'*:** —

  Disparity image for this pair. The quality of the disparity
  image has a direct impact on the final surface reconstruction.
- ***'score_image'*:** —

  Score image assigned to the disparity image for this pair.

A mismatch between the rectified images, i.e., features appearing in
different rows in the two images, or errors in the disparity or the
score image have direct impact on the quality of the final surface
reconstruction. Therefore, we recommend to correct any detected
imperfections by adjusting the stereo model parameters (see
[`set_stereo_model_param`](set_stereo_model_param.md)), in particular those which control
the internal usage of [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md) and
[`binocular_disparity`](binocular_disparity.md) (see [`set_stereo_model_image_pairs`](set_stereo_model_image_pairs.md)
and [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) for further details).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Object`** (output_object)  object(-array) `→` object

Iconic result.

**`StereoModelID`** (input_control)  stereo_model `→`  (handle)

Handle of the stereo model.

**`PairIndex`** (input_control)  number(-array) `→`  (integer / string / real)

Camera indices of the pair (`[From, To]`).

Suggested values:
0, 1, 2

**`ObjectName`** (input_control)  string `→`  (string)

Name of the iconic result to be returned.

Suggested values:
'from_image_rect', 'to_image_rect', 'disparity_image', 'score_image'

## Possible Predecessors

`reconstruct_surface_stereo`

## Module

3D Metrology
