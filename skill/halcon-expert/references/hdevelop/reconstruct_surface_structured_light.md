# reconstruct_surface_structured_light (Operator)

## Name

`reconstruct_surface_structured_light` — Reconstruct a surface from a decoded structured light setup.

## Signature

`reconstruct_surface_structured_light( : : StructuredLightModel : ObjectModel3D)`

## Description

`reconstruct_surface_structured_light` reconstructs a surface from
a structured light setup. Prior to reconstruction,
for every projected pattern image, a camera image of the projection
on the surface is acquired.
For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).
The reconstructed surface is stored in the handle *`ObjectModel3D`*.

Reconstruction is possible for non-specular surfaces, using a projector
projecting light like an 'inverse camera'. In
[`create_structured_light_model`](create_structured_light_model.md), the type of the model must have been
set to *'3d_reconstruction'*.

The reconstruction process uses the vertical decoded correspondence between
projector coordinates lighting the camera coordinates, as well as
calibration information:

[`decode_structured_light_pattern`](decode_structured_light_pattern.md) must be called before
`reconstruct_surface_structured_light`, storing the correspondence image
between the projector coordinates and the camera coordinates
in the model *`StructuredLightModel`*, i. e. for
each camera pixel which projector pixel lighted (i.e. encoded) the observed
point on the surface.
`reconstruct_surface_structured_light` uses the vertical correspondence
image, so the parameter *'pattern_orientation'* of
[`set_structured_light_model_param`](set_structured_light_model_param.md) must have been set to
*'vertical'* or *'both'*. Note that in most cases
*'vertical'* should be chosen for speed, since fewer images are
necessary than for *'both'*.

For setting the calibration information, please refer to the parameter
*'camera_setup_model'* of [`set_structured_light_model_param`](set_structured_light_model_param.md).

The reconstruction is performed only within the domain of the correspondence
image. Reducing the domain of the input images of
[`decode_structured_light_pattern`](decode_structured_light_pattern.md) (e.g., with [`reduce_domain`](reduce_domain.md))
can be used to obtain a reduced reconstructed surface, i. e. for shorter
runtime or to reduce noise.
The resulting *`ObjectModel3D`* contains a mapping, so the
coordinate images can be obtained by [`object_model_3d_to_xyz`](object_model_3d_to_xyz.md) using
*'from_xyz_map'*.
Pixels for which no reconstruction was possible are excluded from its domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`StructuredLightModel`** (input_control)  structured_light_model `→`  (handle)

Handle of the structured light model.

**`ObjectModel3D`** (output_control)  object_model_3d `→`  (handle)

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

The operator `reconstruct_surface_structured_light` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`decode_structured_light_pattern`

## Possible Successors

`object_model_3d_to_xyz`

## See also

`create_structured_light_model`,
`set_structured_light_model_param`

## Module

3D Metrology
