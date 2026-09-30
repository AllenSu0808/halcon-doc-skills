# Opening (Operator)

## Name

`Opening` — Open a region.

## Signature

`static void HOperatorSet.Opening(HObject region, HObject structElement, out HObject regionOpening)`

`HRegion HRegion.Opening(HRegion structElement)`

## Description

An `Opening` operation is defined as an erosion followed
by a Minkowski addition. By applying `Opening` to a
region, larger structures remain mostly intact, while small
structures like lines or points are eliminated. In contrast, a
[`Closing`](closing.md) operation results in small gaps being retained
or filled up (see [`Closing`](closing.md)).

`Opening` serves to eliminate small regions (smaller than
*`structElement`*) and to smooth the boundaries of a region.
The position of *`structElement`* is meaningless, since an
opening operation is invariant with respect to the choice of the
reference point.

Structuring elements (*`structElement`*) can be generated
with operators such as [`GenCircle`](gen_circle.md), [`GenRectangle1`](gen_rectangle1.md),
[`GenRectangle2`](gen_rectangle2.md), [`GenEllipse`](gen_ellipse.md),
[`DrawRegion`](draw_region.md), [`GenRegionPolygon`](gen_region_polygon.md),
[`GenRegionPoints`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be opened.

**`structElement`** (input_object)  region `→` [HRegion](HRegion.md)

Structuring element (position-invariant).

**`regionOpening`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Opened regions.

## Example (HDevelop)

```
* Large regions in an aerial picture (beech trees or meadows):
read_image(Image,'forest_road')
threshold(Image,Light,160,255)
gen_circle(StructElement,100,100,10)
* selecting the large regions
opening(Light,StructElement,Large)
* Selecting of edges with certain orientation:
read_image(Image,'fabrik')
sobel_amp(Image,Sobel,'sum_abs',3)
threshold(Sobel,Edges,10,255)
gen_rectangle2(StructElement,100,100,3.07819,20,1)
opening(Edges,StructElement,Direction)
```

## Complexity

Let F1 be the area of the input region, and F2 be the area of
the structuring element. Then the runtime complexity for one region
is:
$$O\left(2\cdot \sqrt{F1}\cdot \sqrt{F2}\right)\,.$$ ![figure](../assets/df053ef6aed1f7b1.svg)

## Result

`Opening` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`DrawRegion`,
`GenRegionPoints`,
`GenRegionPolygonFilled`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`MinkowskiAdd1`,
`Erosion1`,
`OpeningCircle`

## See also

`GenCircle`,
`GenRectangle2`,
`GenRegionPolygon`

## Module

Foundation
