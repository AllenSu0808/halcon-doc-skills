# add_scene_3d_light (Operator)

## Name

`add_scene_3d_light` — Add a light source to a 3D scene.

## Signature

`add_scene_3d_light( : : Scene3D, LightPosition, LightKind : LightIndex)`

## Description

`add_scene_3d_light` adds a new light source to the scene
*`Scene3D`* and returns its index in *`LightIndex`*. The kind of
the light source must be specified in *`LightKind`*.
For *`LightKind`* = *'point_light'*, *`LightPosition`* is
interpreted as the position of the light source.
For *`LightKind`* = *'directional_light'*, *`LightPosition`*
is interpreted as the vector of the directional light source.

Currently only one light source is supported, such that
`add_scene_3d_light` overwrites the existing light source. This may
be changed in future versions.

If no light source is set, a point light source at [-100.0, -100.0, 0.0]
is used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`LightPosition`** (input_control)  real-array `→`  (real / integer)

Position of the new light source.

Default:
[-100.0,-100.0,0.0]

**`LightKind`** (input_control)  string `→`  (string)

Type of the new light source.

Default:
'point_light'

List of values:
'directional_light', 'point_light'

**`LightIndex`** (output_control)  integer `→`  (integer)

Index of the new light source in the 3D scene.

## Result

`add_scene_3d_light` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_scene_3d`

## Possible Successors

`set_scene_3d_light_param`

## See also

`remove_scene_3d_light`

## Module

3D Metrology
