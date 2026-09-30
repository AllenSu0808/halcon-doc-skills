# ClosingCircle (Operator)

## Name

`ClosingCircle` — Close a region with a circular structuring element.

## Signature

`static void HOperatorSet.ClosingCircle(HObject region, out HObject regionClosing, HTuple radius)`

`HRegion HRegion.ClosingCircle(HTuple radius)`

`HRegion HRegion.ClosingCircle(double radius)`

## Description

`ClosingCircle` behaves analogously to
[`Closing`](closing.md), i.e., the regions' boundaries are smoothed and
holes within a region which are smaller than the circular
structuring element of radius *`radius`* are closed. The
`ClosingCircle` operation is defined as a dilation
followed by a Minkowski subtraction, both with the same circular
structuring element.

## Attention

`ClosingCircle` is applied to each input region
separately. If gaps between different regions are to be closed,
[`Union1`](union1.md) or [`Union2`](union2.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be closed.

**`regionClosing`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Closed regions.

**`radius`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circular structuring element.

Default:
3.5

Suggested values:
1.5, 2.5, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5, 19.5, 25.5, 33.5, 45.5, 60.5, 110.5

Value range:
`0.5
≤
radius
≤
511.5` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

## Example (C)

```
my_closing_circle(Hobject In, double Radius, Hobject *Out)
{
  Hobject  tmp, StructElement;
  gen_circle(StructElement,100.0,100.0,Radius);
  dilation1(In,StructElement,&tmp,1);
  minkowski_sub1(tmp,StructElement,Out,1);
}
```

## Complexity

Let F1 be the area of the input region. Then the runtime
complexity for one region is:
$$O\left(4 \cdot \sqrt{F1} \cdot Radius\right) .$$ ![figure](../assets/c413264716510879.svg)

## Result

`ClosingCircle` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

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
`ClassNdimNorm`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`RankRegion`,
`FillUp`,
`Closing`

## See also

`Dilation1`,
`MinkowskiSub1`,
`Erosion1`,
`Opening`

## Module

Foundation
