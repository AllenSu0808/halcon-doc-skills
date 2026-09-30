# BundleAdjustMosaic (Operator)

## Name

`BundleAdjustMosaic` — Perform a bundle adjustment of an image mosaic.

## Signature

`static void HOperatorSet.BundleAdjustMosaic(HTuple numImages, HTuple referenceImage, HTuple mappingSource, HTuple mappingDest, HTuple homMatrices2D, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple numCorrespondences, HTuple transformation, out HTuple mosaicMatrices2D, out HTuple rows, out HTuple cols, out HTuple error)`

`static HHomMat2D[] HHomMat2D.BundleAdjustMosaic(int numImages, int referenceImage, HTuple mappingSource, HTuple mappingDest, HHomMat2D[] homMatrices2D, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple numCorrespondences, string transformation, out HTuple rows, out HTuple cols, out HTuple error)`

`static HHomMat2D[] HHomMat2D.BundleAdjustMosaic(int numImages, int referenceImage, HTuple mappingSource, HTuple mappingDest, HHomMat2D[] homMatrices2D, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple numCorrespondences, string transformation, out HTuple rows, out HTuple cols, out double error)`

## Description

`BundleAdjustMosaic` performs a bundle adjustment of an
image mosaic. This can be used to determine the geometry of a
mosaic as robustly as possible, and hence to determine the
transformations of the images in the mosaic more accurately than
with single image pairs.

To achieve this, the projective transformation for each overlapping
image pair in the mosaic should be determined with
[`ProjMatchPointsRansac`](proj_match_points_ransac.md). For example, for a
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
*`mappingSource`* and *`mappingDest`*. The indices are
start at 1. Consequently, in the above example
*`mappingSource`* = *[1,1,1,2,2,3]* and
*`mappingDest`* = *[2,3,4,3,4,4]* must be used. The
number of images in the mosaic is given by *`numImages`*. It
is used to check whether each image can be reached by a chain of
transformations. The index of the reference image is given by
*`referenceImage`*. On output, this image has the identity
matrix as its transformation matrix.

The 3×3 projective transformation matrices that
correspond to the image pairs are passed in *`homMatrices2D`*.
Additionally, the coordinates of the matched point pairs in the
image pairs must be passed in *`rows1`*, *`cols1`*,
*`rows2`*, and *`cols2`*. They can be determined from the
output of [`ProjMatchPointsRansac`](proj_match_points_ransac.md) with [`TupleSelect`](tuple_select.md)
or with the HDevelop function `subset`. To enable
`BundleAdjustMosaic` to determine which point pair belongs
to which image pair, *`numCorrespondences`* must contain the
number of found point matches for each image pair.

The parameter *`transformation`* determines the class of
transformations that is used in the bundle adjustment to transform
the image points. This can be used to restrict the allowable
transformations. For *`transformation`* =
*"projective"*, projective transformations are used (see
[`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md)). For *`transformation`* =
*"affine"*, affine transformations are used (see
[`VectorToHomMat2d`](vector_to_hom_mat2d.md)), for *`transformation`* =
*"similarity"*, similarity transformations (see
[`VectorToSimilarity`](vector_to_similarity.md)), and for *`transformation`* =
*"rigid"* rigid transformations (see
[`VectorToRigid`](vector_to_rigid.md)).

The resulting bundle-adjusted transformations are returned as an
array of 3×3 projective transformation matrices in
*`mosaicMatrices2D`*. In addition, the points reconstructed by
the bundle adjustment are returned in (*`rows`*,
*`cols`*). The average projection error of the reconstructed
points is returned in *`error`*. This can be used to check
whether the optimization has converged to useful values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`numImages`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of different images that are used for
the calibration.

Restriction:
`NumImages >= 2`

**`referenceImage`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the reference image.

**`mappingSource`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the source images of the transformations.

**`mappingDest`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of the target images of the transformations.

**`homMatrices2D`** (input_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3×3 projective
transformation matrices.

**`rows1`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of corresponding points in the
respective source images.

**`cols1`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of corresponding points in
the respective source images.

**`rows2`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of corresponding points in the
respective destination images.

**`cols2`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of corresponding points in
the respective destination images.

**`numCorrespondences`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of point correspondences in the
respective image pair.

**`transformation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Transformation class to be used.

Default:
"projective"

List of values:
"affine", "projective", "rigid", "similarity"

**`mosaicMatrices2D`** (output_control)  hom_mat2d-array `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Array of 3×3 projective
transformation matrices that determine the
position of the images in the mosaic.

**`rows`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the points reconstructed by the
bundle adjustment.

**`cols`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the points reconstructed by the
bundle adjustment.

**`error`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

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
`BundleAdjustMosaic` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`

## Possible Successors

`GenBundleAdjustedMosaic`

## See also

`GenProjectiveMosaic`

## Module

Matching
