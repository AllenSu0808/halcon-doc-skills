# run_scene_engine (Operator)

## Name

`run_scene_engine` — Generate synthetic data using a running Scene Engine instance.

## Signature

`def run_scene_engine(scene_engine: HHandle, generation_params: HHandle) -> HHandle`

## Description

The operator `run_scene_engine` generates synthetic data
using the running *`scene_engine`*, which must be
started beforehand with [`open_scene_engine`](open_scene_engine.md).
The generation of the data is controlled using the dictionary
*`generation_params`*, the generated data is returned in
*`generated_data`*.

The operator does not return until the Scene Engine has completed the
generation.

**It is recommended to create the dictionary that contains the data
generation parameters using the procedures**
`create_scene_engine_run_params` and
`set_scene_engine_run_param`, which provide a user-friendly
way of managing the different possible settings for most
use cases.

### Data generation stages

The data generation is performed in five steps:

1. **Physics simulation**:
   In this step, the positions (poses) of the different objects
   are created using a physically realistic simulation.
   The objects are dropped either on a ground plane, or into a
   box.

   The parameters can be used to set the number of instances
   dropped into the scene, as well as for dropping additional
   "disturber" objects.
2. **Material and asset management**:
   In this step, the surface and material characteristics of the
   objects are defined.
   For each object, including the ground plane and the box, these can either
   be uniform settings over the
   complete surface of the object, or texture- and material-maps
   that define the surface on a per-point basis.
3. **Camera placement**:
   In this step, virtual cameras are placed in the scene such that
   they see at least a certain amount of the objects of interest.

   The parameters allow specifying the number of cameras, the distance of the
   cameras to the object, the in-plane rotation (rotation around the z-axis),
   the camera elevation, as well as the minimum visible object surface area.
4. **Meta information**:
   In this step, meta information is computed for each camera
   view that later helps to generate ground truth targets for
   deep learning.
5. **Rendering**:
   This final step renders photorealistic images of the scene,
   using the object placements, materials and camera positions
   determined in the previous steps.

### Data generation parameters

The data generation parameters are passed as a dictionary
*`generation_params`*.
As mentioned above, it is recommended to use the procedures
to create and modify this dictionary (`create_scene_engine_run_params`
and `set_scene_engine_run_param`).

To allow generating data with a high variation, many
values also allow the definition of an interval instead of a single
value. The Scene Engine then randomly selects a value from this
interval as needed. An interval is defined by a tuple consisting of a
minimum and maximum value.
For parameters that require three values, such as RGB values,
a specific constellation consisting of a tuple with three values
can be passed, or an interval can be defined by passing a tuple
with six entries containing the three minimum values followed
by the three maximum values.

For example, if `cameras.elevation`
is set to *60*, the elevation of the camera w.r.t. the
ground plane will always be *60* degrees.
If it is instead set to *[40,90]*, the elevation for
each camera is selected randomly between *40* and
*90* degrees.

For example, if `base_color` is set to
*[0.2, 0, 0]*, red will be set to *0.2*,
while green and blue are set to *0*.
If set to *[0.2,0,0, 0.5,0,0.1]*, however,
red will be between *0.2* and *0.5*,
green will be *0.0*, and blue will be between
*0.0* and *0.1*.

In the dictionary *`generation_params`*, the following values can be set:

- ***"cameras"*** —

  This dictionary controls the placement of cameras in the virtual
  scene during the *"cameras"*-stage.

  - ***"cameras.distance_to_object"*** —

    The distance of the virtual cameras to the placed object.
    When placing a camera, one of the target objects with
    type name *"part"* is selected and centered
    in the camera. The camera is then moved away from that
    centered object by the amount specified in this parameter.

    Suggested values:
     Object diameter * *[1,3]*

    Value range:
     $>$ *0*
  - ***"cameras.elevation"*** —

    The elevation of the cameras w.r.t. the ground plane, in degrees.
    An elevation of *90* degrees corresponds to a camera looking from
    exactly above down onto the plane, while an elevation of *0*
    corresponds to a camera that lies flat on the plane.

    Value range:
     [*0*, *90*]

    Suggested values:
     [*20*, *90*]
  - ***"cameras.field_of_view_y"*** —

    The camera's vertical field of view in degrees.
    Smaller field of views simulate cameras with a larger focal length.

    Value range:
     [*0*, *170*]

    Suggested values:
     [*40*, *90*]
  - ***"cameras.in_plane_rotation"*** —

    The range of in-plane rotation, i.e. rotation around the
    camera's z-axis, in degrees.
    To disable any in-plane rotation, i.e. to have all cameras
    upright, set this value to zero.

    Value range:
     [*-360*, *360*]

    Suggested values:
     [*-180*, *180*]
  - ***"cameras.num_cameras"*** —

    The number of cameras to place.

    Value range:
     [*1*, *100*]

    Default:
     *15*
  - ***"cameras.width"*, *"cameras.height"*** —

    The resolution of the created cameras.

    Value range:
     [*100*, *10000*]

    Default:
     *"width"*: 900, *"height"*: 600
- ***"environment_map"*** —

  This dictionary controls the environment map to be used in the scene.
  The environment map controls both the background of the scene and the
  light sources in the scene.
  It is recommended to use an environment map from the asset library,
  which provides variation in background and lighting.

  - ***"environment_map.base_color"*** —

    For *"environment_map.type"* *"individual"*, this
    determines the color of the environment map in normalized (RGB).

    Value range:
     [*0*, *1*] for each component

    Suggested values:
     [*1*, *0*, *0*]
  - ***"environment_map.tags"*,
    *"environment_map.categories"*** —

    A tuple of strings. For *"environment_map.type"* *"asset"*,
    these values can be used to further filter the assets to be used.
    A list of available tags and categories can be queried using
    [`get_scene_engine_param`](get_scene_engine_param.md).
  - ***"environment_map.type"*** —

    The type of the environment map.
    If set to *"asset"*, a random
    environment map from the asset library will be used.
    If set to *"individual"*, a uniformly colored
    environment map will be used.

    List of values:
     *"asset"*, *"individual"*

    Default:
     *"asset"*.
- ***"objects"*** —

  This dictionary controls the object types and their materials.
  The value is a dictionary. The keys contain the names
  of the object types, each mapping to a dictionary that
  describes the object types properties.

  The possible values in the dictionaries are described in
  the section “Object settings”further below.

  Some object type names are pre-defined and handled
  specially: *"part"* always refers to the
  "main" object type, typically the one for which a
  dataset is created.
  *"box"* and *"ground_plane"* control
  the materials of boxes and the ground plane created
  by the physics stage.

  Suggested values:
   See section “Object settings” further below.

  - ***"objects.myobject1"*, *"objects.foobar"*** —

    Dictionaries containing information about additional user-defined object types.
  - ***"objects.part"*, *"objects.box"*,
    *"objects.ground_plane"*** —

    Dictionary containing details of the main part (*"part"*),
    the box that objects are dropped into (*"box"*),
    and the ground plane (*"ground_plane"*), respectively.
- ***"physics"*** —

  Dictionary with settings for the *"physics"* stage.

  - ***"physics.box_probability"*** —

    Probability of having a box in the scene as a number.

    Value range:
     [*0*, .., *1*]

    Default:
     *0.5*
  - ***"physics.box_width"*, *"physics.box_height"*,
    *"physics.box_length"*, *"physics.box_wall_width"*** —

    If a box is placed into the scene, these values control
    its size.

    Value range:
     $>$ *0*

    Suggested values:
     Object diameter times *4*, *3*, *5* and
    *0.2* respectively.
- ***"renderer"*** —

  Dictionary with additional parameters for the photorealistic renderer.
  Currently, no parameters can be set.
- ***"scene"*** —

  Instead of executing the physics stage to create a new
  scene, an existing scene can be passed in this field.
  This can be used to re-render a scene after manually
  adjusting, for example, materials or camera placements.

  The value of this field is a dictionary and is
  usually the *`generated_data`* of a previous
  run of `run_scene_engine`.

  Attention:
   Typically not set, otherwise *`generated_data`*
  of a previous call.
- ***"stages"*** —

  A tuple containing the stages to be executed.
  For a full run, this tuple should be
  *"physics"*, *"materials"*,
  *"cameras"*, *"rendering"*.

  Stages can be skipped if an existing scene description
  is passed in the *"scene"*-field (see above), or if
  for example only the physical scene but no rendered
  images are required.

  Note that the meta information is computed in the
  camera search stage (*"cameras"*). Thus, the
  *"meta_info"* stage can be skipped if the
  *"cameras"* stage is active. If, however,
  fixed camera poses and parameters are passed in
  the *"scene"* field, the *"meta_info"*
  stage can be used to compute the meta information
  without executing the camera search.

  List of values:
   *"physics"*, *"materials"*,
  *"cameras"*, *"meta_info"*,
  *"rendering"*.

### Object settings

The *"objects"* field of the configuration dictionary defines the
details of all objects to be placed and rendered in the scene,
including the object, the box, the background, and any custom objects.

- ***"material"*** —

  A dictionary that describes the material of the object.

  - ***"material.base_color"*** —

    The base color of the object in (RGB).
    This setting can be used for material types *"preset"* or
    *"individual"*. For *"preset"*, they can be used to
    obtain, for example, red plastic.

    Value range:
     [*0*, *1*] for each component

    Suggested values:
     [*1*, *0*, *0*]
  - ***"material.metallic"*, *"material.roughness"*,
    *"material.ior"*, *"material.transmission"*,
    *"material.diffuse_roughness"*, *"material.sheen_weight"*,
    *"material.sheen_roughness"*, *"material.sheen_tint"*,
    *"material.coat_weight"*, *"material.coat_roughness"*,
    *"material.coat_ior"*, *"material.coat_tint"*** —

    Distribution of 1 value or 3 values (for *"material.sheen_tint"*
    and *"material.coat_tint"*).
    For type *"individual"*, these values define the physically
    based rendering (PBR) properties of the object.
    The parameters are further described below in the
    Individual Materials section.
  - ***"material.preset"*** —

    For *"material.type"* *"preset"*, this field defines the
    name of the preset to use.
    A list of available names can be queried using
    [`get_scene_engine_param`](get_scene_engine_param.md).

    List of values:
     *"plastic"*, *"plastic_clear"*,
    *"metal"*, *"metal_shiny"*, *"glass"*.
  - ***"material.type"*** —

    Material type.
    *"asset"* is a material loaded from the asset library,
    typically a physically realistic texture.
    *"preset"* is a pre-defined uniform material, such as
    plastic or metal, which can be further modified using a color.
    *"individual"* is a user-defined uniform material.

    Details about parameters of the types are described in the
    sections further below.

    List of values:
     *"asset"*, *"preset"*, *"individual"*.
  - ***"material.tags"*, *"material.categories"*** —

    A tuple of strings. For *"material.type"* *"asset"*,
    these values can be used to further filter the assets to be used.
    A list of available tags and categories can be queried using
    [`get_scene_engine_param`](get_scene_engine_param.md).
  - ***"material.use"*** —

    If set to *"fallback"*, then the defined material is
    only applied if the object does not already contain a material.
    If set to *"always"*, the defined material is always applied.
    This can be used to define a fallback material for distractor meshes
    loaded from the asset library, which sometimes already define
    their own material or texture.

    List of values:
     *"always"*, *"fallback"*

    Default:
     *"fallback"*.
- ***"num_instances"*** —

  A distribution that describes the number of instances to create
  for this object type.

  Value range:
   $\ge$ *0*

  Suggested values:
   [*1*, *4*]

### 3D Mesh

To define the 3D mesh of the object type, which is used
for the physics simulation and the rendering, one of the
following three fields, `mesh_fname`,
`mesh` or `mesh_asset` must be set.

- ***"mesh"*** —

  3D object model containing the mesh to be used for the model.
  If set, the 3D object model must contain at least vertices and faces.
- ***"mesh_asset"*** —

  Dictionary with specification of the asset to be used for the model.
  If *"mesh_asset"* is set, then the object is chosen
  randomly from the available assets.
  Note that many assets already contain a texture.
- ***"mesh_asset.tags"*, *"mesh_asset.categories"*** —

  A tuple of strings. For asset meshes,
  these values can be used to further filter the assets to be used.
  A list of available tags and categories can be queried using
  [`get_scene_engine_param`](get_scene_engine_param.md).
- ***"mesh_fname"*** —

  Filename of the mesh to be used for the model.
  If set, the object is read from this file.
  For details about supported file formats see
  [`read_object_model_3d`](read_object_model_3d.md).

  Suggested values:
   *"pipe_joint"*

### Preset Materials

When using *"material.type"* *"preset"*, the following
materials are available. Note that they can be further
modified by setting the color in the *"material.base_color"*
field.

![figure](../assets/cfc9a73fde236b6a.svg)

Default materials available in the Scene Engine, from left to right:
*"plastic"*,
plastic with clear coat (*"plastic_clear"*),
*"metal"*, shiny metal (*"metal_shiny"*),
and *"glass"*.
Note that the color of each material can be further modified.

It is possible to further refine the parameters for these materials.
For this, their detailed settings can be queried using
[`get_scene_engine_param`](get_scene_engine_param.md). The settings can then be modified
and set in the *"material"* dictionary, using *"material.type"*
set to *"individual"*.

### Individual Materials

When using *"material.type"* *"individual"*,
physically based rendering (PBR) properties of the material can be
set.
The following images show how the most important of these
settings influence the resulting materials.

Note that it is recommended to not set singular values, but
distributions for each value. This adds variation to the generated
data, which helps to generalize networks trained on that data.

Further note that [`get_scene_engine_param`](get_scene_engine_param.md) can be used to obtain
the PBR properties (as distributions) of the preset materials.
Those can be used as baseline to fine-tune a material.

For additional details about the parameters, please refer to
the paper described in the *"References"* section below.

![figure](../assets/4697677a9c78b5d7.svg)

Blue plastic components with `roughness`
from *0.0* (left) to *1.0* (right).

![figure](../assets/fe3ae7d320e5f7df.svg)

Different `base_color` for plastic with the same roughness.

![figure](../assets/8bcc47145d58523a.svg)

Different `base_color` for metal with the same roughness.

![figure](../assets/903dfb37cc08bc9e.svg)

Different `base_color` for glass with the same transmission values.

![figure](../assets/0b37ed6ffa8578bb.svg)

The difference between clear coat values from *0.0* to *1.0* with
the same roughness (top row) and roughness values from *0.0* to
*1.0* (bottom row) on metal parts.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`scene_engine`** (input_control)  scene_engine `→` HHandle

Handle of the Scene Engine connection.

**`generation_params`** (input_control)  dict `→` HHandle

Parameters for data generation.

**`generated_data`** (output_control)  dict `→` HHandle

Generated data.

## Result

If the parameters are valid, the operator `run_scene_engine`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`open_scene_engine`,
`set_scene_engine_param`,
`get_scene_engine_param`

## Alternatives

`render_object_model_3d`,
`disp_object_model_3d`

## See also

`create_deep_matching_3d`

## References

Burley, Brent, and Walt Disney Animation Studios: “Physically-based
shading at disney.” Acm Siggraph. 2012.

## Module

3D Metrology
