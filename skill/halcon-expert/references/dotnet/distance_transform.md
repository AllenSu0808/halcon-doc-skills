# DistanceTransform (Operator)

## Name

`DistanceTransform` — Compute the distance transformation of a region.

## Signature

`static void HOperatorSet.DistanceTransform(HObject region, out HObject distanceImage, HTuple metric, HTuple foreground, HTuple width, HTuple height)`

`HImage HRegion.DistanceTransform(string metric, string foreground, int width, int height)`

## Description

`DistanceTransform` computes for every point of the input
region *`region`* (or its complement, respectively) the
distance of the point to the border of the region. The parameter
*`foreground`* determines whether the distances are calculated
for all points within the region (*`foreground`* =
*"true"*) or for all points outside the region
(*`foreground`* = *"false"*). The distance is computed
for every point of the output image *`distanceImage`*, which
has the specified dimensions *`width`* and *`height`*.
The input region is always clipped to the extent of the output
image. If it is important that the distances within the entire
region should be computed, the region should be moved (see
[`MoveRegion`](move_region.md)) so that it has only positive coordinates and
the width and height of the output image should be large enough to
contain the region. The extent of the input region can be obtained
with [`SmallestRectangle1`](smallest_rectangle1.md).

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

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region for which the distance to the border is
computed.

**`distanceImage`** (output_object)  image `→` [HImage](HImage.md) (int4)

Image containing the distance information.

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of metric to be used for the distance
transformation.

Default:
"city-block"

List of values:
"chamfer-3-4", "chamfer-3-4-unnormalized", "chessboard", "city-block", "euclidean", "octagonal"

**`foreground`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Compute the distance for pixels
inside (*"true"*) or outside
(*"false"*) the input region.

Default:
"true"

List of values:
"false", "true"

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the output image.

Default:
640

Suggested values:
160, 192, 320, 384, 640, 768

Value range:
`1
≤
width`

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the output image.

Default:
480

Suggested values:
120, 144, 240, 288, 480, 576

Value range:
`1
≤
height`

## Example (HDevelop)

```
* Step towards extracting the medial axis of a shape:
gen_rectangle1 (Rectangle1, 0, 0, 200, 400)
gen_rectangle1 (Rectangle2, 200, 0, 400, 200)
union2 (Rectangle1, Rectangle2, Shape)
distance_transform (Shape, DistanceImage, 'chessboard', 'true', 640, 480)
```

## Complexity

The runtime complexity is O(*`width`***`height`*).

## Result

`DistanceTransform` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Possible Successors

`Threshold`

## Alternatives

`ClosestPointTransform`

## See also

`Skeleton`

## References

P. Soille: “Morphological Image Analysis, Principles and
Applications”; Springer Verlag Berlin Heidelberg New York,
1999.
  
G. Borgefors: “Distance Transformations in Arbitrary Dimensions”;
Computer Vision, Graphics, and Image Processing, Vol. 27, pages
321--345, 1984.
  
P.E. Danielsson: “Euclidean Distance Mapping”; Computer Graphics
and Image Processing, Vol. 14, pages 227--248, 1980.

## Module

Foundation
