# SetSceneEngineParam (Operator)

## Name

`SetSceneEngineParam` — Set parameters of a running Scene Engine instance.

## Signature

`static void HOperatorSet.SetSceneEngineParam(HTuple sceneEngine, HTuple genParamName, HTuple genParamValue)`

`static void HDeepMatching3D.SetSceneEngineParam(HSceneEngine sceneEngine, string genParamName, HTuple genParamValue)`

`static void HDeepMatching3D.SetSceneEngineParam(HSceneEngine sceneEngine, string genParamName, string genParamValue)`

## Description

The operator `SetSceneEngineParam` sets a parameter
of the running Scene Engine instance *`sceneEngine`*.
The parameter name is specified in *`genParamName`*, the
corresponding value in *`genParamValue`*.

The following parameters are supported:

- *"asset_path"*: A string containing the path of the
  asset library. See [`OpenSceneEngine`](open_scene_engine.md) for a description
  of the assets. When starting a new Scene Engine, the path is
  by default set to the value of the environment variable
  HALCON_ASSET_DIR.

  Default:
   The value of the environment variable
  HALCON_ASSET_DIR
- *"select_device_idx"*:
  An integer that selects the device (GPU) to be used for rendering
  data during the data generation.
  The index is the entry in the list returned by
  [`GetSceneEngineParam`](get_scene_engine_param.md) with parameter *"devices"*.

  Note that the device must be selected before the first call
  of [`RunSceneEngine`](run_scene_engine.md). It is not possible to change the
  device of a running Scene Engine instance after the first call of
  [`RunSceneEngine`](run_scene_engine.md).

  Default:
   *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sceneEngine`** (input_control)  scene_engine `→` [HSceneEngine](HSceneEngine.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Scene Engine connection.

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Names of parameters.

Default:
"asset_path"

Suggested values:
"asset_path", "select_device_idx"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Values of parameters.

Default:
[]

Suggested values:

## Result

If the parameters are valid, the operator `SetSceneEngineParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`OpenSceneEngine`,
`GetSceneEngineParam`

## Possible Successors

`RunSceneEngine`,
`GetSceneEngineParam`

## See also

`CreateDeepMatching3d`,
`GetSceneEngineParam`

## Module

3D Metrology
