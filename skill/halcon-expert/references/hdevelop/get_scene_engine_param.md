# get_scene_engine_param (Operator)

## Name

`get_scene_engine_param` — Read a parameter from a running Scene Engine instance.

## Signature

`get_scene_engine_param( : : SceneEngine, GenParamName : GenParamValue)`

## Description

The operator `get_scene_engine_param` returns the parameter values
of *`GenParamName`* for the running Scene Engine instance *`SceneEngine`*
in *`GenParamValue`*.

The following parameter names are supported:

- *'assets'*:
  Returns a dictionary that contains information about the available
  assets. This includes the asset base directory (see
  [`set_scene_engine_param`](set_scene_engine_param.md) for how to change this directory),
  the available *'tags'* and *'categories'*, as well as
  information about the detected asset providers.
- *'devices'*:
  Returns a tuple containing the available rendering devices.
- *'material_presets'*:
  Returns a dictionary that contains the pre-set material properties.
  In each entry of the dictionary, the key corresponds to the name of
  the preset (such as *'metal'*), and the value contains the
  rendering properties to obtain a surface that mimics this material.
  This allows setting the surface / material properties of an object
  (see [`run_scene_engine`](run_scene_engine.md)).
- *'selected_device'*:
  The device currently selected for data generation.
  See [`set_scene_engine_param`](set_scene_engine_param.md), *'select_device_idx'* for
  how to change the selected device.
- *'version'*:
  Returns a string that contains the version number of the Scene Engine.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SceneEngine`** (input_control)  scene_engine `→`  (handle)

Handle of the Scene Engine connection.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of parameters.

Default:
[]

Suggested values:
'version', 'devices', 'selected_device', 'assets', 'material_presets'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (string / real / integer / handle)

Values of parameters.

## Result

If the parameters are valid, the operator `get_scene_engine_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`open_scene_engine`,
`set_scene_engine_param`

## Possible Successors

`run_scene_engine`,
`set_scene_engine_param`

## See also

`create_deep_matching_3d`

## Module

3D Metrology
