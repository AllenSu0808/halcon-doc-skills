# open_scene_engine (Operator)

## Name

`open_scene_engine` — Start and connect to the Scene Engine synthetic data generator.

## Signature

`open_scene_engine( : : GenParamName, GenParamValue : SceneEngine)`

## Description

The operator `open_scene_engine` starts the executable of
the synthetic data generation tool Scene Engine and connects to
the started instance.
Starting and connecting the Scene Engine can be configured using the
generic parameters *`GenParamName`* and *`GenParamValue`*,
which are described further below.

The executable is terminated when the handle returned in
*`SceneEngine`* is cleared.
This is typically the case once no tuple contains that
handle.
To terminate the executable manually, use
[`clear_handle`](clear_handle.md) to clear the *`SceneEngine`*-Handle.

### Location of the executable

The operator looks for the executable at the following locations,
using the first matching location.

1. The generic parameter *'executable'* (see below).
2. The environment variable HALCON_SCENE_ENGINE, which is
   typically set during installation. Note that the value of
   HALCON_SCENE_ENGINE must end with *'/scene_engine'* (on
   Linux) or *'/scene_engine.exe'* (on Windows).
3. The file *'run_scene_engine.sh'* (on Linux) or
   *'scene_engine.exe'* (on Windows) in the default installation path
   `$HALCONROOT/../SceneEngine-26.05`.

Note that a proper installation of the executable is required,
e.g. using the MVTec Software Manager (SOM).
Most notable, it must be able to find its dynamic link libraries. On Linux,
this requires extending the value of the environment variable
LD_LIBRARY_PATH with the `/lib` directory from the Scene
Engine installation:

`LD_LIBRARY_PATH=/path/to/SceneEngine/lib:$LD_LIBRARY_PATH`

Alternatively, the script *'run_scene_engine.sh'* from the Scene
Engine installation can be used as value of the generic parameter
*'executable'* (see below).

### Location of assets

Assets are 3D models, textures and environment maps that are used
to add variation to the generated images, as well as to make them
more realistic.
Note that assets need to be installed beforehand, using for example
the MVTec Software Manager (SOM).
The path to the assets must be set in the environment variable
HALCON_ASSET_DIR.
Alternatively, the path to the assets can be set using
[`set_scene_engine_param`](set_scene_engine_param.md).
To check if assets were correctly found by the Scene Engine, use
[`get_scene_engine_param`](get_scene_engine_param.md) with the parameter *'assets'*.

### Generic Parameters

The operator supports the following additional parameters, which can
be set by passing a pair of tuples to *`GenParamName`* and
*`GenParamValue`* which contain the parameter names and values,
respectively.

- *'debug_log_file'*: A string that specifies the filename and
  location of a debug file, for example *'c:/temp/scene_engine.log'*.
  If set, the opened Scene Engine instance creates the corresponding file
  and writes debug information into it.
- *'executable'*: A string containing the location of the
  executable to be started. Note that the value of *'executable'*
  must end with *'/scene_engine'* (on Linux) or
  *'/scene_engine.exe'* (on Windows). On Linux, it is also possible
  to use the script *'run_scene_engine.sh'* from the Scene Engine
  installation as value of *'executable'*, as long as its full path
  is specified. This script helps set the correct environment variables.

  Default:
   See above for the default search locations.
- *'timeout'*: After starting the executable, the operator
  will wait this many seconds for the executable to connect.
  If the executable does not start up within that time, an error
  is returned.
  Setting the timeout to *0* disables the timeout.

  Default:
   *60.0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of parameters.

Default:
[]

Suggested values:
'debug_log_file', 'executable', 'timeout'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / real / integer)

Values of parameters.

Default:
[]

Suggested values:
'c:/temp/scene_engine.log', '/tmp/scene_engine.log', 'scene_engine', 'scene_engine.exe', 10.0, 0

**`SceneEngine`** (output_control)  scene_engine `→`  (handle)

Handle of the Scene Engine connection.

## Result

If the parameters are valid, the operator `open_scene_engine`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_scene_engine_param`,
`run_scene_engine`

## Alternatives

`render_object_model_3d`,
`disp_object_model_3d`

## See also

`create_deep_matching_3d`

## Module

3D Metrology
