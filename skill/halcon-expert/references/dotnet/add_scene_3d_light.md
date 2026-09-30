# AddScene3dLight (Operator)

## Name

`AddScene3dLight` — Add a light source to a 3D scene.

## Signature

`static void HOperatorSet.AddScene3dLight(HTuple scene3D, HTuple lightPosition, HTuple lightKind, out HTuple lightIndex)`

`int HScene3D.AddScene3dLight(HTuple lightPosition, string lightKind)`

## Description

`AddScene3dLight` adds a new light source to the scene
*`scene3D`* and returns its index in *`lightIndex`*. The kind of
the light source must be specified in *`lightKind`*.
For *`lightKind`* = *"point_light"*, *`lightPosition`* is
interpreted as the position of the light source.
For *`lightKind`* = *"directional_light"*, *`lightPosition`*
is interpreted as the vector of the directional light source.

Currently only one light source is supported, such that
`AddScene3dLight` overwrites the existing light source. This may
be changed in future versions.

If no light source is set, a point light source at [-100.0, -100.0, 0.0]
is used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene3D`** (input_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

**`lightPosition`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double* / int / long)

Position of the new light source.

Default:
[-100.0,-100.0,0.0]

**`lightKind`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the new light source.

Default:
"point_light"

List of values:
"directional_light", "point_light"

**`lightIndex`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the new light source in the 3D scene.

## Result

`AddScene3dLight` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateScene3d`

## Possible Successors

`SetScene3dLightParam`

## See also

`RemoveScene3dLight`

## Module

3D Metrology
