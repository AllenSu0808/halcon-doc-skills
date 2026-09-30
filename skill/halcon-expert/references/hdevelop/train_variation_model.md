# train_variation_model (Operator)

## Name

`train_variation_model` — Train a variation model.

## Signature

`train_variation_model(Images : : ModelID : )`

## Description

`train_variation_model` trains the variation model that is
passed in *`ModelID`* with one or more images, which are passed
in *`Images`*.

As described for [`create_variation_model`](create_variation_model.md), a variation model
that has been created using the mode *'standard'* can be
trained iteratively, i.e., as soon as images of good objects become
available, they can be trained with `train_variation_model`.
The ideal image of the object is computed as the mean of all
previous training images and the images that are passed in
*`Images`*. The corresponding variation image is computed as
the standard deviation of the training images and the images that
are passed in *`Images`*.

If the variation model has been created using the mode
*'robust'*, the model cannot be trained iteratively, i.e.,
all training images must be accumulated using [`concat_obj`](concat_obj.md) and
be trained with `train_variation_model` in a single call. If
any images have been trained previously, the training information of
the previous call is discarded. The image of the ideal object is
computed as the median of all training images passed in
*`Images`*. The corresponding variation image is computed as a
suitably scaled median absolute deviation of the training images and
the median image.

## Attention

At most 65535 training images can be trained.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Images`** (input_object)  singlechannelimage(-array) `→` object (byte / int2 / uint2)

Images of the object to be trained.

**`ModelID`** (input_control, state is modified)  variation_model `→`  (handle)

ID of the variation model.

## Example (HDevelop)

```
create_variation_model (Width, Height, Type, 'standard', ModelID)
for K := 1 to 10 by 1
    read_image (Image, 'pen-' + K$'02')
    find_generic_shape_model (Image, TemplateID, MatchResultID, \
                              NumMatchResult)
    get_generic_shape_model_result (MatchResultID, 'all', 'hom_mat_2d', \
                                    HomMat2D)
    if (NumMatchResult == 1)
        affine_trans_image (Image, ImageTrans, HomMat2D, 'constant', \
                            'false')
        train_variation_model (ImageTrans, ModelID)
    endif
endfor
prepare_variation_model (ModelID, 10, 4)
```

## Result

`train_variation_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`create_variation_model`,
`find_generic_shape_model`,
`affine_trans_image`,
`concat_obj`

## Possible Successors

`prepare_variation_model`

## See also

`prepare_variation_model`,
`compare_variation_model`,
`compare_ext_variation_model`,
`clear_variation_model`

## Module

Matching
