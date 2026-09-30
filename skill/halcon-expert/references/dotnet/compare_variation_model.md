# CompareVariationModel (Operator)

## Name

`CompareVariationModel` — Compare an image to a variation model.

## Signature

`static void HOperatorSet.CompareVariationModel(HObject image, out HObject region, HTuple modelID)`

`HRegion HVariationModel.CompareVariationModel(HImage image)`

`HRegion HImage.CompareVariationModel(HVariationModel modelID)`

## Description

`CompareVariationModel` compares the input image
*`image`* to the variation model given by *`modelID`*.
Before `CompareVariationModel` can be called, the two
internal threshold images of the variation model must have been
created with [`PrepareVariationModel`](prepare_variation_model.md) or
[`PrepareDirectVariationModel`](prepare_direct_variation_model.md). Let c(x,y)
denote the input image *`image`* and $t_{u,l}$
denote the two threshold images (see [`PrepareVariationModel`](prepare_variation_model.md)
or [`PrepareDirectVariationModel`](prepare_direct_variation_model.md)). Then the output region
*`region`* contains all points that differ substantially from
the model, i.e., the points that fulfill the following condition:
$$c(x,y)>t_{u}(x,y)\vee c(x,y)<t_{l}(x,y).$$
If only too bright or too dark errors should be segmented the
operator [`CompareExtVariationModel`](compare_ext_variation_model.md) can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Image of the object to be compared.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Region containing the points that differ
substantially from the model.

**`modelID`** (input_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

## Example (HDevelop)

```
read_shape_model ('model.shm', TemplateID)
read_variation_model ('model.var', ModelID)
for K := 1 to 10 by 1
    read_image (Image, 'pen-' + K$'02')
    find_generic_shape_model (Image, TemplateID, MatchResultID, \
                              NumMatchResult)
    get_generic_shape_model_result (MatchResultID, 'all', 'hom_mat_2d', \
                                    HomMat2D)
    dev_display (Image)
    if (NumMatchResult == 1)
        affine_trans_image (Image, ImageTrans, HomMat2D, 'constant', \
                            'false')
        compare_variation_model (ImageTrans, RegionDiff, ModelID)
        dev_display (RegionDiff)
    endif
endfor
```

## Result

`CompareVariationModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and if the internal threshold images have been generated
with [`PrepareVariationModel`](prepare_variation_model.md) or
[`PrepareDirectVariationModel`](prepare_direct_variation_model.md).

## Possible Predecessors

`PrepareVariationModel`,
`PrepareDirectVariationModel`

## Possible Successors

`Connection`

## Alternatives

`CompareExtVariationModel`,
`DynThreshold`

## See also

`GetThreshImagesVariationModel`

## Module

Matching
