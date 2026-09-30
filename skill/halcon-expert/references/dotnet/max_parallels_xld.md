# MaxParallelsXld (Operator)

## Name

`MaxParallelsXld` — Join modified XLD parallels lying on the same polygon.

## Signature

`static void HOperatorSet.MaxParallelsXld(HObject extParallels, out HObject maxPolygons)`

`HXLDPoly HXLDExtPara.MaxParallelsXld()`

## Description

`MaxParallelsXld` joins all modified XLD parallels in
*`extParallels`* into a polygon if they lie on the same
original polygon segment. This means that polygons exhibiting
parallelism and enclosing homogeneous areas in several places are
joined into one long polygon (from the first parallel line to the
last parallel line). The resulting polygons are returned in
*`maxPolygons`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`extParallels`** (input_object)  xld_ext_para-array `→` [HXLDExtPara](HXLDExtPara.md)

Extended XLD parallels.

**`maxPolygons`** (output_object)  xld_poly-array `→` [HXLDPoly](HXLDPoly.md)

Maximally extended parallels.

## Possible Predecessors

`ModParallelsXld`

## Possible Successors

`GetPolygonXld`,
`GetLinesXld`

## Module

Foundation
