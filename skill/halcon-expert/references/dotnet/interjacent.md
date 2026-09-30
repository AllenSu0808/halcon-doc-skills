# Interjacent (Operator)

## Name

`Interjacent` — Partition the image plane using given regions.

## Warning

**`Interjacent` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.Interjacent(HObject region, out HObject regionInterjacent, HTuple mode)`

`HRegion HRegion.Interjacent(string mode)`

## Description

`Interjacent` partitions the image plane using the regions
given in *`region`*. The result is a region containing the
extracted separating lines. The following modes of operation can be
used:

- ***"medial_axis"*** —

  This mode is used for regions that do not touch or overlap.
  The operator will find separating lines between the regions
  which partition the background evenly between the input
  regions. This corresponds to the following calls:

  - **Example:** —

    `complement('full',Region,Tmp)`

    `skeleton(Tmp,Result)`
- ***"border"*** —

  If the input regions do not touch or overlap this mode is
  equivalent to `boundary(Region,Result)`, i.e., it
  replaces each region by its boundary. If regions are touching
  they are aggregated into one region. The corresponding output
  region then contains the boundary of the aggregated region, as
  well as the one pixel wide separating line between the
  original regions. This corresponds to the following calls:

  - **Example:** —

    `boundary(Region,Tmp1,'inner')`

    `union1(Tmp1,Tmp2)`

    `skeleton(Tmp2,Result)`
- ***"mixed"*** —

  In this mode the operator behaves like the mode *"medial_axis"*
  for non-overlapping regions. If regions touch or overlap,
  again separating lines between the input regions are generated
  on output, but this time including the “touching line”
  between regions, i.e., touching regions are separated by a
  line in the output region. This corresponds to the following
  calls:

  - **Example:** —

    `erosion1(Region,Mask,Tmp1,1)`

    `union1(Tmp1,Tmp2)`

    `complement(full,Tmp2,Tmp3)`

    `skeleton(Tmp3,Result)`

  where Mask denotes the following “cross mask”:
  ![figure](../assets/2523cea1067b8be5.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions for which the separating lines are to be
determined.

**`regionInterjacent`** (output_object)  region `→` [HRegion](HRegion.md)

Output region containing the separating lines.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of operation.

Default:
"mixed"

List of values:
"border", "medial_axis", "mixed"

## Example (HDevelop)

```
read_image(Image,'forest_air1')
mean_image(Image,Mean,31,31)
dyn_threshold(Image,Mean,Seg,20,'light')
interjacent(Seg,Graph,'medial_axis')
dev_display(Graph)
```

## Result

`Interjacent` always returns the value 2 (
H_MSG_TRUE)
. The behavior
in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## See also

`ExpandRegion`,
`JunctionsSkeleton`,
`Boundary`

## Module

Foundation
