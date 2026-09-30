# opening_seg (Operator)

## Name

`opening_seg` — Separate overlapping regions.

## Warning

**`opening_seg` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`opening_seg(Region, StructElement : RegionOpening : : )`

## Description

The `opening_seg` operation is defined as a sequence of
the following operators: [`erosion1`](erosion1.md),
[`connection`](connection.md) and [`dilation1`](dilation1.md) (see example).
Only one iteration is done in [`erosion1`](erosion1.md) and
[`dilation1`](dilation1.md).

`opening_seg` serves to separate overlapping regions whose
area of overlap is smaller than *`StructElement`*. It should
be noted that the resulting regions can overlap without actually
merging (see [`expand_region`](expand_region.md)). `opening_seg` uses the
center of gravity as the reference point of the structuring element.

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

**`RegionOpening`** (output_object)  region-array `→` object

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

`opening_seg` returns 2 (
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

`expand_region`,
`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`erosion1`,
`connection`,
`dilation1`

## Module

Foundation
