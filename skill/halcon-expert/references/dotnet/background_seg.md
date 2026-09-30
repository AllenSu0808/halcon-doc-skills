# BackgroundSeg (Operator)

## Name

`BackgroundSeg` — Determine the connected components of the background of given regions.

## Signature

`static void HOperatorSet.BackgroundSeg(HObject foreground, out HObject backgroundRegions)`

`HRegion HRegion.BackgroundSeg()`

## Description

`BackgroundSeg` determines connected components of the
background of the foreground regions given in *`foreground`*.
This operator is normally used after an edge operator in order to
determine the regions enclosed by the extracted edges. The
connected components are determined using 4-neighborhood.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`foreground`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions.

**`backgroundRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Connected components of the background.

## Example (HDevelop)

```
* Simulation of background_seg:
background_seg(Foreground,BackgroundRegions)
  complement(Foreground,Background)
  get_system('neighborhood',Save)
  set_system('neighborhood',4)
  connection(Background,BackgroundRegions)
  set_system('neighborhood',Save)

* Segmentation with edge filter:
read_image(Image,'fabrik')
sobel_dir(Image,Sobel,Dir,'sum_sqrt',3)
threshold(Sobel,Edges,20,255)
skeleton(Edges,Margins)
background_seg(Margins,Regions)
```

## Complexity

Let F be the area of the background, H and W be the height and
width of the image, and N be the number of resulting regions.
Then the runtime complexity is O(H + sqrt(F) * sqrt(N)).

## Result

`BackgroundSeg` always returns the value 2 (
H_MSG_TRUE)
. The
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

`SelectShape`

## Alternatives

`Complement`,
`Connection`

## See also

`Threshold`,
`HysteresisThreshold`,
`Skeleton`,
`ExpandRegion`,
`SetSystem`,
`SobelAmp`,
`EdgesImage`,
`Roberts`,
`BandpassImage`

## Module

Foundation
