# set_scene_3d_light_param (Operator)

## Name

`set_scene_3d_light_param` — Set parameters of a light in a 3D scene.

## Signature

`def set_scene_3d_light_param(scene_3d: HHandle, light_index: int, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[str, int, float]]) -> None`

## Description

`set_scene_3d_light_param` sets parameters of a light source in the
3D scene *`scene_3d`*. The name and value of a parameter must be given
in *`gen_param_name`* and *`gen_param_value`*. The following
parameters can be set:

- ***"ambient"*:** —

  Ambient part of the light source. Must be given as a tuple of
  three numbers.

  Default:
   *[0.2, 0.2, 0.2]*.
- ***"diffuse"*:** —

  Diffuse part of the light source. Must be given as a tuple of
  three numbers.

  Default:
   *[0.8, 0.8, 0.8]*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_3d`** (input_control)  scene_3d `→` HHandle

Handle of the 3D scene.

**`light_index`** (input_control)  integer `→` int

Index of the light source.

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of the generic parameters.

Default:
"ambient"

List of values:
"ambient", "diffuse"

**`gen_param_value`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int, float]]

Values of the generic parameters.

Default:
[0.2,0.2,0.2]

Suggested values:
[0.2,0.2,0.2]

## Result

`set_scene_3d_light_param` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`add_scene_3d_instance`

## Module

3D Metrology
