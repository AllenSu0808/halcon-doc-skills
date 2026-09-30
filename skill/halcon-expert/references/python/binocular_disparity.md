# binocular_disparity (Operator)

## Name

`binocular_disparity` — Compute the disparities of a rectified image pair using correlation
techniques.

## Signature

`def binocular_disparity(image_rect_1: HObject, image_rect_2: HObject, method: str, mask_width: int, mask_height: int, texture_thresh: Union[float, int], min_disparity: int, max_disparity: int, num_levels: int, score_thresh: Union[float, int], filter: MaybeSequence[str], sub_disparity: str) -> Tuple[HObject, HObject]`

## Description

`binocular_disparity` computes pixel-wise correspondences
between two rectified images using correlation techniques. Different
from [`binocular_distance`](binocular_distance.md) the results are not transformed into
distance values.

The algorithm requires a reference image *`image_rect_1`* and a
search image *`image_rect_2`* which must be rectified, i.e.,
corresponding epipolar lines are parallel and lie on identical image
rows ($r_{1}=r_{2}$). In case this assumption is
violated the images can be rectified by using the operators
[`calibrate_cameras`](calibrate_cameras.md), [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md),
and [`map_image`](map_image.md). Hence, given a pixel in the reference image
*`image_rect_1`* the homologous pixel in *`image_rect_2`* is
selected by searching along the corresponding row in
*`image_rect_2`* and matching a local neighborhood within a
rectangular window of size *`mask_width`* and
*`mask_height`*. The pixel correspondences are returned in the
single-channel *`disparity`* image $d(r_{1},c_{1})$ which specifies for each pixel $(r1,c1)$ of
the reference image *`image_rect_1`* a suitable matching pixel
$(r2,c2)$ of *`image_rect_2`* according to the equation
$c_{2}=c_{1}+d(r_{1},c_{1})$.
A quality measure for each disparity value is returned in *`score`*,
containing the best result of the matching function $S$ of a reference
pixel. For the matching, the gray values of the original unprocessed
images are used.

The used matching function is defined by the parameter
*`method`* allocating three different kinds of correlation:

- *"sad"*: Summed Absolute Differences
  $$S(r,c,d) = \frac{1}{N} \sum_{r'=r-m}^{r} \sum_{c'=c-n}^{c} \left| q_1(r',c') - q_2(r',c' + d) \right|$$ ![figure](../assets/3009f0825eeeef7d.svg)
  with $0\le S(r,c,d)\le255$.
- *"ssd"*: Summed Squared Differences
  $$S(r,c,d) = \frac{1}{N} \sum_{r' = r - m}^{r + m} \sum_{c' = c - n}^{c + n} \bigl( g_1(r', c') - g_2(r', c' + d) \bigr)^2,$$ ![figure](../assets/6584c320d02d33d9.svg)
  with $0\le S(r,c,d)\le65025$.
- *"ncc"*: Normalized Cross Correlation
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

Note that the methods *"sad"* and *"ssd"* compare the
gray values of the pixels within a mask window directly, whereas
*"ncc"* compensates for the mean gray value and its variance
within the mask window. Therefore, if the two images differ in
brightness and contrast, this method should be preferred. For images
with similar brightness and contrast *"sad"* and
*"ssd"* are to be preferred as they are faster because of
less complex internal computations.

It should be noted, that the quality of correlation for rising
$S$ is falling in methods *"sad"* and *"ssd"*
(the best quality value is 0) but rising in method *"ncc"*
(the best quality value is 1.0).

The size of the correlation window, referenced by $2m+1$
and $2n+1$, has to be odd numbered and is passed in
*`mask_width`* and *`mask_height`*. The search space is
confined by the minimum and maximum disparity value
*`min_disparity`* and *`max_disparity`*. Due to pixel values
not defined beyond the image border the resulting domain of
*`disparity`* and *`score`* is not set along the image
border within a margin of height (*`mask_height`*-1)/2 at the
top and bottom border and of width (*`mask_width`*-1)/2 at the
left and right border. For the same reason, the maximum disparity
range is reduced at the left and right image border.

Since matching turns out to be highly unreliable when dealing with
poorly textured areas, the minimum statistical spread of gray values
within the correlation window can be defined in
*`texture_thresh`*. This threshold is applied on both input
images *`image_rect_1`* and *`image_rect_2`*. In addition,
*`score_thresh`* guarantees the matching quality and defines the
maximum (*"sad"*,*"ssd"*) or, respectively, minimum
(*"ncc"*) score value of the correlation function. Setting
*`filter`* to *"left_right_check"*, moreover, increases
the robustness of the returned matches, as the result relies on a
concurrent direct and reverse match, whereas *"none"*
switches it off.

The number of pyramid levels used to improve the time response of
`binocular_disparity` is determined by
*`num_levels`*. Following a coarse-to-fine scheme disparity
images of higher levels are computed and segmented into rectangular
subimages of similar disparity to reduce the disparity range on the
next lower pyramid level. *`texture_thresh`* and
*`score_thresh`* are applied on every level and the returned
domain of the *`disparity`* and *`score`* images arises
from the intersection of the resulting domains of every single
level. Generally, pyramid structures are the more advantageous the
more the disparity image can be segmented into regions of
homogeneous disparities and the bigger the disparity range is
specified. As a drawback, coarse pyramid levels might loose
important texture information which can result in deficient
disparity values.

Finally, the value *"interpolation"* for parameter
*`sub_disparity`* performs subpixel refinement of
disparities. It is switched off by setting the parameter to
*"none"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image_rect_1`** (input_object)  singlechannelimage `→` HObject (byte)

Rectified image of camera 1.

**`image_rect_2`** (input_object)  singlechannelimage `→` HObject (byte)

Rectified image of camera 2.

**`disparity`** (output_object)  singlechannelimage `→` HObject (real)

Disparity map.

**`score`** (output_object)  singlechannelimage `→` HObject (real)

Evaluation of the disparity values.

**`method`** (input_control)  string `→` str

Matching function.

Default:
"ncc"

List of values:
"ncc", "sad", "ssd"

**`mask_width`** (input_control)  integer `→` int

Width of the correlation window.

Default:
11

Suggested values:
5, 7, 9, 11, 21

Restriction:
`3 <= MaskWidth && odd(MaskWidth)`

**`mask_height`** (input_control)  integer `→` int

Height of the correlation window.

Default:
11

Suggested values:
5, 7, 9, 11, 21

Restriction:
`3 <= MaskHeight && odd(MaskHeight)`

**`texture_thresh`** (input_control)  real `→` Union[float, int]

Variance threshold of textured image regions.

Default:
0.0

Suggested values:
0.0, 10.0, 30.0

Restriction:
`0.0 <= TextureThresh`

**`min_disparity`** (input_control)  integer `→` int

Minimum of the expected disparities.

Default:
-30

Value range:
`-32768
≤
min_disparity
≤
32767`

**`max_disparity`** (input_control)  integer `→` int

Maximum of the expected disparities.

Default:
30

Value range:
`-32768
≤
max_disparity
≤
32767`

**`num_levels`** (input_control)  integer `→` int

Number of pyramid levels.

Default:
1

Suggested values:
1, 2, 3, 4

Restriction:
`1 <= NumLevels`

**`score_thresh`** (input_control)  real `→` Union[float, int]

Threshold of the correlation function.

Default:
0.5

Suggested values:
-1.0, 0.0, 0.3, 0.5, 0.7

**`filter`** (input_control)  string(-array) `→` MaybeSequence[str]

Downstream filters.

Default:
"none"

List of values:
"left_right_check", "none"

**`sub_disparity`** (input_control)  string `→` str

Subpixel interpolation of disparities.

Default:
"none"

List of values:
"interpolation", "none"

## Result

`binocular_disparity` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`map_image`

## Possible Successors

`threshold`,
`disparity_to_distance`,
`disparity_image_to_xyz`

## Alternatives

`binocular_disparity_mg`,
`binocular_disparity_ms`,
`binocular_distance`,
`binocular_distance_mg`,
`binocular_distance_ms`

## See also

`map_image`,
`gen_binocular_rectification_map`,
`binocular_calibration`

## Module

3D Metrology
