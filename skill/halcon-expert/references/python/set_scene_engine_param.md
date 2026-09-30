# set_scene_engine_param (Operator)

## Name

`set_scene_engine_param` — Set parameters of a running Scene Engine instance.

## Signature

`def set_scene_engine_param(scene_engine: HHandle, gen_param_name: str, gen_param_value: HTupleType) -> None`

## Description

The operator `set_scene_engine_param` sets a parameter
of the running Scene Engine instance *`scene_engine`*.
The parameter name is specified in *`gen_param_name`*, the
corresponding value in *`gen_param_value`*.

The following parameters are supported:

- *"asset_path"*: A string containing the path of the
  asset library. See [`open_scene_engine`](open_scene_engine.md) for a description
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
  [`get_scene_engine_param`](get_scene_engine_param.md) with parameter *"devices"*.

  Note that the device must be selected before the first call
  of [`run_scene_engine`](run_scene_engine.md). It is not possible to change the
  device of a running Scene Engine instance after the first call of
  [`run_scene_engine`](run_scene_engine.md).

  Default:
   *0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_engine`** (input_control)  scene_engine `→` HHandle

Handle of the Scene Engine connection.

**`gen_param_name`** (input_control)  attribute.name `→` str

Names of parameters.

Default:
"asset_path"

Suggested values:
"asset_path", "select_device_idx"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` HTupleType

Values of parameters.

Default:
[]

Suggested values:

## Result

If the parameters are valid, the operator `set_scene_engine_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`open_scene_engine`,
`get_scene_engine_param`

## Possible Successors

`run_scene_engine`,
`get_scene_engine_param`

## See also

`create_deep_matching_3d`,
`get_scene_engine_param`

## Module

3D Metrology
