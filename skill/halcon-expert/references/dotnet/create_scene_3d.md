# CreateScene3d (Operator)

## Name

`CreateScene3d` — Create the data structure that is needed to visualize collections of
3D objects.

## Signature

`static void HOperatorSet.CreateScene3d(out HTuple scene3D)`

`public HScene3D()`

`void HScene3D.CreateScene3d()`

## Description

`CreateScene3d` creates a new 3D scene and returns it in
*`scene3D`*.

A 3D scene is a collection of instances of 3D object models, cameras, and
light sources. Use the operators [`AddScene3dInstance`](add_scene_3d_instance.md),
[`AddScene3dCamera`](add_scene_3d_camera.md), and [`AddScene3dLight`](add_scene_3d_light.md) to add these
objects to *`scene3D`*. Use [`DisplayScene3d`](display_scene_3d.md) to display a
3D scene in a window.

A pose is associated (with [`AddScene3dInstance`](add_scene_3d_instance.md) or
[`SetScene3dInstancePose`](set_scene_3d_instance_pose.md)) to each instance in the Scene, which
represents the instance's position within the scene coordinate system SCS.
The pose of the scene in the world coordinate system WCS can be set with
[`SetScene3dToWorldPose`](set_scene_3d_to_world_pose.md). The pose of the camera in the
world coordinate system can be set with [`SetScene3dCameraPose`](set_scene_3d_camera_pose.md) and
defines the camera coordinate system CCS.

![figure](../assets/595b2e9a51c68a01.svg)

The coordinate systems in a 3D scene

Parameters influencing the whole scene such as the quality of the
rendering can be set with [`SetScene3dParam`](set_scene_3d_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`scene3D`** (output_control)  scene_3d `→` [HScene3D](HScene3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D scene.

## Example (HDevelop)

```
  * Create a new scene
  create_scene_3d (Scene)
  * A scene needs at least one camera. The default pose
  * of a camera is located at the origin. The pose can be
  * changed with set_scene_3d_camera_pose.
  add_scene_3d_camera (Scene, CameraParam, CameraIndex)
  * Further a scene needs at least one light.
  add_scene_3d_light (Scene, [42.0, 42.0, 42.0], 'point_light', LightIndex)
  *
  * To add an object, add_scene_3d_instance is called with a
  * 3d object model and a pose. add_scene_3d returns an InstanceIndex
  * which must be used to reference this instance in subsequent calls.
  add_scene_3d_instance (Scene, ObjectModel3D, Pose, InstanceIndex)
  * Set its color.
  set_scene_3d_instance_param (Scene, InstanceIndex, 'color', 'green')
  * Display the scene.
  display_scene_3d (WindowHandle, Scene, CameraIndex)
  clear_scene_3d (Scene)
```

## Result

`CreateScene3d` returns 2 (
H_MSG_TRUE)
if the scene could be created
successfully. If necessary, an exception is raised.

## Possible Successors

`AddScene3dInstance`,
`AddScene3dLight`,
`AddScene3dCamera`,
`SetScene3dParam`

## See also

`ClearScene3d`

## Module

3D Metrology
