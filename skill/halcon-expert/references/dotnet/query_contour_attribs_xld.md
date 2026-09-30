# QueryContourAttribsXld (Operator)

## Name

`QueryContourAttribsXld` — Return the names of the defined attributes of an XLD contour.

## Signature

`static void HOperatorSet.QueryContourAttribsXld(HObject contour, out HTuple attribs)`

`HTuple HXLDCont.QueryContourAttribsXld()`

## Description

`QueryContourAttribsXld` returns the names of the
defined attributes of an XLD contour *`contour`* in
*`attribs`*. Attributes are additional values defined for
each contour point, e.g., the direction perpendicular to the contour
(*"angle"*). Operators which define contour point attributes contain
a description of the name and semantics of the defined values.
The operator [`GetContourAttribXld`](get_contour_attrib_xld.md) can be used to access the
values of a particular attribute.

For an overview of the different contour point
attributes and the operators that add them to XLD contours see the operator
reference of [`GetContourAttribXld`](get_contour_attrib_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Input contour.

**`attribs`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

List of the defined contour attributes.

## Possible Predecessors

`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## See also

`GetContourAttribXld`,
`GetContourGlobalAttribXld`,
`QueryContourGlobalAttribsXld`

## Module

Foundation
