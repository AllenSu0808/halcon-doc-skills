# GenRegionPolygonXld (Operator)

## Name

`GenRegionPolygonXld` — Create a region from an XLD polygon.

## Signature

`static void HOperatorSet.GenRegionPolygonXld(HObject polygon, out HObject region, HTuple mode)`

`HRegion HXLDPoly.GenRegionPolygonXld(string mode)`

## Description

`GenRegionPolygonXld` creates a region *`region`* from a
subpixel XLD polygon *`polygon`*. The polygon is sampled
according to the Bresenham algorithm and influenced by the
parameter *"neighborhood"* of the operator [`SetSystem`](set_system.md). Open
polygons are closed before converting them to regions. Finally, the
parameter *`mode`* defines whether the region is filled up
(*"filled"*) or returned by its contour (*"margin"*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygon`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Input polygon(s).

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Created region(s).

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Fill mode of the region(s).

Default:
"filled"

Suggested values:
"filled", "margin"

## Possible Predecessors

`GenPolygonsXld`

## Alternatives

`GenRegionPolygon`,
`GenRegionContourXld`

## See also

`SetSystem`

## Module

Foundation
