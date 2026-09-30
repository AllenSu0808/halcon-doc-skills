# GetSceneEngineParam (Operator)

## Name

`GetSceneEngineParam` — Read a parameter from a running Scene Engine instance.

## Signature

`static void HOperatorSet.GetSceneEngineParam(HTuple sceneEngine, HTuple genParamName, out HTuple genParamValue)`

`static HTuple HDeepMatching3D.GetSceneEngineParam(HSceneEngine sceneEngine, HTuple genParamName)`

`static HTuple HDeepMatching3D.GetSceneEngineParam(HSceneEngine sceneEngine, string genParamName)`

## Description

The operator `GetSceneEngineParam` returns the parameter values
of *`genParamName`* for the running Scene Engine instance *`sceneEngine`*
in *`genParamValue`*.

The following parameter names are supported:

- *"assets"*:
  Returns a dictionary that contains information about the available
  assets. This includes the asset base directory (see
  [`SetSceneEngineParam`](set_scene_engine_param.md) for how to change this directory),
  the available *"tags"* and *"categories"*, as well as
  information about the detected asset providers.
- *"devices"*:
  Returns a tuple containing the available rendering devices.
- *"material_presets"*:
  Returns a dictionary that contains the pre-set material properties.
  In each entry of the dictionary, the key corresponds to the name of
  the preset (such as *"metal"*), and the value contains the
  rendering properties to obtain a surface that mimics this material.
  This allows setting the surface / material properties of an object
  (see [`RunSceneEngine`](run_scene_engine.md)).
- *"selected_device"*:
  The device currently selected for data generation.
  See [`SetSceneEngineParam`](set_scene_engine_param.md), *"select_device_idx"* for
  how to change the selected device.
- *"version"*:
  Returns a string that contains the version number of the Scene Engine.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sceneEngine`** (input_control)  scene_engine `→` [HSceneEngine](HSceneEngine.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Scene Engine connection.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of parameters.

Default:
[]

Suggested values:
"version", "devices", "selected_device", "assets", "material_presets"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Values of parameters.

## Result

If the parameters are valid, the operator `GetSceneEngineParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`OpenSceneEngine`,
`SetSceneEngineParam`

## Possible Successors

`RunSceneEngine`,
`SetSceneEngineParam`

## See also

`CreateDeepMatching3d`

## Module

3D Metrology
