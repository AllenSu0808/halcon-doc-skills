# find_uncalib_descriptor_model (Operator)

## Name

`find_uncalib_descriptor_model` — Find the best matches of a descriptor model in an image.

## Signature

`find_uncalib_descriptor_model(Image : : ModelID, DetectorParamName, DetectorParamValue, DescriptorParamName, DescriptorParamValue, MinScore, NumMatches, ScoreType : HomMat2D, Score)`

## Description

The operator `find_uncalib_descriptor_model` finds the best matches
of a descriptor model *`ModelID`* in *`Image`*.
The descriptor model must have been created previously by calling
[`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md),
[`create_calib_descriptor_model`](create_calib_descriptor_model.md)
or [`read_descriptor_model`](read_descriptor_model.md).

A match is only accepted if its score exceeds the value of
*`MinScore`*. This criterion is based on the 'inlier_ratio'
score that is described in details below. The main result of the operator
`find_uncalib_descriptor_model` for each match is a 3x3 matrix
*`HomMat2D`*, which describes a 2D projection of model points to
search image points and is represented by a tuple of 9 elements in
row-major order. If more matches of the searched object (template)
appear and pass the *`MinScore`* criterion, the resulting multiple
homographies are concatenated. The number of objects actually found is
then equal to NumObjects = |*`HomMat2D`*|/9.

The detection process is divided into three parts. **First**,
interest points are extracted from the search image (only inside the
domain of the search image).
This is done using the point detector and its parameters
selected once during the generation of the model. However,
*`DetectorParamName`* and *`DetectorParamValue`* can be used
to specify different detector parameter values during the
`find_uncalib_descriptor_model` call. By changing these parameters,
it is possible to adjust to illumination changes between the model
generation and the online detection. However, it is recommended to use
the same values used to create the model (pass an empty tuple).

**The second step** of the detection process is to calculate
correspondences between the model points and the points that were
detected. The run time parameters of the descriptor can be adjusted
with *`DescriptorParamName`* and *`DescriptorParamValue`*:

- ***'min_score_descr'*:** —

  is the minimal classifier score for an interest point to be regarded
  as a potential match. The score function is between 0.0 and 1.0,
  but typically only values between 0.0 and 0.1 make sense. Increasing
  *'min_score_descr'* can increase significantly the detection
  speed. Note, however, that using *'min_score_descr'* might have
  negative effect on the robustness of the detection process, especially
  when only few points can be found.
  Typical values are [*0.0* .. *0.1*],
  default value is *0.0*.
- ***'guided_matching'*:** —

  enhances the accuracy
  of the object recognition when switched on. Note that it increases the
  computational costs up to 10% in some cases.
  Possible values are [*'on'*, *'off'*],
  default value is *'on'*.

**The last step** is the estimation of a homography that describes
the point correspondences. The homography is a 2D projection, which
describes a transformation from model points to points in *`Image`*.
Here, Natural 3D Markers (N3Ms) are utilized to identify robustly the point
correspondences (see references).

Additionally to the estimated homography in *`HomMat2D`*, the
operator returns one or more *`Score`* estimations per object
instance as specified by the user in a tuple *`ScoreType`*.
Currently the following values for *`ScoreType`* are supported:

- ***'num_points'*:** —

  number of point
  correspondences per instance. An object instance should be considered
  good, if it has 10 or more point correspondences with the model. Fewer
  points are insufficient, because any random 4 point correspondences
  define a mathematically correct homography between two images.
- ***'inlier_ratio'*:** —

  the ratio of the number
  of point correspondences to the number of model points. Although
  this value can have values of [*0.0* .. *1.0*],
  it is rather unlikely that this ratio can reach *1.0*. Yet,
  objects having inlier ratio less than *0.1*, should be
  disregarded.

Note that the resulting scores for more than one object instance will be
concatenated in *`Score`*, such that
|*`Score`*| = NumObjects*|*`ScoreType`*|.

The point correspondences for each object can be queried with
[`get_descriptor_model_points`](get_descriptor_model_points.md).

## Attention

Note that the domain of the search image should contain the whole
object to be searched for because interest points are only extracted
inside the domain of the search image. This means that if the domain
does not contain the full object to be searched for, the resulting
*`Score`* will decrease. Note also that matches may be found even
if the reference point (origin) of the model lies outside of the
domain of the search image. Both is in contrast to shape-based
matching, where the domain of the search image defines the search
space for the reference point of the model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image where the model should be found.

**`ModelID`** (input_control)  descriptor_model `→`  (handle)

The handle to the descriptor model.

**`DetectorParamName`** (input_control)  attribute.name-array `→`  (string)

The detector's parameter names.

Default:
[]

List of values:
'alpha', 'check_neighbor', 'mask_size_grd', 'mask_size_smooth', 'min_check_neighbor_diff', 'min_score', 'radius', 'sigma_grad', 'sigma_smooth', 'subpix', 'threshold'

**`DetectorParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Values of the detector's parameters.

Default:
[]

Suggested values:
0.08, 1, 1.2, 3, 15, 30, 1000, 'on', 'off'

**`DescriptorParamName`** (input_control)  attribute.name-array `→`  (string)

The descriptor's parameter names.

Default:
[]

List of values:
'guided_matching', 'min_score_descr'

**`DescriptorParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Values of the descriptor's parameters.

Default:
[]

Suggested values:
0.0, 0.001, 0.005, 0.01, 'on', 'off'

**`MinScore`** (input_control)  real(-array) `→`  (real)

Minimum score of the instances of the models to
be found.

Default:
0.2

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
MinScore
≤
1`

**`NumMatches`** (input_control)  integer `→`  (integer)

Maximal number of found instances.

Default:
1

Suggested values:
1, 2, 3, 4

Restriction:
`NumMatches >= 1`

**`ScoreType`** (input_control)  string(-array) `→`  (string)

Score type to be evaluated in *`Score`*.

Default:
'num_points'

List of values:
'inlier_ratio', 'num_points'

**`HomMat2D`** (output_control)  hom_mat2d(-array) `→`  (real)

Homography between model and found instance.

**`Score`** (output_control)  number(-array) `→`  (real / integer)

Score of the found instances according to the
ScoreType input.

## Example (HDevelop)

```
create_uncalib_descriptor_model (ImageReduced,'harris',[],[], \
                                 [],[],42,ModelID)

get_descriptor_model_params (ModelID,DetectorType, \
                             DetectorParamName,DetectorParamValue, \
                             DescriptorParamName,DescriptorParamValue)
write_descriptor_model (ModelID,'simple_example.dsm')

read_descriptor_model ('simple_example.dsm',ModelID)
find_uncalib_descriptor_model (SearchImage,ModelID,[],[],[],[],0.2,1, \
                               ['num_points','inlier_ratio'],HomMat2D,Score)
```

## Possible Predecessors

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`,
`read_descriptor_model`

## See also

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`,
`find_calib_descriptor_model`,
`get_descriptor_model_points`

## References

S. Hinterstoisser, S. Benhimane, and N. Navab: “N3M: Natural 3D Markers for
Real-Time Object Detection and Pose Estimation.“
IEEE 11th International Conference on Computer Vision, 2007. pp. 1-7,
ICCV 2007.

## Module

Matching
