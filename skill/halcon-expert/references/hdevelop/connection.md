# connection (Operator)

## Name

`connection` — Compute connected components of a region.

## Signature

`connection(Region : ConnectedRegions : : )`

## Description

`connection` determines the connected components of the
input regions given in *`Region`*. The neighborhood used for
this can be set via `set_system('neighborhood',<4/8>)`.
The default is 8-neighborhood, which is useful for determining the
connected components of the foreground. The maximum number of
connected components that is returned by `connection` can be
set via `set_system('max_connection',<Num>)`. The default
value of *0* causes all connected components to be returned.
The inverse operator of `connection` is [`union1`](union1.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Input region.

**`ConnectedRegions`** (output_object)  region-array `→` object

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

`connection` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`auto_threshold`,
`threshold`,
`dyn_threshold`,
`erosion1`

## Possible Successors

`select_shape`,
`select_gray`,
`shape_trans`,
`set_colored`,
`dilation1`,
`count_obj`,
`reduce_domain`,
`add_channels`

## Alternatives

`background_seg`

## See also

`set_system`,
`union1`

## Module

Foundation
