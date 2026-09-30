# Connection (Operator)

## Name

`Connection` — Compute connected components of a region.

## Signature

`static void HOperatorSet.Connection(HObject region, out HObject connectedRegions)`

`HRegion HRegion.Connection()`

## Description

`Connection` determines the connected components of the
input regions given in *`region`*. The neighborhood used for
this can be set via `set_system('neighborhood',<4/8>)`.
The default is 8-neighborhood, which is useful for determining the
connected components of the foreground. The maximum number of
connected components that is returned by `Connection` can be
set via `set_system('max_connection',<Num>)`. The default
value of *0* causes all connected components to be returned.
The inverse operator of `Connection` is [`Union1`](union1.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region.

**`connectedRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Connected components.

## Example (HDevelop)

```
read_image(Image,'clip')
dev_set_colored(12)
threshold(Image,Dark,0,150)
count_obj(Dark,NumThresholded)
dev_display (Dark)
connection(Dark,ConnectedRegions)
count_obj(ConnectedRegions,NumConnected)
dev_display (ConnectedRegions)
```

## Complexity

Let F be the area of the input region and N be the number of
generated connected components. Then the runtime complexity is
O(sqrt(F) * sqrt(N)).

## Result

`Connection` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`AutoThreshold`,
`Threshold`,
`DynThreshold`,
`Erosion1`

## Possible Successors

`SelectShape`,
`SelectGray`,
`ShapeTrans`,
`SetColored`,
`Dilation1`,
`CountObj`,
`ReduceDomain`,
`AddChannels`

## Alternatives

`BackgroundSeg`

## See also

`SetSystem`,
`Union1`

## Module

Foundation
