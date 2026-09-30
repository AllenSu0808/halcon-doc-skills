# OpeningSeg (Operator)

## Name

`OpeningSeg` — Separate overlapping regions.

## Warning

**`OpeningSeg` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.OpeningSeg(HObject region, HObject structElement, out HObject regionOpening)`

`HRegion HRegion.OpeningSeg(HRegion structElement)`

## Description

The `OpeningSeg` operation is defined as a sequence of
the following operators: [`Erosion1`](erosion1.md),
[`Connection`](connection.md) and [`Dilation1`](dilation1.md) (see example).
Only one iteration is done in [`Erosion1`](erosion1.md) and
[`Dilation1`](dilation1.md).

`OpeningSeg` serves to separate overlapping regions whose
area of overlap is smaller than *`structElement`*. It should
be noted that the resulting regions can overlap without actually
merging (see [`ExpandRegion`](expand_region.md)). `OpeningSeg` uses the
center of gravity as the reference point of the structuring element.

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

**`regionOpening`** (output_object)  region-array `→` [HRegion](HRegion.md)

Opened regions.

## Example (HDevelop)

```
* Simulation of opening_seg
* opening_seg(Region,StructElement,RegionOpening):
    erosion1(Region,StructElement,H1,1)
    connection(H1,H2)
    dilation1(H2,StructElement,RegionOpening,1)
```

## Complexity

Let F1 be the area of the input region, and F2 be the area of
the structuring element. Then the runtime complexity for one region
is:
$$O\left(\sqrt{F1} \cdot \sqrt{F2} \cdot \sqrt{\sqrt{F1}}\right) .$$ ![figure](../assets/253138a7fe1d487f.svg)

## Result

`OpeningSeg` returns 2 (
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

`ExpandRegion`,
`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Erosion1`,
`Connection`,
`Dilation1`

## Module

Foundation
