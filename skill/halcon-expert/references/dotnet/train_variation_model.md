# TrainVariationModel (Operator)

## Name

`TrainVariationModel` — Train a variation model.

## Signature

`static void HOperatorSet.TrainVariationModel(HObject images, HTuple modelID)`

`void HVariationModel.TrainVariationModel(HImage images)`

`void HImage.TrainVariationModel(HVariationModel modelID)`

## Description

`TrainVariationModel` trains the variation model that is
passed in *`modelID`* with one or more images, which are passed
in *`images`*.

As described for [`CreateVariationModel`](create_variation_model.md), a variation model
that has been created using the mode *"standard"* can be
trained iteratively, i.e., as soon as images of good objects become
available, they can be trained with `TrainVariationModel`.
The ideal image of the object is computed as the mean of all
previous training images and the images that are passed in
*`images`*. The corresponding variation image is computed as
the standard deviation of the training images and the images that
are passed in *`images`*.

If the variation model has been created using the mode
*"robust"*, the model cannot be trained iteratively, i.e.,
all training images must be accumulated using [`ConcatObj`](concat_obj.md) and
be trained with `TrainVariationModel` in a single call. If
any images have been trained previously, the training information of
the previous call is discarded. The image of the ideal object is
computed as the median of all training images passed in
*`images`*. The corresponding variation image is computed as a
suitably scaled median absolute deviation of the training images and
the median image.

## Attention

At most 65535 training images can be trained.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`images`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Images of the object to be trained.

**`modelID`** (input_control, state is modified)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

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

`TrainVariationModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`CreateVariationModel`,
`FindGenericShapeModel`,
`AffineTransImage`,
`ConcatObj`

## Possible Successors

`PrepareVariationModel`

## See also

`PrepareVariationModel`,
`CompareVariationModel`,
`CompareExtVariationModel`,
`ClearVariationModel`

## Module

Matching
