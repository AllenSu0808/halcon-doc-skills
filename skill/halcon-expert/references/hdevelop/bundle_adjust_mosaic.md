# bundle_adjust_mosaic (Operator)

## Name

`bundle_adjust_mosaic` — Perform a bundle adjustment of an image mosaic.

## Signature

`bundle_adjust_mosaic( : : NumImages, ReferenceImage, MappingSource, MappingDest, HomMatrices2D, Rows1, Cols1, Rows2, Cols2, NumCorrespondences, Transformation : MosaicMatrices2D, Rows, Cols, Error)`

## Description

`bundle_adjust_mosaic` performs a bundle adjustment of an
image mosaic. This can be used to determine the geometry of a
mosaic as robustly as possible, and hence to determine the
transformations of the images in the mosaic more accurately than
with single image pairs.

To achieve this, the projective transformation for each overlapping
image pair in the mosaic should be determined with
[`proj_match_points_ransac`](proj_match_points_ransac.md). For example, for a
2×2 block of images in the following layout

|  |  |
| --- | --- |
| 1 | 2 |
| 3 | 4 |

the following projective transformations should be determined,
assuming that all images overlap each other: 1->2,
1->3, 1->4, 2->3,
2->4 and 3->4. The indices of the
images that determine the respective transformation are given by
*`MappingSource`* and *`MappingDest`*. The indices are
start at 1. Consequently, in the above example
*`MappingSource`* = *[1,1,1,2,2,3]* and
*`MappingDest`* = *[2,3,4,3,4,4]* must be used. The
number of images in the mosaic is given by *`NumImages`*. It
is used to check whether each image can be reached by a chain of
transformations. The index of the reference image is given by
*`ReferenceImage`*. On output, this image has the identity
matrix as its transformation matrix.

The 3×3 projective transformation matrices that
correspond to the image pairs are passed in *`HomMatrices2D`*.
Additionally, the coordinates of the matched point pairs in the
image pairs must be passed in *`Rows1`*, *`Cols1`*,
*`Rows2`*, and *`Cols2`*. They can be determined from the
output of [`proj_match_points_ransac`](proj_match_points_ransac.md) with [`tuple_select`](tuple_select.md)
or with the HDevelop function `subset`. To enable
`bundle_adjust_mosaic` to determine which point pair belongs
to which image pair, *`NumCorrespondences`* must contain the
number of found point matches for each image pair.

The parameter *`Transformation`* determines the class of
transformations that is used in the bundle adjustment to transform
the image points. This can be used to restrict the allowable
transformations. For *`Transformation`* =
*'projective'*, projective transformations are used (see
[`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md)). For *`Transformation`* =
*'affine'*, affine transformations are used (see
[`vector_to_hom_mat2d`](vector_to_hom_mat2d.md)), for *`Transformation`* =
*'similarity'*, similarity transformations (see
[`vector_to_similarity`](vector_to_similarity.md)), and for *`Transformation`* =
*'rigid'* rigid transformations (see
[`vector_to_rigid`](vector_to_rigid.md)).

The resulting bundle-adjusted transformations are returned as an
array of 3×3 projective transformation matrices in
*`MosaicMatrices2D`*. In addition, the points reconstructed by
the bundle adjustment are returned in (*`Rows`*,
*`Cols`*). The average projection error of the reconstructed
points is returned in *`Error`*. This can be used to check
whether the optimization has converged to useful values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`NumImages`** (input_control)  integer `→`  (integer)

Number of different images that are used for
the calibration.

Restriction:
`NumImages >= 2`

**`ReferenceImage`** (input_control)  integer `→`  (integer)

Index of the reference image.

**`MappingSource`** (input_control)  integer-array `→`  (integer)

Indices of the source images of the transformations.

**`MappingDest`** (input_control)  integer-array `→`  (integer)

Indices of the target images of the transformations.

**`HomMatrices2D`** (input_control)  hom_mat2d-array `→`  (real)

Array of 3×3 projective
transformation matrices.

**`Rows1`** (input_control)  point.x-array `→`  (real / integer)

Row coordinates of corresponding points in the
respective source images.

**`Cols1`** (input_control)  point.y-array `→`  (real / integer)

Column coordinates of corresponding points in
the respective source images.

**`Rows2`** (input_control)  point.x-array `→`  (real / integer)

Row coordinates of corresponding points in the
respective destination images.

**`Cols2`** (input_control)  point.y-array `→`  (real / integer)

Column coordinates of corresponding points in
the respective destination images.

**`NumCorrespondences`** (input_control)  integer-array `→`  (integer)

Number of point correspondences in the
respective image pair.

**`Transformation`** (input_control)  string `→`  (string)

Transformation class to be used.

Default:
'projective'

List of values:
'affine', 'projective', 'rigid', 'similarity'

**`MosaicMatrices2D`** (output_control)  hom_mat2d-array `→`  (real)

Array of 3×3 projective
transformation matrices that determine the
position of the images in the mosaic.

**`Rows`** (output_control)  point.x-array `→`  (real)

Row coordinates of the points reconstructed by the
bundle adjustment.

**`Cols`** (output_control)  point.y-array `→`  (real)

Column coordinates of the points reconstructed by the
bundle adjustment.

**`Error`** (output_control)  real(-array) `→`  (real)

Average error per reconstructed point.

## Example (HDevelop)

```
* Assume that Images contains the four images of the mosaic in the
* layout given in the above description.  Then the following example
* computes the bundle-adjusted transformation matrices.
From := [1,1,1,2,2,3]
To := [2,3,4,3,4,4]
HomMatrices2D := []
Rows1 := []
Cols1 := []
Rows2 := []
Cols2 := []
NumMatches := []
for J := 0 to |From|-1 by 1
    select_obj (Images, ImageF, From[J])
    select_obj (Images, ImageT, To[J])
    points_foerstner (ImageF, 1, 2, 3, 100, 0.1, 'gauss', 'true', \
                      RowsF, ColsF, _, _, _, _, _, _, _, _)
    points_foerstner (ImageT, 1, 2, 3, 100, 0.1, 'gauss', 'true', \
                      RowsT, ColsT, _, _, _, _, _, _, _, _)
    proj_match_points_ransac (ImageF, ImageT, RowsF, ColsF, RowsT, ColsT, \
                              'ncc', 10, 0, 0, 480, 640, 0, 0.5, \
                              'gold_standard', 2, 42, HomMat2D, \
                              Points1, Points2)
    HomMatrices2D := [HomMatrices2D,HomMat2D]
    Rows1 := [Rows1,subset(RowsF,Points1)]
    Cols1 := [Cols1,subset(ColsF,Points1)]
    Rows2 := [Rows2,subset(RowsT,Points2)]
    Cols2 := [Cols2,subset(ColsT,Points2)]
    NumMatches := [NumMatches,|Points1|]
endfor
bundle_adjust_mosaic (4, 1, From, To, HomMatrices2D, Rows1, Cols1, \
                      Rows2, Cols2, NumMatches, 'rigid', MosaicMatrices, \
                      Rows, Columns, Error)
gen_bundle_adjusted_mosaic (Images, MosaicImage, HomMatrices2D, \
                            'default', 'false', TransMat2D)
```

## Result

If the parameters are valid, the operator
`bundle_adjust_mosaic` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`proj_match_points_ransac`,
`proj_match_points_ransac_guided`

## Possible Successors

`gen_bundle_adjusted_mosaic`

## See also

`gen_projective_mosaic`

## Module

Matching
