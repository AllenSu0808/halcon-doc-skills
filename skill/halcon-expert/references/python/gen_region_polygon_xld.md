# gen_region_polygon_xld (Operator)

## Name

`gen_region_polygon_xld` — Create a region from an XLD polygon.

## Signature

`def gen_region_polygon_xld(polygon: HObject, mode: str) -> HObject`

## Description

`gen_region_polygon_xld` creates a region *`region`* from a
subpixel XLD polygon *`polygon`*. The polygon is sampled
according to the Bresenham algorithm and influenced by the
parameter *"neighborhood"* of the operator [`set_system`](set_system.md). Open
polygons are closed before converting them to regions. Finally, the
parameter *`mode`* defines whether the region is filled up
(*"filled"*) or returned by its contour (*"margin"*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygon`** (input_object)  xld_poly(-array) `→` HObject

Input polygon(s).

**`region`** (output_object)  region(-array) `→` HObject

Created region(s).

**`mode`** (input_control)  string `→` str

Fill mode of the region(s).

Default:
"filled"

Suggested values:
"filled", "margin"

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`gen_region_polygon`,
`gen_region_contour_xld`

## See also

`set_system`

## Module

Foundation
