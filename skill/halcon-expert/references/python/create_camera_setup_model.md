# create_camera_setup_model (Operator)

## Name

`create_camera_setup_model` — Create a model for a setup of calibrated cameras.

## Signature

`def create_camera_setup_model(num_cameras: int) -> HHandle`

## Description

The operator `create_camera_setup_model` creates a new camera
setup model and returns a handle to it in *`camera_setup_model_id`*.
The camera setup comprises a fixed number of cameras, which is
specified by *`num_cameras`* and cannot be changed once the model
was created. For each camera, the setup stores its internal parameters,
covariances of the internal parameters (optional) and a pose of the
camera.

Using [`set_camera_setup_param`](set_camera_setup_param.md), you can change the coordinate
system in which the cameras are represented: You can either select
a camera and convert all camera poses to be relative to this camera
or you can apply a general coordinate transformation, which moves
the setup's coordinate system into an arbitrary pose. Changing the coordinate
system of the camera setup is particularly useful in cases, where, e.g.,
you want to represent the cameras in the coordinate system of an
object being observed by the cameras. This concept is further
demonstrated in the example below.

The internal parameters and pose of a camera are set or modified by
[`set_camera_setup_cam_param`](set_camera_setup_cam_param.md). Further camera parameters and
general setup parameters can be set by [`set_camera_setup_param`](set_camera_setup_param.md) as
well. All parameters can be read back by [`get_camera_setup_param`](get_camera_setup_param.md).

A camera setup model can be saved into a file by
[`write_camera_setup_model`](write_camera_setup_model.md) and read back by
[`read_camera_setup_model`](read_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`num_cameras`** (input_control)  integer `→` int

Number of cameras in the setup.

Default:
2

Suggested values:
1, 2, 3, 4

Restriction:
`NumCameras >= 1`

**`camera_setup_model_id`** (output_control)  camera_setup_model `→` HHandle

Handle to the camera setup model.

## Example (HDevelop)

```
* Create camera setup of three cameras.
create_camera_setup_model (3, CameraSetupModelID)
gen_cam_par_area_scan_division (0.006, 0, 8.3e-6, 8.3e-6,\
              512, 384, 1024, 768, StartCamPar)
* Camera 0 is located in the origin.
set_camera_setup_cam_param (CameraSetupModelID, 0, [], StartCamPar,\
                            [0, 0, 0, 0, 0, 0, 0])

* Camera 1 is shifted 0.07 m in positive x-direction relative to
* camera 0.
set_camera_setup_cam_param (CameraSetupModelID, 1, [], StartCamPar,\
                            [0.07, 0, 0, 0, 0, 0, 0])

* Camera 2 is shifted 0.1 m in negative y-direction relative to
* camera 0.
set_camera_setup_cam_param (CameraSetupModelID, 2, [], StartCamPar,\
                            [0.0, -0.1, 0, 0, 0, 0, 0])

* There is an object, which is 0.5 away from the origin in
* z-direction, and is facing the origin.
ObjectPose := [0, 0, 0.5, 180, 0, 0, 0]
* Place the setup's origin in the object.
set_camera_setup_param (CameraSetupModelID, 'general', 'coord_transf_pose',\
                        ObjectPose)

* Now the camera poses are given relative to the object.
get_camera_setup_param (CameraSetupModelID, 0, 'pose', CamPose0)
* CamPose0 is equivalent to [0.0, 0.0, 0.5, 180.0, 0.0, 0.0, 0]

get_camera_setup_param (CameraSetupModelID, 1, 'pose', CamPose1)
* CamPose1 is equivalent to [0.07, 0.0, 0.5, 180.0, 0.0, 0.0, 0]

get_camera_setup_param (CameraSetupModelID, 2, 'pose', CamPose2)
* CamPose2 is equivalent to [0.0, 0.1, 0.5, 180.0, 0.0, 0.0, 0]
```

## Possible Successors

`set_camera_setup_param`

## Module

Calibration
