# closest_point_transform (Operator)

## Name

`closest_point_transform` — Compute the closest-point transformation of a region.

## Signature

`def closest_point_transform(region: HObject, metric: str, foreground: str, closest_point_mode: str, width: int, height: int) -> Tuple[HObject, HObject]`

## Description

`closest_point_transform` computes for every pixel of the
input region *`region`* (or its complement, respectively) the
distance to the closest pixel outside the region (i.e., to the pixel
on the outside border of the region) and returns this information in
*`distances`*. In addition to the distance, the corresponding
closest pixel is returned in *`closest_points`*.

The parameter *`foreground`* determines whether the distances
are calculated for all points within the region (*`foreground`*
= *"true"*) or for all points outside the region
(*`foreground`* = *"false"*). The distance is computed
for every pixel of the output images *`distances`* and
*`closest_points`*. The size of the images is specified by
*`width`* and *`height`*. The input region is always
clipped to the extent of the output image. If it is important that
the distances within the entire region should be computed, the
region should be moved (see [`move_region`](move_region.md)) so that it has only
positive coordinates and the width and height of the output image
should be large enough to contain the region. The extent of the
input region can be obtained with [`smallest_rectangle1`](smallest_rectangle1.md).

The parameter *`metric`* determines which metric is used for
the calculation of the distances. If *`metric`* =
*"city-block"*, the distance is calculated from the shortest
path from the point to the border of the region, where only
horizontal and vertical “movements” are allowed. They are
weighted with a weight of 1. If *`metric`* =
*"chessboard"*, the distance is calculated from the shortest
path to the border, where horizontal, vertical, and diagonal
“movements” are allowed. They are weighted with a weight of 1.
If *`metric`* = *"octagonal"*, a combination of these
approaches is used, which leads to diagonal paths receiving a higher
weight. If *`metric`* = *"chamfer-3-4"*, horizontal and
vertical movements are weighted with a weight of 3, while diagonal
movements are weighted with a weight of 4. To normalize the
distances, the resulting distance image is divided by 3. Since this
normalization step takes some time, and one usually is interested in
the relative distances of the points, the normalization can be
suppressed with *`metric`* =
*"chamfer-3-4-unnormalized"*. Finally, if *`metric`* =
*"euclidean"*, the computed distance is approximately
Euclidean.

The parameter *`closest_point_mode`* determines how the closest
points are stored. For *`closest_point_mode`* =
*"absolute"*, absolute coordinates are stored in
*`closest_points`*. For *`closest_point_mode`* =
*"relative"*, the offset to the coordinate of the respective
pixel is stored in *`closest_points`*.

## Attention

It should be noted that the closest points are usually not unique,
i.e., for each pixel in the image *`distances`*, there usually
exist several points on the outer border of the region that have the
respective distance to that pixel. For example, all points on the
skeleton of the region in the chosen metric have the same distance
to at least two distinct points on the outer border of the region.
`closest_point_transform` returns one of these points that is
determined by the implementation of the algorithm. In particular,
invariances with respect to rotation or mirroring of the region
should *not* be expected.

Furthermore, it should be noted that for *`foreground`* =
*"true"*, point coordinates that lie outside the image
defined by *`width`* and *`height`* are returned if the
input region *`region`* touches the border of this image, since
in this case the outside border of the region lies one pixel outside
of the image. If the returned coordinates should be used for a
direct access to an image, a suitable border treatment must be
implemented.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region for which the distance to the border is
computed.

**`distances`** (output_object)  image `→` HObject (int4)

Image containing the distance information.

**`closest_points`** (output_object)  image `→` HObject (vector_field)

Image containing the coordinates of the closest points.

**`metric`** (input_control)  string `→` str

Type of metric to be used for the closest-point
transformation.

Default:
"city-block"

List of values:
"chamfer-3-4", "chamfer-3-4-unnormalized", "chessboard", "city-block", "euclidean", "octagonal"

**`foreground`** (input_control)  string `→` str

Compute the distance for pixels inside (*"true"*)
or outside (*"false"*) the input region.

Default:
"true"

List of values:
"false", "true"

**`closest_point_mode`** (input_control)  string `→` str

Mode in which the coordinates of the closest points
are returned.

Default:
"absolute"

List of values:
"absolute", "relative"

**`width`** (input_control)  extent.x `→` int

Width of the output images.

Default:
640

Suggested values:
160, 192, 320, 384, 640, 768

Value range:
`1
≤
width`

**`height`** (input_control)  extent.y `→` int

Height of the output images.

Default:
480

Suggested values:
120, 144, 240, 288, 480, 576

Value range:
`1
≤
height`

## Complexity

The runtime complexity is O(*`width`***`height`*).

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
