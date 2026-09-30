# set_planar_uncalib_deformable_model_metric (Operator)

## Name

`set_planar_uncalib_deformable_model_metric` — Set the metric of a planar uncalibrated deformable model that was created
from XLD contours.

## Signature

`def set_planar_uncalib_deformable_model_metric(image: HObject, model_id: HHandle, hom_mat_2d: Sequence[float], metric: str) -> None`

## Description

`set_planar_uncalib_deformable_model_metric` changes the value of the
parameter *`metric`* that was selected during the creation of the
deformable model *`model_id`* from XLD contours. Because no information
about the polarity of the model contours is available for XLD contours, the
polarity is determined based on a representative *`image`*. For this,
the model contours are mapped to the respective position where the object
appears in the *`image`* using *`hom_mat_2d`*, which can be obtained
by a previous call to [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md).

The parameter *`metric`* then determines the conditions under which the
model is recognized later in the search image. If *`metric`* =
*"use_polarity"*, the object in the image and the model must have the
same contrast. If, e.g., the model is a bright object on a dark
background, the object is found only if it is also brighter than the
background. If *`metric`* = *"ignore_global_polarity"*, the
object is found in the image also if the contrast reverses globally. In the
above example, the object hence is also found if it is darker than the
background. The runtime of [`find_planar_uncalib_deformable_model`](find_planar_uncalib_deformable_model.md)
will increase slightly in this case.

It must be ensured that the object contours in the *`image`* have the
same (or inverse) polarity as the object contours in the image in which the
object must be searched later. Especially, the object must not be occluded in
the *`image`* and the background must be either brighter than the object
or darker. Otherwise, the determined polarity of the model contour will not
represent the polarity of the object contour during the search. Note that
only the polarity of the contours is determined, not their contrast. Note
also that the polarity is determined from a single-channel image, only. If a
multi-channel image is passed in *`image`*, only the first channel will
be used (and no error message will be returned).

A typical proceeding is to read the XLD contours from file. Since these XLD
contours do not provide polarity information, the model must be created
from the XLD contours by setting the parameter `metric` to
*"ignore_local_polarity"*. Then, in a first search image the model
is recognized. The transformation that maps the model contours to the
position of the object in the search image (*`hom_mat_2d`*) can be
determined from the matching result. To verify the match interactively, the
model contours can be mapped to this position. If the matching result is
correct, the value of the parameter *`metric`* can be changed, e.g., to
*"use_polarity"*. This leads to a faster and more robust recognition
in the following images.

## Attention

`set_planar_uncalib_deformable_model_metric` can only be used with
deformable models that were created from XLD contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image used for the determination of the
polarity.

**`model_id`** (input_control, state is modified)  deformable_model `→` HHandle

Handle of the model.

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Transformation matrix.

**`metric`** (input_control)  string `→` str

Match metric.

Default:
"use_polarity"

List of values:
"ignore_global_polarity", "use_polarity"

## Result

If the parameters are valid, the operator
`set_planar_uncalib_deformable_model_metric` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`create_planar_uncalib_deformable_model_xld`,
`find_planar_uncalib_deformable_model`

## Possible Successors

`find_planar_uncalib_deformable_model`

## See also

`create_planar_uncalib_deformable_model_xld`

## Module

Matching
