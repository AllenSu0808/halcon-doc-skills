# query_contour_attribs_xld (Operator)

## Name

`query_contour_attribs_xld` — Return the names of the defined attributes of an XLD contour.

## Signature

`def query_contour_attribs_xld(contour: HObject) -> Sequence[str]`

## Description

`query_contour_attribs_xld` returns the names of the
defined attributes of an XLD contour *`contour`* in
*`attribs`*. Attributes are additional values defined for
each contour point, e.g., the direction perpendicular to the contour
(*"angle"*). Operators which define contour point attributes contain
a description of the name and semantics of the defined values.
The operator [`get_contour_attrib_xld`](get_contour_attrib_xld.md) can be used to access the
values of a particular attribute.

For an overview of the different contour point
attributes and the operators that add them to XLD contours see the operator
reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input contour.

**`attribs`** (output_control)  string-array `→` Sequence[str]

List of the defined contour attributes.

## Possible Predecessors

`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## See also

`get_contour_attrib_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`

## Module

Foundation
