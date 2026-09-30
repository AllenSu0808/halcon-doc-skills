# closing_circle (Operator)

## Name

`closing_circle` — Close a region with a circular structuring element.

## Signature

`def closing_circle(region: HObject, radius: Union[float, int]) -> HObject`

## Description

`closing_circle` behaves analogously to
[`closing`](closing.md), i.e., the regions' boundaries are smoothed and
holes within a region which are smaller than the circular
structuring element of radius *`radius`* are closed. The
`closing_circle` operation is defined as a dilation
followed by a Minkowski subtraction, both with the same circular
structuring element.

## Attention

`closing_circle` is applied to each input region
separately. If gaps between different regions are to be closed,
[`union1`](union1.md) or [`union2`](union2.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be closed.

**`region_closing`** (output_object)  region(-array) `→` HObject

Closed regions.

**`radius`** (input_control)  real `→` Union[float, int]

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

`closing_circle` returns 2 (
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

`threshold`,
`regiongrowing`,
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`rank_region`,
`fill_up`,
`closing`

## See also

`dilation1`,
`minkowski_sub1`,
`erosion1`,
`opening`

## Module

Foundation
