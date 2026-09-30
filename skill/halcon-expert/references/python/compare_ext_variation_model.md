# compare_ext_variation_model (Operator)

## Name

`compare_ext_variation_model` — Compare an image to a variation model.

## Signature

`def compare_ext_variation_model(image: HObject, model_id: HHandle, mode: str) -> HObject`

## Description

`compare_ext_variation_model` compares the input image
*`image`* to the variation model given by *`model_id`*.
`compare_ext_variation_model` is an extension of
[`compare_variation_model`](compare_variation_model.md) that provides more modes for the
image comparison. Before `compare_ext_variation_model` can be
called, the two internal threshold images of the variation model
must have been created with [`prepare_variation_model`](prepare_variation_model.md) or
[`prepare_direct_variation_model`](prepare_direct_variation_model.md). Let c(x,y)
denote the input image *`image`* and $t_{u,l}$
denote the two threshold images (see [`prepare_variation_model`](prepare_variation_model.md)
or [`prepare_direct_variation_model`](prepare_direct_variation_model.md)). Then, for *`mode`*
= *"absolute"* the output region *`region`* contains
all points that differ substantially from the model, i.e., the
points that fulfill the following condition:
$$c(x,y)>t_{u}(x,y)\vee c(x,y)<t_{l}(x,y).$$
This mode is identical to [`compare_variation_model`](compare_variation_model.md). For
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
respective regions can be selected with [`select_obj`](select_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2)

Image of the object to be compared.

**`region`** (output_object)  region(-array) `→` HObject

Region containing the points that differ
substantially from the model.

**`model_id`** (input_control)  variation_model `→` HHandle

ID of the variation model.

**`mode`** (input_control)  string `→` str

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

`compare_ext_variation_model` returns 2 (
H_MSG_TRUE)
if all parameters
are correct and if the internal threshold images have been generated
with [`prepare_variation_model`](prepare_variation_model.md) or
[`prepare_direct_variation_model`](prepare_direct_variation_model.md).

## Possible Predecessors

`prepare_variation_model`,
`prepare_direct_variation_model`

## Possible Successors

`select_obj`,
`connection`

## Alternatives

`compare_variation_model`,
`dyn_threshold`

## See also

`get_thresh_images_variation_model`

## Module

Matching
