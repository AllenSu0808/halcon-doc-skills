# SetStereoModelImagePairs (Operator)

## Name

`SetStereoModelImagePairs` — Specify image pairs to be used for surface stereo reconstruction.

## Signature

`static void HOperatorSet.SetStereoModelImagePairs(HTuple stereoModelID, HTuple from, HTuple to)`

`void HStereoModel.SetStereoModelImagePairs(HTuple from, HTuple to)`

## Description

The operator `SetStereoModelImagePairs` stores a list of image
pairs for a stereo model *`stereoModelID`* of type
*"surface_pairwise"* or *"surface_fusion"*.
Calling the operator for a model of another type
will raise an error. In the mode *"surface_pairwise"* or
*"surface_fusion"*, surfaces are
reconstructed by computing disparity images for image pairs. You specify
these image pairs by passing tuples of camera indices in the parameters
*`from`* and *`to`*. Then, e.g., the disparity image from
the camera with index `From[0]` to the camera with index
`To[0]` is computed and so on.

The camera indices must be valid for the camera setup model assigned to the
stereo model (see [`CreateStereoModel`](create_stereo_model.md)), otherwise an error is
returned. If an image pairs list already exists in the stereo model, it is
substituted by the current one.

Besides storing the list of image pairs, the operator
`SetStereoModelImagePairs` prepares a pair of rectification
image maps for each image pair, which are used repeatedly in successive
calls to [`ReconstructSurfaceStereo`](reconstruct_surface_stereo.md) to rectify the
images to a normalized binocular stereo pair; refer to
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md) for further details.
Three of the [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md) parameters
are exported as stereo model parameters and can be modified by
[`SetStereoModelParam`](set_stereo_model_param.md) or just inspected by
[`GetStereoModelParam`](get_stereo_model_param.md):

- ***"rectif_interpolation"*:** —

  Interpolation mode corresponding to the parameter `mapType`
  of [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md).
- ***"rectif_sub_sampling"*:** —

  sub-sampling factor corresponding to the parameter `subSampling`
  of [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md).
- ***"rectif_method"*:** —

  Rectification method corresponding to the parameter `method`
  of [`GenBinocularRectificationMap`](gen_binocular_rectification_map.md).

Note that after modifying these parameters,
`SetStereoModelImagePairs` must be executed again for the changes
to take effect.

The current list of image pairs in the model can be inspected by
[`GetStereoModelImagePairs`](get_stereo_model_image_pairs.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- stereoModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`stereoModelID`** (input_control, state is modified)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`from`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Camera indices for the *from* cameras in the
image pairs.

Number of elements:
From > 0

**`to`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Camera indices for the *to* cameras in the
image pairs.

Number of elements:
To == From

## Possible Predecessors

`CreateStereoModel`

## Possible Successors

`ReconstructSurfaceStereo`

## See also

`SetStereoModelParam`,
`GetStereoModelImagePairs`

## Module

3D Metrology
