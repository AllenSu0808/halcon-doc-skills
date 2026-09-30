# get_region_thickness (Operator)

## Name

`get_region_thickness` — Access the thickness of a region along the main axis.

## Signature

`def get_region_thickness(region: HObject) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `get_region_thickness` calculates the thickness of the
regions along the main axis (see [`elliptic_axis`](elliptic_axis.md))
for each pixel of the section. The thickness at one point on the main axis
is defined as the distance between the intersections of the contour with
the plumb on the main axis in the respective point which are the furthest
apart.
Additionally the operator `get_region_thickness` returns the
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

**`region`** (input_object)  region `→` HObject

Region to be analyzed.

**`thickness`** (output_control)  integer-array `→` Sequence[int]

Thickness of the region along its main axis.

**`histogramm`** (output_control)  integer-array `→` Sequence[int]

Histogram of the thickness of the region along
its main axis.

## Result

The operator `get_region_thickness` returns the value 2 (
H_MSG_TRUE)
if exactly one region is passed.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`sobel_amp`,
`threshold`,
`connection`,
`select_shape`,
`select_obj`

## See also

`copy_obj`,
`elliptic_axis`

## Module

Foundation
