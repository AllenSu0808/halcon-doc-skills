# GetObjClass (Operator)

## Name

`GetObjClass` — Name of the class of an image object.

## Signature

`static void HOperatorSet.GetObjClass(HObject objectVal, out HTuple classVal)`

`HTuple HObject.GetObjClass()`

## Description

`GetObjClass` returns
the name of the corresponding class to each object.
The following classes are possible:

- **'image'** —

  Object with region (definition domain) and at least one channel.
- **'region'** —

  Object with a region without gray values.
- **'xld_cont'** —

  XLD object as contour
- **'xld_poly'** —

  XLD object as polygon
- **'xld_parallel'** —

  XLD object with parallel polygons

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (input_object)  object(-array) `→` [HObject](HObject.md)

Image objects to be examined.

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of class.

## Result

If the parameter values are correct the operator `GetObjClass`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Successors

`DispImage`,
`DispRegion`,
`DispXld`

## See also

`GetChannelInfo`,
`CountRelation`

## Module

Foundation
