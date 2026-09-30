# GetRegionThickness (Operator)

## Name

`GetRegionThickness` — Access the thickness of a region along the main axis.

## Signature

`static void HOperatorSet.GetRegionThickness(HObject region, out HTuple thickness, out HTuple histogramm)`

`HTuple HRegion.GetRegionThickness(out HTuple histogramm)`

## Description

The operator `GetRegionThickness` calculates the thickness of the
regions along the main axis (see [`EllipticAxis`](elliptic_axis.md))
for each pixel of the section. The thickness at one point on the main axis
is defined as the distance between the intersections of the contour with
the plumb on the main axis in the respective point which are the furthest
apart.
Additionally the operator `GetRegionThickness` returns the
*`histogramm`*
of the thicknesses of the region.
The length of the histogram corresponds to the largest
occurring thickness in the observed region.

## Attention

Only one region may be passed. If the region has several connection
components, only the first one is investigated. All other components
are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Region to be analyzed.

**`thickness`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Thickness of the region along its main axis.

**`histogramm`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Histogram of the thickness of the region along
its main axis.

## Result

The operator `GetRegionThickness` returns the value 2 (
H_MSG_TRUE)
if exactly one region is passed.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`SobelAmp`,
`Threshold`,
`Connection`,
`SelectShape`,
`SelectObj`

## See also

`CopyObj`,
`EllipticAxis`

## Module

Foundation
