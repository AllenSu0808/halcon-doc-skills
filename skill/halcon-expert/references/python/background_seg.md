# background_seg (Operator)

## Name

`background_seg` — Determine the connected components of the background of given regions.

## Signature

`def background_seg(foreground: HObject) -> HObject`

## Description

`background_seg` determines connected components of the
background of the foreground regions given in *`foreground`*.
This operator is normally used after an edge operator in order to
determine the regions enclosed by the extracted edges. The
connected components are determined using 4-neighborhood.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`foreground`** (input_object)  region(-array) `→` HObject

Input regions.

**`background_regions`** (output_object)  region-array `→` HObject

Connected components of the background.

## Complexity

Let F be the area of the background, H and W be the height and
width of the image, and N be the number of resulting regions.
Then the runtime complexity is O(H + sqrt(F) * sqrt(N)).

## Result

`background_seg` always returns the value 2 (
H_MSG_TRUE)
. The
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

`select_shape`

## Alternatives

`complement`,
`connection`

## See also

`threshold`,
`hysteresis_threshold`,
`skeleton`,
`expand_region`,
`set_system`,
`sobel_amp`,
`edges_image`,
`roberts`,
`bandpass_image`

## Module

Foundation
