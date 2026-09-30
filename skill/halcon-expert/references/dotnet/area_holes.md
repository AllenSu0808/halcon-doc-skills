# AreaHoles (Operator)

## Name

`AreaHoles` — Compute the area of holes of regions.

## Signature

`static void HOperatorSet.AreaHoles(HObject regions, out HTuple area)`

`HTuple HRegion.AreaHoles()`

## Description

The operator `AreaHoles` calculates the area of the holes in the
input regions. The area is defined as the number of pixels contained in the
holes. If a region has more than one hole the sum of the areas of all holes
in this region are returned. The neighborhood type is set via
`set_system('neighborhood',<4/8>)`
(default: 8-neighborhood).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the area of their holes.

If more than one region is passed the results are stored in tuples with
the index of a value in the tuple corresponding to the index of the
input region. In case of an empty region the area has the value 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be examined.

**`area`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Area(s) of holes of the region(s).

## Example (HDevelop)

```
read_image(Image,'modules/modules_01')
threshold(Image,Region,50,250)
area_holes(Region,Area)
```

## Result

The operator `AreaHoles` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## See also

`AreaCenter`,
`FillUp`

## Module

Foundation
