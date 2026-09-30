# rank_region (Operator)

## Name

`rank_region` — Rank operator for regions.

## Signature

`rank_region(Region : RegionCount : Width, Height, Number : )`

## Description

`rank_region` calculates the binary rank operator. A filter
mask of size *`Height`* x *`Width`*) is used. In the
process, for each point in the region the number of points of
*`Region`* lying within the filter mask are counted. If this
number is greater or equal to *`Number`*, the current point
is added to the output region. If
$$Number = \frac{Height * Width}{2}$$ ![figure](../assets/06928eacc2181abc.svg)
is chosen, the median operator is obtained.

## Attention

For *`Height`* and *`Width`* only odd values > 3 are
valid. If invalid parameters are chosen they are converted
automatically (without raising an exception) to the next larger odd
values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region(s) to be transformed.

**`RegionCount`** (output_object)  region(-array) `→` object

Resulting region(s).

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21

Value range:
`3
≤
Width
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`Width >= 3 && odd(Width)`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the filter mask.

Default:
15

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21

Value range:
`3
≤
Height
≤
511` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`Height >= 3 && odd(Height)`

**`Number`** (input_control)  integer `→`  (integer)

Minimum number of points lying within the filter mask.

Default:
70

Suggested values:
5, 10, 20, 40, 60, 80, 90, 120, 150, 200

Value range:
`1
≤
Number
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

`rank_region` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`,
`class_ndim_norm`

## Possible Successors

`select_shape`,
`disp_region`

## Alternatives

`closing_rectangle1`,
`expand_region`

## See also

`rank_image`,
`mean_image`

## Module

Foundation
