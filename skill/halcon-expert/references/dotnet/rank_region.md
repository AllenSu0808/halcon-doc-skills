# RankRegion (Operator)

## Name

`RankRegion` — Rank operator for regions.

## Signature

`static void HOperatorSet.RankRegion(HObject region, out HObject regionCount, HTuple width, HTuple height, HTuple number)`

`HRegion HRegion.RankRegion(int width, int height, int number)`

## Description

`RankRegion` calculates the binary rank operator. A filter
mask of size *`height`* x *`width`*) is used. In the
process, for each point in the region the number of points of
*`region`* lying within the filter mask are counted. If this
number is greater or equal to *`number`*, the current point
is added to the output region. If
$$Number = \frac{Height * Width}{2}$$ ![figure](../assets/06928eacc2181abc.svg)
is chosen, the median operator is obtained.

## Attention

For *`height`* and *`width`* only odd values > 3 are
valid. If invalid parameters are chosen they are converted
automatically (without raising an exception) to the next larger odd
values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be transformed.

**`regionCount`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Resulting region(s).

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21

Value range:
`3
≤
width
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`Width >= 3 && odd(Width)`

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21

Value range:
`3
≤
height
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`Height >= 3 && odd(Height)`

**`number`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum number of points lying within the filter mask.

Default:
70

Suggested values:
5, 10, 20, 40, 60, 80, 90, 120, 150, 200

Value range:
`1
≤
number
≤
1000` (lin)

Minimum increment:
1

Recommended increment:
10

Restriction:
`Number > 0`

## Example (HDevelop)

```
read_image(Image,'monkey')
mean_image(Image,Mean,5,5)
dyn_threshold(Image,Mean,Points,25,'light')
rank_region(Points,Textur,15,15,30)
gen_circle(Mask,10,10,3)
opening(Textur,Mask,Seg)
```

## Complexity

Let F be the area of the input region. Then the runtime
complexity is O(F * 8).

## Result

`RankRegion` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`,
`ClassNdimNorm`

## Possible Successors

`SelectShape`,
`DispRegion`

## Alternatives

`ClosingRectangle1`,
`ExpandRegion`

## See also

`RankImage`,
`MeanImage`

## Module

Foundation
