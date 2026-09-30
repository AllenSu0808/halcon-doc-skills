# ReconstructSurfaceStructuredLight (Operator)

## Name

`ReconstructSurfaceStructuredLight` — Reconstruct a surface from a decoded structured light setup.

## Signature

`static void HOperatorSet.ReconstructSurfaceStructuredLight(HTuple structuredLightModel, out HTuple objectModel3D)`

`void HObjectModel3D.ReconstructSurfaceStructuredLight(HStructuredLightModel structuredLightModel)`

`HObjectModel3D HStructuredLightModel.ReconstructSurfaceStructuredLight()`

## Description

`ReconstructSurfaceStructuredLight` reconstructs a surface from
a structured light setup. Prior to reconstruction,
for every projected pattern image, a camera image of the projection
on the surface is acquired.
For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).
The reconstructed surface is stored in the handle *`objectModel3D`*.

Reconstruction is possible for non-specular surfaces, using a projector
projecting light like an 'inverse camera'. In
[`CreateStructuredLightModel`](create_structured_light_model.md), the type of the model must have been
set to *"3d_reconstruction"*.

The reconstruction process uses the vertical decoded correspondence between
projector coordinates lighting the camera coordinates, as well as
calibration information:

[`DecodeStructuredLightPattern`](decode_structured_light_pattern.md) must be called before
`ReconstructSurfaceStructuredLight`, storing the correspondence image
between the projector coordinates and the camera coordinates
in the model *`structuredLightModel`*, i. e. for
each camera pixel which projector pixel lighted (i.e. encoded) the observed
point on the surface.
`ReconstructSurfaceStructuredLight` uses the vertical correspondence
image, so the parameter *"pattern_orientation"* of
[`SetStructuredLightModelParam`](set_structured_light_model_param.md) must have been set to
*"vertical"* or *"both"*. Note that in most cases
*"vertical"* should be chosen for speed, since fewer images are
necessary than for *"both"*.

For setting the calibration information, please refer to the parameter
*"camera_setup_model"* of [`SetStructuredLightModelParam`](set_structured_light_model_param.md).

The reconstruction is performed only within the domain of the correspondence
image. Reducing the domain of the input images of
[`DecodeStructuredLightPattern`](decode_structured_light_pattern.md) (e.g., with [`ReduceDomain`](reduce_domain.md))
can be used to obtain a reduced reconstructed surface, i. e. for shorter
runtime or to reduce noise.
The resulting *`objectModel3D`* contains a mapping, so the
coordinate images can be obtained by [`ObjectModel3dToXyz`](object_model_3d_to_xyz.md) using
*"from_xyz_map"*.
Pixels for which no reconstruction was possible are excluded from its domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`structuredLightModel`** (input_control)  structured_light_model `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the structured light model.

**`objectModel3D`** (output_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

## Example (HDevelop)

```
* Set the calibration information
set_structured_light_model_param (StructuredLightModel, \
                                  'camera_setup_model', CameraSetupModelID)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
* Reconstruct the surface
reconstruct_surface_structured_light (StructuredLightModel, ObjectModel3D)
```

## Result

The operator `ReconstructSurfaceStructuredLight` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`DecodeStructuredLightPattern`

## Possible Successors

`ObjectModel3dToXyz`

## See also

`CreateStructuredLightModel`,
`SetStructuredLightModelParam`

## Module

3D Metrology
