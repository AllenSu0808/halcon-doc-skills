# area_holes (Operator)

## Name

`area_holes` — Compute the area of holes of regions.

## Signature

`area_holes(Regions : : : Area)`

## Description

The operator `area_holes` calculates the area of the holes in the
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

**`Regions`** (input_object)  region(-array) `→` object

Region(s) to be examined.

**`Area`** (output_control)  integer(-array) `→`  (integer)

Area(s) of holes of the region(s).

## Example (HDevelop)

```
read_image(Image,'modules/modules_01')
threshold(Image,Region,50,250)
area_holes(Region,Area)
```

## Result

The operator `area_holes` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## See also

`area_center`,
`fill_up`

## Module

Foundation
