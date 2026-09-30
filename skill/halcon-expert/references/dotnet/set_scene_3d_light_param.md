# SetScene3dLightParam (Operator)

## Name

`SetScene3dLightParam` — Set parameters of a light in a 3D scene.

## Signature

`static void HOperatorSet.SetScene3dLightParam(HTuple scene3D, HTuple lightIndex, HTuple genParamName, HTuple genParamValue)`

`void HScene3D.SetScene3dLightParam(int lightIndex, HTuple genParamName, HTuple genParamValue)`

`void HScene3D.SetScene3dLightParam(int lightIndex, string genParamName, string genParamValue)`

## Description

`SetScene3dLightParam` sets parameters of a light source in the
3D scene *`scene3D`*. The name and value of a parameter must be given
in *`genParamName`* and *`genParamValue`*. The following
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

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`lightIndex`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the light source.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"ambient"

List of values:
"ambient", "diffuse"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the generic parameters.

Default:
[0.2,0.2,0.2]

Suggested values:
[0.2,0.2,0.2]

## Result

`SetScene3dLightParam` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`AddScene3dInstance`

## Module

3D Metrology
