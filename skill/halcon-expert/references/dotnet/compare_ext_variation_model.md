# CompareExtVariationModel (Operator)

## Name

`CompareExtVariationModel` — Compare an image to a variation model.

## Signature

`static void HOperatorSet.CompareExtVariationModel(HObject image, out HObject region, HTuple modelID, HTuple mode)`

`HRegion HVariationModel.CompareExtVariationModel(HImage image, string mode)`

`HRegion HImage.CompareExtVariationModel(HVariationModel modelID, string mode)`

## Description

`CompareExtVariationModel` compares the input image
*`image`* to the variation model given by *`modelID`*.
`CompareExtVariationModel` is an extension of
[`CompareVariationModel`](compare_variation_model.md) that provides more modes for the
image comparison. Before `CompareExtVariationModel` can be
called, the two internal threshold images of the variation model
must have been created with [`PrepareVariationModel`](prepare_variation_model.md) or
[`PrepareDirectVariationModel`](prepare_direct_variation_model.md). Let c(x,y)
denote the input image *`image`* and $t_{u,l}$
denote the two threshold images (see [`PrepareVariationModel`](prepare_variation_model.md)
or [`PrepareDirectVariationModel`](prepare_direct_variation_model.md)). Then, for *`mode`*
= *"absolute"* the output region *`region`* contains
all points that differ substantially from the model, i.e., the
points that fulfill the following condition:
$$c(x,y)>t_{u}(x,y)\vee c(x,y)<t_{l}(x,y).$$
This mode is identical to [`CompareVariationModel`](compare_variation_model.md). For
*`mode`* = *"light"*, *`region`* contains all
points that are too bright:
$$c(x,y)>t_{u}(x,y).$$
For *`mode`* = *"dark"*, *`region`* contains all
points that are too dark:
$$c(x,y)<t_{l}(x,y).$$
Finally, for *`mode`* = *"light_dark"* two regions are
returned in *`region`*. The first region contains the result
of *`mode`* = *"light"*, while the second region
contains the result of *`mode`* = *"dark"*. The
respective regions can be selected with [`SelectObj`](select_obj.md).

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

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method used for comparing the variation model.

Default:
"absolute"

Suggested values:
"absolute", "light", "dark", "light_dark"

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
        compare_ext_variation_model (ImageTrans, RegionDiff, ModelID, \
                                     'absolute')
        dev_display (RegionDiff)
    endif
endfor
```

## Result

`CompareExtVariationModel` returns 2 (
H_MSG_TRUE)
if all parameters
are correct and if the internal threshold images have been generated
with [`PrepareVariationModel`](prepare_variation_model.md) or
[`PrepareDirectVariationModel`](prepare_direct_variation_model.md).

## Possible Predecessors

`PrepareVariationModel`,
`PrepareDirectVariationModel`

## Possible Successors

`SelectObj`,
`Connection`

## Alternatives

`CompareVariationModel`,
`DynThreshold`

## See also

`GetThreshImagesVariationModel`

## Module

Matching
