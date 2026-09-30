# get_stereo_model_image_pairs (Operator)

## Name

`get_stereo_model_image_pairs` — Return the list of image pairs set in a stereo model.

## Signature

`def get_stereo_model_image_pairs(stereo_model_id: HHandle) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `get_stereo_model_image_pairs` returns the list
of image pairs for the stereo model *`stereo_model_id`*.
The camera indices of the *from* and *to* cameras in
the pairs are returned in the parameters *`from`* and
*`to`*, respectively (the terms "from" and "to" signal that
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

**`stereo_model_id`** (input_control)  stereo_model `→` HHandle

Handle of the stereo model.

**`from`** (output_control)  integer-array `→` Sequence[int]

Camera indices for the *from* cameras in the image
pairs.

**`to`** (output_control)  integer-array `→` Sequence[int]

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
