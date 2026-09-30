# FillUpShape (Operator)

## Name

`FillUpShape` — Fill up holes in regions having given shape features.

## Signature

`static void HOperatorSet.FillUpShape(HObject region, out HObject regionFillUp, HTuple feature, HTuple min, HTuple max)`

`HRegion HRegion.FillUpShape(string feature, HTuple min, HTuple max)`

`HRegion HRegion.FillUpShape(string feature, double min, double max)`

## Description

`FillUpShape` fills up those holes in the input region
*`region`* having given shape features. The parameter
*`feature`* determines the shape feature to be used, while
*`min`* and *`max`* determine the range the shape
feature has to lie in in order for the hole to be filled up.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region(s).

**`regionFillUp`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Output region(s) with filled holes.

**`feature`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Shape feature used.

Default:
"area"

List of values:
"anisometry", "area", "compactness", "convexity", "inner_circle", "outer_circle", "phi", "ra", "rb"

**`min`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum value for Feature.

Default:
1.0

Suggested values:
0.0, 1.0, 10.0, 50.0, 100.0, 500.0, 1000.0, 10000.0

Value range:
`0.0
≤
min`

**`max`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum value for Feature.

Default:
100.0

Suggested values:
10.0, 50.0, 100.0, 500.0, 1000.0, 10000.0, 100000.0

Value range:
`0.0
≤
max`

## Example (C)

```
read_image(&Image,"monkey");
threshold(Image,&Seg,120.0,255.0);
fill_up_shape(Seg,&Filled,"area",0.0,200.0);
```

## Result

`FillUpShape` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## Alternatives

`FillUp`

## See also

`SelectShape`,
`Connection`,
`AreaCenter`

## Module

Foundation
