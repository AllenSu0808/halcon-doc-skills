# get_region_chain (Operator)

## Name

`get_region_chain` — Contour of an object as chain code.

## Warning

**`get_region_chain` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`get_region_chain(Region : : : Row, Column, Chain)`

## Description

The operator `get_region_chain` returns the contour of a region.
A contour is a series of
pixels describing the outline of the region.
The contour “lies on” the region.
It starts at the smallest line number;
in that line at the pixel with the largest column index.
The rotation occurs clockwise.
Holes of the region are ignored.
The direction code (chain code) is defined as follows:

3 2 1
4 * 0
5 6 7
The operator `get_region_chain` returns the code in the form of a tuple.
In case of an empty region the parameters *`Row`* and
*`Column`* are zero and *`Chain`* is the empty tuple.

## Attention

Holes of the region are ignored.
Only one region may be passed, and it must have exactly one
connection component.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

Region to be transformed.

**`Row`** (output_control)  chain.begin.y `→`  (integer)

Line of starting point.

**`Column`** (output_control)  chain.begin.x `→`  (integer)

Column of starting point.

**`Chain`** (output_control)  chain.code-array `→`  (integer)

Direction code of the contour (from starting point).

Value range:
`0
≤
Chain
≤
7`

## Result

The operator `get_region_chain` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one connection component is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
the operator `set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`sobel_amp`,
`threshold`,
`skeleton`,
`edges_image`,
`gen_rectangle1`,
`gen_circle`

## Possible Successors

`approx_chain`,
`approx_chain_simple`

## See also

`copy_obj`,
`get_region_contour`,
`get_region_polygon`

## Module

Foundation
