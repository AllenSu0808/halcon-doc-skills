# XyzToObjectModel3d (Operator)

## Name

`XyzToObjectModel3d` — Transform 3D points from images to a 3D object model.

## Signature

`static void HOperatorSet.XyzToObjectModel3d(HObject x, HObject y, HObject z, out HTuple objectModel3D)`

`public HObjectModel3D(HImage x, HImage y, HImage z)`

`void HObjectModel3D.XyzToObjectModel3d(HImage x, HImage y, HImage z)`

## Description

The operator `XyzToObjectModel3d` transforms an image triple
that contains the X, Y, and Z-coordinates of 3D points to a 3D object model.
Thereby, only points in the intersecting domains of all three images are
used and the images need to be of same size.
The size of these images can be queried from the model by
[`GetObjectModel3dParams`](get_object_model_3d_params.md) with *"mapping_size"*.
The handle of the created 3D object model is returned in
*`objectModel3D`*.
The created 3D object model contains the coordinates of the points, as well
as a mapping attribute that contains the original row and column of each
3D point.
Points where one of the coordinates is infinity or "Not a Number" (NaN)
are ignored and not added to the 3D object model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`x`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Image with the X-Coordinates and the ROI of the 3D points.

**`y`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Image with the Y-Coordinates of the 3D points.

**`z`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (real)

Image with the Z-Coordinates of the 3D points.

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

## Result

The operator `XyzToObjectModel3d` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct. Otherwise, an exception
will be raised.

## Possible Predecessors

`DisparityImageToXyz`,
`GetSheetOfLightResult`

## Alternatives

`GenObjectModel3dFromPoints`,
`GetSheetOfLightResultObjectModel3d`

## See also

`ReadObjectModel3d`

## Module

3D Metrology
