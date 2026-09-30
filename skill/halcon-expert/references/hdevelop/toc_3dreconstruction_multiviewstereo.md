## Multi-View Stereo

List of Operators ↓

This chapter contains operators for multi-view 3D reconstruction.

### Concept of Multi-view 3D Reconstruction

With multi-view 3D reconstruction, it is possible to generate 3D objects
using 2D images from multiple cameras.
It is possible to reconstruct the complete 3D surface of an object, or
single 3D points.

In the following, the steps that are required to reconstruct surfaces and
points are described briefly. Note that a well-calibrated camera setup
is the main requirement for a precise 3D reconstruction; see
[Calibration](toc_calibration.md) for more details. Additionally, in the HDevelop
example `reconstruct_surface_mixed_camera_types.hdev`, a typical
calibration workflow (from the calibration data model via the camera setup
model to the stereo model) is performed.

- **Generate stereo model:** —

  First, create the stereo model using

  - [`create_stereo_model`](create_stereo_model.md).

  If you want to reconstruct 3D points, choose the `Method`
  *`'points_3d'`*.

  ![figure](../assets/9bd380577c73fb82.svg)

  3D point reconstruction with *`'points_3d'`*.

  For the reconstruction of surfaces, the methods
  *`'surface_pairwise'`* and *`'surface_fusion'`* are
  available. For detailed information on these two methods, have a look
  at the reference manual entry of [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/5a3a0bf7c082677e.svg) | ![figure](../assets/26dafc478d4cec48.svg) | ![figure](../assets/07e197caa4370bb6.svg) |
  | ( 1) | ( 2) | ( 3) |

  These three 2D images are used for the surface reconstruction as seen
  in the images below.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/50c90c6a7b876074.svg) | ![figure](../assets/a2dc3649824f141f.svg) | ![figure](../assets/dc498705a331eebc.svg) |
  | ( 1) | ( 2) | ( 3) |

  (1) Surface reconstruction with *`'surface_pairwise'`*.
  (2) Surface reconstruction with *`'surface_fusion'`*.
  (3) Surface reconstruction with *`'surface_fusion'`*, where the
  color information is extracted from the used 2D images.
  Have a look at the HDevelop example
  `reconstruct_surface_mixed_camera_types.hdev` to see the 3D
  reconstruction process.
- **Set the image pairs (only for surface reconstruction):** —

  For the reconstruction of 3D surfaces, multiple binocular stereo
  reconstructions are performed, and then combined. For the binocular
  reconstruction, image pairs have to be specified. For example, for the
  three images shown above, the image pairs might be `[0,1]` and
  `[1,2]`. The image pairs have to be specified using

  - [`set_stereo_model_image_pairs`](set_stereo_model_image_pairs.md),

  and query the image pairs with

  - [`get_stereo_model_image_pairs`](get_stereo_model_image_pairs.md).

  For more information, see [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) as well as
  the above-mentioned operators.
- **Modify the stereo model parameters:** —

  With

  - [`set_stereo_model_param`](set_stereo_model_param.md),

  you can optimize the settings of the 3D reconstruction for your setup.

  When reconstructing surfaces, it is highly recommended to limit the 3D
  reconstruction using a bounding box which is as tight as possible
  around the object that is to be reconstructed.

  ![figure](../assets/ef2c406fdb31d166.svg)

  The bounding box, which is set with [`set_stereo_model_param`](set_stereo_model_param.md),
  restricts the area where the object is reconstructed, and thus can
  be used to reduce the runtime greatly.

  When using the *`'surface_fusion'`* `Method` in
  [`create_stereo_model`](create_stereo_model.md), it is recommended to first optimize the
  parameters of the *`'surface_pairwise'`* `Method`, since it
  is used as a basis. For more details on the parameters, see the examples
  `reconstruct_surface_stereo_pairwise_workflow.hdev` and
  `reconstruct_surface_stereo_fusion_workflow.hdev`.

  You can query the set parameters with

  - [`get_stereo_model_param`](get_stereo_model_param.md).
- **Perform the 3D reconstruction:** —

  Then, to perform the actual reconstruction, use

  - [`reconstruct_points_stereo`](reconstruct_points_stereo.md) or
  - [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md).
- **Get intermediate results (only for surface reconstruction):** —

  Note that to query these intermediate results, you must enable the
  *`'persistence'`* mode for the stereo model with
  [`set_stereo_model_param`](set_stereo_model_param.md) before performing the reconstruction.

  With

  - [`get_stereo_model_object`](get_stereo_model_object.md),

  you can access and inspect intermediate results of a surface
  reconstruction performed with [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md). These
  images can be used for troubleshooting the reconstruction process.

  With

  - [`get_stereo_model_object_model_3d`](get_stereo_model_object_model_3d.md),

  you can get the 3D object model that was reconstructed with
  [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) as an intermediate result using
  the `Method` *`'surface_fusion'`*.

---

#### List of Operators

- [`clear_stereo_model`](clear_stereo_model.md) — Free the memory of a stereo model.

- [`create_stereo_model`](create_stereo_model.md) — Create a HALCON stereo model.

- [`get_stereo_model_image_pairs`](get_stereo_model_image_pairs.md) — Return the list of image pairs set in a stereo model.

- [`get_stereo_model_object`](get_stereo_model_object.md) — Get intermediate iconic results of a stereo reconstruction.

- [`get_stereo_model_object_model_3d`](get_stereo_model_object_model_3d.md) — Get intermediate 3D object model of a stereo reconstruction

- [`get_stereo_model_param`](get_stereo_model_param.md) — Get stereo model parameters.

- [`reconstruct_points_stereo`](reconstruct_points_stereo.md) — Reconstruct 3D points from calibrated multi-view stereo images.

- [`reconstruct_surface_stereo`](reconstruct_surface_stereo.md) — Reconstruct surface from calibrated multi-view stereo images.

- [`set_stereo_model_image_pairs`](set_stereo_model_image_pairs.md) — Specify image pairs to be used for surface stereo reconstruction.

- [`set_stereo_model_param`](set_stereo_model_param.md) — Set stereo model parameters.
