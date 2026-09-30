# gen_projective_mosaic (Operator)

## Name

`gen_projective_mosaic` — Combine multiple images into a mosaic image.

## Signature

`def gen_projective_mosaic(images: HObject, start_image: int, mapping_source: Sequence[int], mapping_dest: Sequence[int], hom_matrices_2d: Sequence[float], stacking_order: MaybeSequence[Union[str, int]], transform_domain: str) -> Tuple[HObject, Sequence[float]]`

## Description

`gen_projective_mosaic` combines the input images contained in
the object *`images`* into a mosaic image *`mosaic_image`*.
The relative positions of the images are defined by
3x3 projective transformation matrices. The array
*`hom_matrices_2d`* contains a sequence of these linearized
matrices. The values in *`mapping_source`* and
*`mapping_dest`* are the indices of the images that the
corresponding matrix applies to. *`mapping_source`*=*4*
and *`mapping_dest`*=*7* means that the matrix describes
the transformation of the image number *4* into the
projective plane of image *7*. The transformation matrices
between the respective image pairs given by *`mapping_source`*
and *`mapping_dest`* are typically determined with
[`proj_match_points_ransac`](proj_match_points_ransac.md).

As usual for operators that access image objects (e.g.,
[`select_obj`](select_obj.md)), the images are numbered starting from 1, i.e.,
*`mapping_source`*, *`mapping_dest`*, *`start_image`*,
and *`stacking_order`*) must contain values between 1 and the
number of images passed in *`images`*.

The parameter *`start_image`* states which image defines the
image plane of the final image, that is, which input image remains
unchanged in the output image. This is usually an image that is
located near the center of the image mosaic.

The origin of *`mosaic_image`* and its size are automatically
chosen so that all of the input images are completely visible.

The order in which the images are added to the mosaic is given by
the array *`stacking_order`*. The first index in this array
will end up at the bottom of the image stack while the last one will
be on top. If *"default"* is given instead of an array of
integers, the canonical order (images in the order used in
*`images`*) will be used.

The parameter *`transform_domain`* can be used to determine
whether the domains of *`images`* are also transformed. Since
the transformation of the domains costs runtime, this parameter
should be used to specify whether this is desired or not. If
*`transform_domain`* is set to *"false"* the domain of
the input images is ignored and the complete images are
transformed.

On output, the parameter *`mosaic_matrices_2d`* contains a set of
3x3 projective transformation matrices that describe
for each image in *`images`* the mapping of the image to its
position in the mosaic.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`images`** (input_object)  (multichannel-)image-array `→` HObject (byte / uint2 / real)

Input images.

**`mosaic_image`** (output_object)  (multichannel-)image `→` HObject (byte / uint2 / real)

Output image.

**`start_image`** (input_control)  integer `→` int

Index of the central input image.

**`mapping_source`** (input_control)  integer-array `→` Sequence[int]

Indices of the source images of the transformations.

**`mapping_dest`** (input_control)  integer-array `→` Sequence[int]

Indices of the target images of the transformations.

**`hom_matrices_2d`** (input_control)  hom_mat2d-array `→` Sequence[float]

Array of 3x3 projective
transformation matrices.

**`stacking_order`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Stacking order of the images in the mosaic.

Default:
"default"

Suggested values:
"default"

**`transform_domain`** (input_control)  string `→` str

Should the domains of the input images also be
transformed?

Default:
"false"

List of values:
"false", "true"

**`mosaic_matrices_2d`** (output_control)  hom_mat2d-array `→` Sequence[float]

Array of 3x3 projective
transformation matrices that determine the
position of the images in the mosaic.

## Example (HDevelop)

```
gen_empty_obj (Images)
for J := 1 to 6 by 1
    read_image (Image, 'mosaic/pcb_'+J$'02')
    concat_obj (Images, Image, Images)
endfor
From := [1,2,3,4,5]
To := [2,3,4,5,6]
Num := |From|
ProjMatrices := []
for J := 0 to Num-1 by 1
    F := From[J]
    T := To[J]
    select_obj (Images, ImageF, F)
    select_obj (Images, ImageT, T)
    points_foerstner (ImageF, 1, 2, 3, 200, 0.3, 'gauss', 'false', \
                      RowJunctionsF, ColJunctionsF, CoRRJunctionsF, \
                      CoRCJunctionsF, CoCCJunctionsF, RowAreaF, \
                      ColAreaF, CoRRAreaF, CoRCAreaF, CoCCAreaF)
    points_foerstner (ImageT, 1, 2, 3, 200, 0.3, 'gauss', 'false', \
                      RowJunctionsT, ColJunctionsT, CoRRJunctionsT, \
                      CoRCJunctionsT, CoCCJunctionsT, RowAreaT, \
                      ColAreaT, CoRRAreaT, CoRCAreaT, CoCCAreaT)
    proj_match_points_ransac (ImageF, ImageT, RowJunctionsF, \
                              ColJunctionsF, RowJunctionsT, \
                              ColJunctionsT, 'ncc', 21, 0, 0, 480, 640, \
                              0, 0.5, 'gold_standard', 1, 4364537, \
                              ProjMatrix, Points1, Points2)
    ProjMatrices := [ProjMatrices,ProjMatrix]
endfor
gen_projective_mosaic (Images, MosaicImage, 2, From, To, ProjMatrices, \
                       'default', 'false', MosaicMatrices2D)
```

## Possible Predecessors

`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`vector_to_proj_hom_mat2d`,
`hom_vector_to_proj_hom_mat2d`

## See also

`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
