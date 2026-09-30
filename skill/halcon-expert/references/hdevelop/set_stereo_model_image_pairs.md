# set_stereo_model_image_pairs (Operator)

## Name

`set_stereo_model_image_pairs` — Specify image pairs to be used for surface stereo reconstruction.

## Signature

`set_stereo_model_image_pairs( : : StereoModelID, From, To : )`

## Description

The operator `set_stereo_model_image_pairs` stores a list of image
pairs for a stereo model *`StereoModelID`* of type
*'surface_pairwise'* or *'surface_fusion'*.
Calling the operator for a model of another type
will raise an error. In the mode *'surface_pairwise'* or
*'surface_fusion'*, surfaces are
reconstructed by computing disparity images for image pairs. You specify
these image pairs by passing tuples of camera indices in the parameters
*`From`* and *`To`*. Then, e.g., the disparity image from
the camera with index `From[0]` to the camera with index
`To[0]` is computed and so on.

The camera indices must be valid for the camera setup model assigned to the
stereo model (see [`create_stereo_model`](create_stereo_model.md)), otherwise an error is
returned. If an image pairs list already exists in the stereo model, it is
substituted by the current one.

Besides storing the list of image pairs, the operator
`set_stereo_model_image_pairs` prepares a pair of rectification
image maps for each image pair, which are used repeatedly in successive
calls to [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) to rectify the
images to a normalized binocular stereo pair; refer to
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md) for further details.
Three of the [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md) parameters
are exported as stereo model parameters and can be modified by
[`set_stereo_model_param`](set_stereo_model_param.md) or just inspected by
[`get_stereo_model_param`](get_stereo_model_param.md):

- ***'rectif_interpolation'*:** —

  Interpolation mode corresponding to the parameter `MapType`
  of [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md).
- ***'rectif_sub_sampling'*:** —

  sub-sampling factor corresponding to the parameter `SubSampling`
  of [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md).
- ***'rectif_method'*:** —

  Rectification method corresponding to the parameter `Method`
  of [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md).

Note that after modifying these parameters,
`set_stereo_model_image_pairs` must be executed again for the changes
to take effect.

The current list of image pairs in the model can be inspected by
[`get_stereo_model_image_pairs`](get_stereo_model_image_pairs.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- StereoModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`StereoModelID`** (input_control, state is modified)  stereo_model `→`  (handle)

Handle of the stereo model.

**`From`** (input_control)  integer-array `→`  (integer)

Camera indices for the *from* cameras in the
image pairs.

Number of elements:
From > 0

**`To`** (input_control)  integer-array `→`  (integer)

Camera indices for the *to* cameras in the
image pairs.

Number of elements:
To == From

## Possible Predecessors

`create_stereo_model`

## Possible Successors

`reconstruct_surface_stereo`

## See also

`set_stereo_model_param`,
`get_stereo_model_image_pairs`

## Module

3D Metrology
