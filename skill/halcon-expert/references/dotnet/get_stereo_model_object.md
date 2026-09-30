# GetStereoModelObject (Operator)

## Name

`GetStereoModelObject` — Get intermediate iconic results of a stereo reconstruction.

## Signature

`static void HOperatorSet.GetStereoModelObject(out HObject objectVal, HTuple stereoModelID, HTuple pairIndex, HTuple objectName)`

`HObject HStereoModel.GetStereoModelObject(HTuple pairIndex, string objectName)`

`HObject HStereoModel.GetStereoModelObject(int pairIndex, string objectName)`

## Description

With the operator `GetStereoModelObject` you can
access and inspect intermediate iconic results of a surface
reconstruction performed with [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for
the stereo model *`stereoModelID`*. In particular, this is
useful for troubleshooting the reconstruction process.
Note that to collect the
iconic results, you must enable the *"persistence"* mode for
the stereo model (see [`SetStereoModelParam`](set_stereo_model_param.md)) *before*
performing the reconstruction.
Iconic results are then associated with each image pair that was
processed during the reconstruction (see
[`GetStereoModelImagePairs`](get_stereo_model_image_pairs.md)).

You select the image pair of interest by specifying the
corresponding camera indices `[From, To]` in *`pairIndex`*.
By setting one of the following values in *`objectName`*,
the corresponding iconic objects are then returned in *`objectVal`*:

- ***"from_image_rect"*, *"to_image_rect"*:** —

  Rectified image corresponding to the *from* and
  *to* camera, respectively. Both images can be used to inspect
  the quality of the internal binocular stereo image rectification.
- ***"disparity_image"*:** —

  Disparity image for this pair. The quality of the disparity
  image has a direct impact on the final surface reconstruction.
- ***"score_image"*:** —

  Score image assigned to the disparity image for this pair.

A mismatch between the rectified images, i.e., features appearing in
different rows in the two images, or errors in the disparity or the
score image have direct impact on the quality of the final surface
reconstruction. Therefore, we recommend to correct any detected
imperfections by adjusting the stereo model parameters (see
[`SetStereoModelParam`](set_stereo_model_param.md)), in particular those which control
the internal usage of [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md) and
[`BinocularDisparity`](binocular_disparity.md) (see [`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md)
and [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) for further details).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Iconic result.

**`stereoModelID`** (input_control)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`pairIndex`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / string / double)

Camera indices of the pair (`[From, To]`).

Suggested values:
0, 1, 2

**`objectName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the iconic result to be returned.

Suggested values:
"from_image_rect", "to_image_rect", "disparity_image", "score_image"

## Possible Predecessors

`ReconstructSurfaceStereo`

## Module

3D Metrology
