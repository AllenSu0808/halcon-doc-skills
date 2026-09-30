# gen_region_polygon_xld (Operator)

## Name

`gen_region_polygon_xld` — Create a region from an XLD polygon.

## Signature

`gen_region_polygon_xld(Polygon : Region : Mode : )`

## Description

`gen_region_polygon_xld` creates a region *`Region`* from a
subpixel XLD polygon *`Polygon`*. The polygon is sampled
according to the Bresenham algorithm and influenced by the
parameter *'neighborhood'* of the operator [`set_system`](set_system.md). Open
polygons are closed before converting them to regions. Finally, the
parameter *`Mode`* defines whether the region is filled up
(*'filled'*) or returned by its contour (*'margin'*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Polygon`** (input_object)  xld_poly(-array) `→` object

Input polygon(s).

**`Region`** (output_object)  region(-array) `→` object

Created region(s).

**`Mode`** (input_control)  string `→`  (string)

Fill mode of the region(s).

Default:
'filled'

Suggested values:
'filled', 'margin'

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`gen_region_polygon`,
`gen_region_contour_xld`

## See also

`set_system`

## Module

Foundation
