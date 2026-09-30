# set_shape_model_metric (Operator)

## Name

`set_shape_model_metric` — Set the metric of a shape model that was created from XLD contours.

## Signature

`set_shape_model_metric(Image : : ModelID, HomMat2D, Metric : )`

## Description

`set_shape_model_metric` changes the value of the parameter
*`Metric`* that was selected during the creation of the shape model
*`ModelID`* from XLD contours. For this, the polarity of the model
edges is determined based on the image *`Image`*. The transformation
that maps the model edges to the image position where the respective object
appears is given in *`HomMat2D`*.

The parameter *`Metric`* determines the conditions under which the model
is recognized later in the search image. If *`Metric`* =
*'use_polarity'*, the object in the image and the model must have the
same contrast. If, for example, the model is a bright object on a dark
background, the object is found only if it is also brighter than the
background. If *`Metric`* = *'ignore_global_polarity'*, the
object is found in the image also if the contrast reverses globally. In the
above example, the object hence is also found if it is darker than the
background. The runtime of [`find_generic_shape_model`](find_generic_shape_model.md) will increase
slightly in this case.

It must be ensured that the object edges in the *`Image`* have the same
(or inverse) polarity as the object edges in the image in which the object
must be searched later. Especially, the object must not be occluded in the
*`Image`* and the background must be either brighter than the object or
darker. Otherwise, the determined polarity of the model edges will not
represent the polarity of the object edges during the search. Note that only
the polarity of the edges is determined, not their contrast. Note also that
the polarity is determined from a single-channel image, only. If a
multichannel image is passed in *`Image`*, only the first channel will
be used (and no error message will be returned).

The transformation defined by the matrix *`HomMat2D`* maps the model
contours to the respective position where the object appears in the
*`Image`*. It can be obtained by finding the object in the
*`Image`*, e.g., with the operator [`find_generic_shape_model`](find_generic_shape_model.md) and
determining the respective transformation matrix with the procedure
`get_hom_mat2d_from_matching_result`.
The operator `set_shape_model_metric`
ignores an origin that was set by [`set_shape_model_origin`](set_shape_model_origin.md) and always
assumes (0,0) as the origin. Hence, when finding the object in the
*`Image`*, all other operators must have the origin at the point (0,0).
Therefore, [`set_shape_model_origin`](set_shape_model_origin.md) must be called with (0,0) as the
origin.

A typical proceeding is to read the XLD contours from file. Since these XLD
contours do not provide polarity information, the shape model must be created
from the XLD contours by setting the parameter `Metric` to
*'ignore_local_polarity'*. Then, in a first search image the model
is recognized. The transformation that maps the model contours to the
position of the object in the search image can be determined from the
matching result. To verify the match interactively, the model contours can
be mapped to this position. If the matching result is correct, the value of
the parameter *`Metric`* can be changed, e.g., to
*'use_polarity'*. This leads to a faster and more robust recognition
in the following images.

## Attention

`set_shape_model_metric` can only be used with shape models that were
created from XLD contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image used for the determination of the
polarity.

**`ModelID`** (input_control, state is modified)  shape_model `→`  (handle)

Handle of the model.

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Transformation matrix.

**`Metric`** (input_control)  string `→`  (string)

Match metric.

Default:
'use_polarity'

List of values:
'ignore_global_polarity', 'use_polarity'

## Example (HDevelop)

```
*
* Read the contours from file
read_contour_xld_dxf (Contours, 'metal-part-01', [], [], DxfStatus)
*
* Scale the contours such that they correspond to the image
hom_mat2d_identity (HomMat2DIdentity)
hom_mat2d_scale (HomMat2DIdentity, 3.35, 3.35, 0, 0, HomMat2DScale)
affine_trans_contour_xld (Contours, ContoursAffineTrans, HomMat2DScale)
*
* Create the shape model with Metric='ignore_local_polarity'
create_generic_shape_model (ModelID)
train_generic_shape_model (ContoursAffineTrans, ModelID)
*
* Get an image of the object and try to find the object in this image
read_image (Image, 'metal-parts/metal-parts-01')
find_generic_shape_model (Image, ModelID, MatchResultID, NumMatchResult)
*
* Visualize the match
get_generic_shape_model_result_object (Objects, MatchResultID, 'all', \
                                       'contours')
stop()
get_generic_shape_model_result (MatchResultID, 'all', 'hom_mat_2d', \
                                HomMat2D)
*
* Set the matching metric to 'use_polarity', based on the position
* of the found object
set_shape_model_metric (Image, ModelID, HomMat2D, 'use_polarity')
*
* Use the shape model to detect the object faster and more robust
read_image (Image, 'metal-parts/metal-parts-02')
find_generic_shape_model (Image, ModelID, MatchResultID, NumMatchResult)
*
* Visualize the matches
get_generic_shape_model_result_object (Objects, MatchResultID, 'all', \
                                       'contours')
```

## Result

If the parameters are valid, the operator `set_shape_model_metric`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`create_generic_shape_model`

## Possible Successors

`find_generic_shape_model`

## See also

`set_generic_shape_model_param`

## Module

Matching
