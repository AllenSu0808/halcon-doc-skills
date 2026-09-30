# GetStereoModelImagePairs (Operator)

## Name

`GetStereoModelImagePairs` — Return the list of image pairs set in a stereo model.

## Signature

`static void HOperatorSet.GetStereoModelImagePairs(HTuple stereoModelID, out HTuple from, out HTuple to)`

`HTuple HStereoModel.GetStereoModelImagePairs(out HTuple to)`

## Description

The operator `GetStereoModelImagePairs` returns the list
of image pairs for the stereo model *`stereoModelID`*.
The camera indices of the *from* and *to* cameras in
the pairs are returned in the parameters *`from`* and
*`to`*, respectively (the terms "from" and "to" signal that
during reconstruction the disparity "from" one image "to" the other
image of the pair is computed). The indices
identify cameras from the camera setup model assigned to the stereo model
(see [`CreateStereoModel`](create_stereo_model.md)).

The list of image pairs can be set with the operator
[`SetStereoModelImagePairs`](set_stereo_model_image_pairs.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stereoModelID`** (input_control)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

**`from`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Camera indices for the *from* cameras in the image
pairs.

**`to`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Camera indices for the *to* cameras in the image
pairs.

## Possible Predecessors

`SetStereoModelImagePairs`

## Possible Successors

`ReconstructSurfaceStereo`

## See also

`SetStereoModelImagePairs`

## Module

3D Metrology
