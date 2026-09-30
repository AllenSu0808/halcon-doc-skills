# binocular_distance (Operator)

## Name

`binocular_distance` — Compute the distance values for a rectified stereo image pair using
correlation techniques.

## Signature

`binocular_distance(ImageRect1, ImageRect2 : Distance, Score : CamParamRect1, CamParamRect2, RelPoseRect, Method, MaskWidth, MaskHeight, TextureThresh, MinDisparity, MaxDisparity, NumLevels, ScoreThresh, Filter, SubDistance : )`

## Description

`binocular_distance` computes the distance values for a
rectified stereo image pair using correlation techniques. The
operator first calculates the disparities between the two images
*`ImageRect1`* and *`ImageRect2`* similar to
[`binocular_disparity`](binocular_disparity.md). The resulting disparities are
transformed into distance values of the corresponding 3D world
points to the rectified stereo camera system as in
[`disparity_to_distance`](disparity_to_distance.md). The distances are returned in the
single-channel image *`Distance`* in which each gray value
represents the distance of the respective 3D world point to the
stereo camera system.

The algorithm requires a reference image *`ImageRect1`* and a
search image *`ImageRect2`* which must be rectified, i.e.,
corresponding epipolar lines are parallel and lie on identical image
rows ($r_{1}=r_{2}$). In case this assumption is
violated the images can be rectified by using the operators
[`calibrate_cameras`](calibrate_cameras.md), [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)
and [`map_image`](map_image.md). Hence, given a pixel in the reference image
*`ImageRect1`* the homologous pixel in *`ImageRect2`* is
selected by searching along the corresponding row in
*`ImageRect2`* and matching a local neighborhood within a
rectangular window of size *`MaskWidth`* and
*`MaskHeight`*. For each defined reference pixel the pixel
correspondences are transformed into distances of the world points
defined by the intersection of the lines of sight of a corresponding
pixel pair to the $z=0$ plane of the rectified stereo
system.

For this transformation the rectified internal camera parameters
*`CamParamRect1`* of camera 1 and *`CamParamRect2`* of
camera 2, and the pose with the external parameters *`RelPoseRect`*
have to be defined. Latter one is of the form
$\text{ccs}R_1 P_{\mathrm{ccs}}R_2$ ![figure](../assets/959330a2a3b8ae9b.svg)
and characterizes the relative pose of both cameras to each other.
More precisely, it specifies the point transformation from the
rectified camera system 2 (*ccsR2*) into the rectified camera system
1 (*ccsR1*), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
These parameters can be obtained from the operator
[`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). After all, a quality
measure for each distance value is returned in *`Score`*,
containing the best result of the matching function $S$ of a
reference pixel. For the matching, the gray values of the original
unprocessed images are used.

- *'sad'*: Summed Absolute Differences
  $$S(r,c,d) = \frac{1}{N} \sum_{r'=r-m}^{r} \sum_{c'=c-n}^{c} \left| q_1(r',c') - q_2(r',c' + d) \right|$$ ![figure](../assets/3009f0825eeeef7d.svg)
  with $0\le S(r,c,d)\le255$.
- *'ssd'*: Summed Squared Differences
  $$S(r,c,d) = \frac{1}{N} \sum_{r' = r - m}^{r + m} \sum_{c' = c - n}^{c + n} \bigl( g_1(r', c') - g_2(r', c' + d) \bigr)^2,$$ ![figure](../assets/6584c320d02d33d9.svg)
  with $0\le S(r,c,d)\le65025$.
- *'ncc'*: Normalized Cross Correlation
  $$S(r, c, d) = \frac{\displaystyle \sum_{r'=r-m}^{r+m} \sum_{c'=c-n}^{c+n} \big(g_1(r', c') - \overline{g_1}(r, c)\big) \big(g_2(r', c'+d) - \overline{g_2}(r, c+d)\big)}{\sqrt{\displaystyle \Big(\sum_{r'=r-m}^{r+m} \sum_{c'=c-n}^{c+n} \big(g_1(r', c') - \overline{g_1}(r, c)\big)^2\Big) \Big(\sum_{r'=r-m}^{r+m} \sum_{c'=c-n}^{c+n} \big(g_2(r', c'+d) - \overline{g_2}(r, c+d)\big)^2\Big)}}$$ ![figure](../assets/78f30a2852198cbd.svg)
  with $-1.0\le S(r,c,d)\le1.0$.

with

$r1$, $c1$, $r2$, $c2$:
row and column coordinates of the corresponding
pixels of the two input images,

$g1$, $g2$: gray values of the unprocessed input images,

$N=(2m+1)(2n+1)$: size of correlation window

$\tilde{\mathbf{g}}(r,c) = \frac{1}{N} \sum_{r' = r - m}^{r + m} \sum_{c' = c - n}^{c + n} g(r',c')$ ![figure](../assets/d7d29a3883ddf0a8.svg): mean value within the correlation window of width
$2m+1$ and height $2n+1$.

Note that the methods *'sad'* and *'ssd'* compare the
gray values of the pixels within a mask window directly, whereas
*'ncc'* compensates for the mean gray value and its variance
within the mask window. Therefore, if the two images differ in
brightness and contrast, this method should be preferred. For images
with similar brightness and contrast *'sad'* and
*'ssd'* are to be preferred as they are faster because of
less complex internal computations. See [`binocular_disparity`](binocular_disparity.md)
for further details.

It should be noted that the quality of correlation for rising $S$ is
falling in methods *'sad'* and *'ssd'* (the best
quality value is 0) but rising in method *'ncc'* (the best
quality value is 1.0).

The size of the correlation window ($2m+1$ and $2n+1$)
has to be odd numbered and is
passed in *`MaskWidth`* and *`MaskHeight`*. The search
space is confined by the minimum and maximum disparity value
*`MinDisparity`* and *`MaxDisparity`*. Due to pixel values
not defined beyond the image border the resulting domain of
*`Distance`* and *`Score`* is generally not set along the
image border within a margin of height *`MaskHeight`*/2 at the
top and bottom border and of width *`MaskWidth`*/2 at the left
and right border. For the same reason, the maximum disparity range
is reduced at the left and right image border.

Since matching turns out to be highly unreliable when dealing with
poorly textured areas, the minimum variance within the correlation
window can be defined in *`TextureThresh`*. This threshold is
applied on both input images *`ImageRect1`* and
*`ImageRect2`*. In addition, *`ScoreThresh`* guarantees
the matching quality and defines the maximum
(*'sad'*,*'ssd'*) or, respectively, minimum
(*'ncc'*) score value of the correlation function. Setting
*`Filter`* to *'left_right_check'*, moreover, increases
the robustness of the returned matches, as the result relies on a
concurrent direct and reverse match, whereas *'none'*
switches it off.

The number of pyramid levels used to improve the time response of
`binocular_distance` is determined by
*`NumLevels`*. Following a coarse-to-fine scheme disparity
images of higher levels are computed and segmented into
rectangular subimages to reduce the disparity range on the next
lower pyramid level. *`TextureThresh`* and *`ScoreThresh`*
are applied on every level and the returned domain of the
*`Distance`* and *`Score`* images arises from the
intersection of the resulting domains of every single
level. Generally, pyramid structures are the more advantageous the
more the distance image can be segmented into regions of homogeneous
distance values and the bigger the disparity range must be
specified. As a drawback, coarse pyramid levels might loose
important texture information which can result in deficient distance
values.

Finally, the value *'interpolation'* for parameter
*`SubDistance`* increases the refinement and accuracy of the
distance values. It is switched off by setting the parameter to
*'none'*.

## Attention

If using cameras with telecentric lenses, the *`Distance`* is
not defined as the distance of a point to the camera but as the
distance from the point to the plane, defined by the y-axes of both
cameras and their baseline (see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)).

For a stereo setup of mixed type (i.e., for a stereo setup in which
one of the original cameras is a perspective camera and the other
camera is a telecentric camera; see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)), the rectifying plane of
the two cameras is in a position with respect to the object that
would lead to very unintuitive distances. Therefore,
`binocular_distance` does not support a stereo setup of mixed
type. For stereo setups of mixed type, please use
[`reconstruct_surface_stereo`](reconstruct_surface_stereo.md), in which the reference
coordinate system can be chosen arbitrarily. Alternatively,
[`binocular_disparity`](binocular_disparity.md) and [`disparity_image_to_xyz`](disparity_image_to_xyz.md) might
be used.

Additionally, stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ImageRect1`** (input_object)  singlechannelimage `→` object (byte)

Rectified image of camera 1.

**`ImageRect2`** (input_object)  singlechannelimage `→` object (byte)

Rectified image of camera 2.

**`Distance`** (output_object)  singlechannelimage `→` object (real)

Distance image.

**`Score`** (output_object)  singlechannelimage `→` object (real)

Evaluation of a distance value.

**`CamParamRect1`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters of the rectified camera 1.

**`CamParamRect2`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters of the rectified camera 2.

**`RelPoseRect`** (input_control)  pose `→`  (real / integer)

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`Method`** (input_control)  string `→`  (string)

Matching function.

Default:
'ncc'

List of values:
'ncc', 'sad', 'ssd'

**`MaskWidth`** (input_control)  integer `→`  (integer)

Width of the correlation window.

Default:
11

Suggested values:
5, 7, 9, 11, 21

Restriction:
`3 <= MaskWidth && odd(MaskWidth)`

**`MaskHeight`** (input_control)  integer `→`  (integer)

Height of the correlation window.

Default:
11

Suggested values:
5, 7, 9, 11, 21

Restriction:
`3 <= MaskHeight && odd(MaskHeight)`

**`TextureThresh`** (input_control)  real `→`  (real / integer)

Variance threshold of textured image regions.

Default:
0.0

Suggested values:
0.0, 2.0, 5.0, 10.0

Restriction:
`0.0 <= TextureThresh`

**`MinDisparity`** (input_control)  integer `→`  (integer)

Minimum of the expected disparities.

Default:
0

Value range:
`-32768
≤
MinDisparity
≤
32767`

**`MaxDisparity`** (input_control)  integer `→`  (integer)

Maximum of the expected disparities.

Default:
30

Value range:
`-32768
≤
MaxDisparity
≤
32767`

**`NumLevels`** (input_control)  integer `→`  (integer)

Number of pyramid levels.

Default:
1

Suggested values:
1, 2, 3, 4

Restriction:
`1 <= NumLevels`

**`ScoreThresh`** (input_control)  real `→`  (real / integer)

Threshold of the correlation function.

Default:
0.0

Suggested values:
0.0, 2.0, 5.0, 10.0

**`Filter`** (input_control)  string(-array) `→`  (string)

Downstream filters.

Default:
'none'

List of values:
'left_right_check', 'none'

**`SubDistance`** (input_control)  string(-array) `→`  (string)

Distance interpolation.

Default:
'none'

List of values:
'interpolation', 'none'

## Example (HDevelop)

```
* Set internal and external stereo parameters.
* Note that, typically, these values are the result of a prior
* calibration.
gen_cam_par_area_scan_division (0.01, -665, 5.2e-006, 5.2e-006, \
                                622, 517, 1280, 1024, CamParam1)
gen_cam_par_area_scan_division (0.01, -731, 5.2e-006, 5.2e-006, \
                                654, 519, 1280, 1024, CamParam2)
create_pose (0.1535,-0.0037,0.0447,0.17,319.84,359.89, \
             'Rp+T', 'gba', 'point', RelPose)
* Compute the mapping for rectified images.
gen_binocular_rectification_map (Map1, Map2, CamParam1, CamParam2, \
                                 RelPose, 1, 'viewing_direction', \
                                 'bilinear', CamParamRect1, CamParamRect2, \
                                 Cam1PoseRect1, Cam2PoseRect2, RelPoseRect)
* Compute the distance values in online images.
while (1)
  grab_image_async (Image1, AcqHandle1, -1)
  map_image (Image1, Map1, ImageRect1)

  grab_image_async (Image2, AcqHandle2, -1)
  map_image (Image2, Map2, ImageRect2)

  binocular_distance (ImageRect1, ImageRect2, Distance, Score, \
                      CamParamRect1, CamParamRect2, RelPoseRect, 'sad', \
                      11, 11, 20, -40, 20, 2, 25, \
                      'left_right_check', 'interpolation')
endwhile
```

## Result

[`binocular_disparity`](binocular_disparity.md) returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`map_image`

## Possible Successors

`threshold`

## Alternatives

`binocular_distance_mg`,
`binocular_distance_ms`,
`binocular_disparity`,
`binocular_disparity_mg`,
`binocular_disparity_ms`

## See also

`map_image`,
`gen_binocular_rectification_map`,
`binocular_calibration`,
`distance_to_disparity`,
`disparity_to_distance`,
`disparity_image_to_xyz`

## Module

3D Metrology
