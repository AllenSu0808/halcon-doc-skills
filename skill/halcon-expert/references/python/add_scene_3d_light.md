# add_scene_3d_light (Operator)

## Name

`add_scene_3d_light` — Add a light source to a 3D scene.

## Signature

`def add_scene_3d_light(scene_3d: HHandle, light_position: Sequence[Union[int, float]], light_kind: str) -> int`

## Description

`add_scene_3d_light` adds a new light source to the scene
*`scene_3d`* and returns its index in *`light_index`*. The kind of
the light source must be specified in *`light_kind`*.
For *`light_kind`* = *"point_light"*, *`light_position`* is
interpreted as the position of the light source.
For *`light_kind`* = *"directional_light"*, *`light_position`*
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

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`light_position`** (input_control)  real-array `→` Sequence[Union[int, float]]

Position of the new light source.

Default:
[-100.0,-100.0,0.0]

**`light_kind`** (input_control)  string `→` str

Type of the new light source.

Default:
"point_light"

List of values:
"directional_light", "point_light"

**`light_index`** (output_control)  integer `→` int

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
