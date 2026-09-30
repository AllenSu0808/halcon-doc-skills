# closest_point_transform (Operator)

## Name

`closest_point_transform` — Compute the closest-point transformation of a region.

## Signature

`closest_point_transform(Region : Distances, ClosestPoints : Metric, Foreground, ClosestPointMode, Width, Height : )`

## Description

`closest_point_transform` computes for every pixel of the
input region *`Region`* (or its complement, respectively) the
distance to the closest pixel outside the region (i.e., to the pixel
on the outside border of the region) and returns this information in
*`Distances`*. In addition to the distance, the corresponding
closest pixel is returned in *`ClosestPoints`*.

The parameter *`Foreground`* determines whether the distances
are calculated for all points within the region (*`Foreground`*
= *'true'*) or for all points outside the region
(*`Foreground`* = *'false'*). The distance is computed
for every pixel of the output images *`Distances`* and
*`ClosestPoints`*. The size of the images is specified by
*`Width`* and *`Height`*. The input region is always
clipped to the extent of the output image. If it is important that
the distances within the entire region should be computed, the
region should be moved (see [`move_region`](move_region.md)) so that it has only
positive coordinates and the width and height of the output image
should be large enough to contain the region. The extent of the
input region can be obtained with [`smallest_rectangle1`](smallest_rectangle1.md).

The parameter *`Metric`* determines which metric is used for
the calculation of the distances. If *`Metric`* =
*'city-block'*, the distance is calculated from the shortest
path from the point to the border of the region, where only
horizontal and vertical “movements” are allowed. They are
weighted with a weight of 1. If *`Metric`* =
*'chessboard'*, the distance is calculated from the shortest
path to the border, where horizontal, vertical, and diagonal
“movements” are allowed. They are weighted with a weight of 1.
If *`Metric`* = *'octagonal'*, a combination of these
approaches is used, which leads to diagonal paths receiving a higher
weight. If *`Metric`* = *'chamfer-3-4'*, horizontal and
vertical movements are weighted with a weight of 3, while diagonal
movements are weighted with a weight of 4. To normalize the
distances, the resulting distance image is divided by 3. Since this
normalization step takes some time, and one usually is interested in
the relative distances of the points, the normalization can be
suppressed with *`Metric`* =
*'chamfer-3-4-unnormalized'*. Finally, if *`Metric`* =
*'euclidean'*, the computed distance is approximately
Euclidean.

The parameter *`ClosestPointMode`* determines how the closest
points are stored. For *`ClosestPointMode`* =
*'absolute'*, absolute coordinates are stored in
*`ClosestPoints`*. For *`ClosestPointMode`* =
*'relative'*, the offset to the coordinate of the respective
pixel is stored in *`ClosestPoints`*.

## Attention

It should be noted that the closest points are usually not unique,
i.e., for each pixel in the image *`Distances`*, there usually
exist several points on the outer border of the region that have the
respective distance to that pixel. For example, all points on the
skeleton of the region in the chosen metric have the same distance
to at least two distinct points on the outer border of the region.
`closest_point_transform` returns one of these points that is
determined by the implementation of the algorithm. In particular,
invariances with respect to rotation or mirroring of the region
should *not* be expected.

Furthermore, it should be noted that for *`Foreground`* =
*'true'*, point coordinates that lie outside the image
defined by *`Width`* and *`Height`* are returned if the
input region *`Region`* touches the border of this image, since
in this case the outside border of the region lies one pixel outside
of the image. If the returned coordinates should be used for a
direct access to an image, a suitable border treatment must be
implemented.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region for which the distance to the border is
computed.

**`Distances`** (output_object)  image `→` object (int4)

Image containing the distance information.

**`ClosestPoints`** (output_object)  image `→` object (vector_field)

Image containing the coordinates of the closest points.

**`Metric`** (input_control)  string `→`  (string)

Type of metric to be used for the closest-point
transformation.

Default:
'city-block'

List of values:
'chamfer-3-4', 'chamfer-3-4-unnormalized', 'chessboard', 'city-block', 'euclidean', 'octagonal'

**`Foreground`** (input_control)  string `→`  (string)

Compute the distance for pixels inside (*'true'*)
or outside (*'false'*) the input region.

Default:
'true'

List of values:
'false', 'true'

**`ClosestPointMode`** (input_control)  string `→`  (string)

Mode in which the coordinates of the closest points
are returned.

Default:
'absolute'

List of values:
'absolute', 'relative'

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the output images.

Default:
640

Suggested values:
160, 192, 320, 384, 640, 768

Value range:
`1
≤
Width`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the output images.

Default:
480

Suggested values:
120, 144, 240, 288, 480, 576

Value range:
`1
≤
Height`

## Complexity

The runtime complexity is O(*`Width`***`Height`*).

## Result

`closest_point_transform` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Possible Successors

`threshold`,
`vector_field_to_real`

## Alternatives

`distance_transform`

## See also

`skeleton`

## References

Y. Ge, C.R. Maurer, Jr., J.M. Fitzpatrick: “Surface-based 3-D image
registration using the Iterative Closest Point algorithm with a
closest point transform”; in: “Medical Imaging 1996: Image
Processing”, M.H. Loew, K.M. Hanson, Editors, Proc. SPIE 2710,
pages 358--367, 1996.
  
P. Soille: “Morphological Image Analysis, Principles and
Applications”; Springer Verlag Berlin Heidelberg New York, 1999.
  
G. Borgefors: “Distance Transformations in Arbitrary Dimensions”;
Computer Vision, Graphics, and Image Processing, Vol. 27, pages
321--345, 1984.
  
P.E. Danielsson: “Euclidean Distance Mapping”; Computer Graphics
and Image Processing, Vol. 14, pages 227--248, 1980.

## Module

Foundation
