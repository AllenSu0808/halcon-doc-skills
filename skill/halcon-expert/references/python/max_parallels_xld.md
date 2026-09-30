# max_parallels_xld (Operator)

## Name

`max_parallels_xld` — Join modified XLD parallels lying on the same polygon.

## Signature

`def max_parallels_xld(ext_parallels: HObject) -> HObject`

## Description

`max_parallels_xld` joins all modified XLD parallels in
*`ext_parallels`* into a polygon if they lie on the same
original polygon segment. This means that polygons exhibiting
parallelism and enclosing homogeneous areas in several places are
joined into one long polygon (from the first parallel line to the
last parallel line). The resulting polygons are returned in
*`max_polygons`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ext_parallels`** (input_object)  xld_ext_para-array `→` HObject

Extended XLD parallels.

**`max_polygons`** (output_object)  xld_poly-array `→` HObject

Maximally extended parallels.

## Possible Predecessors

`mod_parallels_xld`

## Possible Successors

`get_polygon_xld`,
`get_lines_xld`

## Module

Foundation
