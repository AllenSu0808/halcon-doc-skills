# QueryContourGlobalAttribsXld (Operator)

## Name

`QueryContourGlobalAttribsXld` — Return the names of the defined global attributes of an XLD contour.

## Signature

`static void HOperatorSet.QueryContourGlobalAttribsXld(HObject contour, out HTuple attribs)`

`HTuple HXLDCont.QueryContourGlobalAttribsXld()`

## Description

`QueryContourGlobalAttribsXld` returns the names of the
globally defined attributes that are set for an XLD *`contour`* in
*`attribs`*. Global attributes are additional values defined
for each contour, e.g., the normal vector of the regression line of
a contour (*"regr_norm_row"* and *"regr_norm_col"*).
Operators which define global attributes contain a description
of the name and semantics of the defined values.
The operator [`GetContourGlobalAttribXld`](get_contour_global_attrib_xld.md) can be used to access the
value of a particular attribute.

For an overview of the different global contour
attributes and the operators that add them to XLD contours see the operator
reference of [`GetContourGlobalAttribXld`](get_contour_global_attrib_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Input contour.

**`attribs`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

List of the defined global contour attributes.

## Possible Predecessors

`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## See also

`GetContourGlobalAttribXld`,
`GetContourAttribXld`,
`QueryContourAttribsXld`

## Module

Foundation
