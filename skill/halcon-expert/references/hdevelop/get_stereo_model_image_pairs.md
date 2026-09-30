# get_stereo_model_image_pairs (Operator)

## Name

`get_stereo_model_image_pairs` — Return the list of image pairs set in a stereo model.

## Signature

`get_stereo_model_image_pairs( : : StereoModelID : From, To)`

## Description

The operator `get_stereo_model_image_pairs` returns the list
of image pairs for the stereo model *`StereoModelID`*.
The camera indices of the *from* and *to* cameras in
the pairs are returned in the parameters *`From`* and
*`To`*, respectively (the terms "from" and "to" signal that
during reconstruction the disparity "from" one image "to" the other
image of the pair is computed). The indices
identify cameras from the camera setup model assigned to the stereo model
(see [`create_stereo_model`](create_stereo_model.md)).

The list of image pairs can be set with the operator
[`set_stereo_model_image_pairs`](set_stereo_model_image_pairs.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`StereoModelID`** (input_control)  stereo_model `→`  (handle)

Handle of the stereo model.

**`From`** (output_control)  integer-array `→`  (integer)

Camera indices for the *from* cameras in the image
pairs.

**`To`** (output_control)  integer-array `→`  (integer)

Camera indices for the *to* cameras in the image
pairs.

## Possible Predecessors

`set_stereo_model_image_pairs`

## Possible Successors

`reconstruct_surface_stereo`

## See also

`set_stereo_model_image_pairs`

## Module

3D Metrology
