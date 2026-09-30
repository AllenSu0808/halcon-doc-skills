# fill_up_shape (Operator)

## Name

`fill_up_shape` — Fill up holes in regions having given shape features.

## Signature

`fill_up_shape(Region : RegionFillUp : Feature, Min, Max : )`

## Description

`fill_up_shape` fills up those holes in the input region
*`Region`* having given shape features. The parameter
*`Feature`* determines the shape feature to be used, while
*`Min`* and *`Max`* determine the range the shape
feature has to lie in in order for the hole to be filled up.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Input region(s).

**`RegionFillUp`** (output_object)  region(-array) `→` object

Output region(s) with filled holes.

**`Feature`** (input_control)  string `→`  (string)

Shape feature used.

Default:
'area'

List of values:
'anisometry', 'area', 'compactness', 'convexity', 'inner_circle', 'outer_circle', 'phi', 'ra', 'rb'

**`Min`** (input_control)  number `→`  (real / integer)

Minimum value for Feature.

Default:
1.0

Suggested values:
0.0, 1.0, 10.0, 50.0, 100.0, 500.0, 1000.0, 10000.0

Value range:
`0.0
≤
Min`

**`Max`** (input_control)  number `→`  (real / integer)

Maximum value for Feature.

Default:
100.0

Suggested values:
10.0, 50.0, 100.0, 500.0, 1000.0, 10000.0, 100000.0

Value range:
`0.0
≤
Max`

## Example (C)

```
read_image(&Image,"monkey");
threshold(Image,&Seg,120.0,255.0);
fill_up_shape(Seg,&Filled,"area",0.0,200.0);
```

## Result

`fill_up_shape` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## Alternatives

`fill_up`

## See also

`select_shape`,
`connection`,
`area_center`

## Module

Foundation
