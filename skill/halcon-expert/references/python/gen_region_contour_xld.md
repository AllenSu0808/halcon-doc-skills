# gen_region_contour_xld (Operator)

## Name

`gen_region_contour_xld` — Create a region from an XLD contour.

## Signature

`def gen_region_contour_xld(contour: HObject, mode: str) -> HObject`

## Description

`gen_region_contour_xld` creates a region *`region`* from a
subpixel XLD contour *`contour`*. The contour is sampled
according to the Bresenham algorithm and influenced by the parameter
*"neighborhood"* of the operator [`set_system`](set_system.md). Open contours
are closed before converting them to regions. Finally, the parameter
*`mode`* defines whether the region is filled up (*"filled"*)
or returned by its contour (*"margin"*).

Please note that the coordinates of the contour points are rounded
to their nearest integer pixel coordinates during the conversion.
This may lead to unexpected results when passing the contour
obtained by the operator [`gen_contour_region_xld`](gen_contour_region_xld.md) to
`gen_region_contour_xld`: When setting `mode` of
[`gen_contour_region_xld`](gen_contour_region_xld.md) to *"border"*, the input region
of [`gen_contour_region_xld`](gen_contour_region_xld.md) and the output region of
`gen_region_contour_xld` differ. For example, let us assume
that the input region of [`gen_contour_region_xld`](gen_contour_region_xld.md) consists of
the single pixel (1,1). Then, the resulting contour that is
obtained when calling [`gen_contour_region_xld`](gen_contour_region_xld.md) with
`mode` set to *"border"* consists of the five points
(0.5,0.5), (0.5,1.5), (1.5,1.5), (1.5,0.5), and (0.5,0.5).
Consequently, when passing this contour again to
`gen_region_contour_xld`, the resulting region consists of the
points (1,1), (1,2), (2,2), and (2,1).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` HObject

Input contour(s).

**`region`** (output_object)  region(-array) `→` HObject

Created region(s).

**`mode`** (input_control)  string `→` str

Fill mode of the region(s).

Default:
"filled"

Suggested values:
"filled", "margin"

## Possible Predecessors

`gen_contour_polygon_xld`,
`gen_contour_polygon_rounded_xld`

## Alternatives

`gen_region_polygon`,
`gen_region_polygon_xld`

## See also

`set_system`

## Module

Foundation
