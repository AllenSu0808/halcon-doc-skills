# set_scene_3d_light_param (Operator)

## Name

`set_scene_3d_light_param` — Set parameters of a light in a 3D scene.

## Signature

`set_scene_3d_light_param( : : Scene3D, LightIndex, GenParamName, GenParamValue : )`

## Description

`set_scene_3d_light_param` sets parameters of a light source in the
3D scene *`Scene3D`*. The name and value of a parameter must be given
in *`GenParamName`* and *`GenParamValue`*. The following
parameters can be set:

- ***'ambient'*:** —

  Ambient part of the light source. Must be given as a tuple of
  three numbers.

  Default:
   *[0.2, 0.2, 0.2]*.
- ***'diffuse'*:** —

  Diffuse part of the light source. Must be given as a tuple of
  three numbers.

  Default:
   *[0.8, 0.8, 0.8]*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Scene3D`** (input_control)  scene_3d `→`  (handle)

Handle of the 3D scene.

**`LightIndex`** (input_control)  integer `→`  (integer)

Index of the light source.

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the generic parameters.

Default:
'ambient'

List of values:
'ambient', 'diffuse'

**`GenParamValue`** (input_control)  string(-array) `→`  (string / integer / real)

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
