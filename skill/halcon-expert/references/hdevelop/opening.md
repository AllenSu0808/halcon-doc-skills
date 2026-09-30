# opening (Operator)

## Name

`opening` — Open a region.

## Signature

`opening(Region, StructElement : RegionOpening : : )`

## Description

An `opening` operation is defined as an erosion followed
by a Minkowski addition. By applying `opening` to a
region, larger structures remain mostly intact, while small
structures like lines or points are eliminated. In contrast, a
[`closing`](closing.md) operation results in small gaps being retained
or filled up (see [`closing`](closing.md)).

`opening` serves to eliminate small regions (smaller than
*`StructElement`*) and to smooth the boundaries of a region.
The position of *`StructElement`* is meaningless, since an
opening operation is invariant with respect to the choice of the
reference point.

Structuring elements (*`StructElement`*) can be generated
with operators such as [`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md),
[`gen_rectangle2`](gen_rectangle2.md), [`gen_ellipse`](gen_ellipse.md),
[`draw_region`](draw_region.md), [`gen_region_polygon`](gen_region_polygon.md),
[`gen_region_points`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be opened.

**`StructElement`** (input_object)  region `→` object

Structuring element (position-invariant).

**`RegionOpening`** (output_object)  region(-array) `→` object

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

`opening` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`draw_region`,
`gen_region_points`,
`gen_region_polygon_filled`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`minkowski_add1`,
`erosion1`,
`opening_circle`

## See also

`gen_circle`,
`gen_rectangle2`,
`gen_region_polygon`

## Module

Foundation
