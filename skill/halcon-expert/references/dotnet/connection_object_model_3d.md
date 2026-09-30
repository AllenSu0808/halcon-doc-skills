# ConnectionObjectModel3d (Operator)

## Name

`ConnectionObjectModel3d` — Determine the connected components of the
3D object model.

## Signature

`static void HOperatorSet.ConnectionObjectModel3d(HTuple objectModel3D, HTuple feature, HTuple value, out HTuple objectModel3DConnected)`

`static HObjectModel3D[] HObjectModel3D.ConnectionObjectModel3d(HObjectModel3D[] objectModel3D, HTuple feature, HTuple value)`

`HObjectModel3D[] HObjectModel3D.ConnectionObjectModel3d(string feature, double value)`

## Description

`ConnectionObjectModel3d` determines the connected components
of the input 3D object model given in *`objectModel3D`*. The decision
if two parts of the 3D object model are connected can be based on
different attributes and respective distance functions.
The attribute and distance function can be selected in *`feature`*:

- ***"distance_3d"*:** —

  The euclidean distance between the point coordinates of the
  set of the 3D points are tested. For any distance below *`value`*
  the points are considered as connected.
- ***"angle"*:** —

  The angles between the normals of the points in the 3D object model
  are compared. Similar normals are considered as connected if their
  angular distance is below *`value`*. *`value`* is
  specified in radians and should be between 0 and pi.

  Prerequisite: The 3D object model must contain normals, which can
  be computed with [`SurfaceNormalsObjectModel3d`](surface_normals_object_model_3d.md).
- ***"distance_mapping"*:** —

  The mapping measures the distance between the pixel coordinates of
  points in the 3D object model that are stored in the 2D mapping.
  Use a value larger than 1.5 for *`value`* to get a connection
  in an 8-neighborhood in the image.

  Prerequisite: The 3D object model must contain a 2D mapping, which is
  available if the 3D object model has been created with
  [`XyzToObjectModel3d`](xyz_to_object_model_3d.md).
- ***"mesh"*:** —

  Returns parts of the 3D object model that are connected with
  triangles or polygons. *`value`* is ignored.

  Prerequisite: The 3D object model must provide a triangulation, which can
  be obtained with [`TriangulateObjectModel3d`](triangulate_object_model_3d.md). Alternatively,
  if the 3D object model already contains a 2D mapping,
  [`PrepareObjectModel3d`](prepare_object_model_3d.md) can be used with
  `purpose` set to *"segmentation"*
  to quickly triangulate the 3D object model.
- ***"lines"*:** —

  Returns parts of the object model that are connected by lines.
  *`value`* is ignored.

  Prerequisite: The 3D object model must contain polylines, which can be
  computed with [`IntersectPlaneObjectModel3d`](intersect_plane_object_model_3d.md).

Alternatively, the required attributes can be set manually with
[`SetObjectModel3dAttrib`](set_object_model_3d_attrib.md) or
[`SetObjectModel3dAttribMod`](set_object_model_3d_attrib_mod.md). Note that the 3D object model might
already contain the required attribute, especially if the 3D object model
has been read with [`ReadObjectModel3d`](read_object_model_3d.md) or if it has been
deserialized with [`DeserializeObjectModel3d`](deserialize_object_model_3d.md). To check whether the
required attribute is available, use [`GetObjectModel3dParams`](get_object_model_3d_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`objectModel3D`** (input_control)  object_model_3d(-array) `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model.

**`feature`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Attribute used to calculate the connected
components.

Default:
"distance_3d"

List of values:
"angle", "distance_3d", "distance_mapping", "lines", "mesh"

**`value`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum value for the distance between two
connected components.

Default:
1.0

Suggested values:
1.0, 1.1, 1.5, 10.0, 100.0

**`objectModel3DConnected`** (output_control)  object_model_3d-array `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object models that represent
the connected components.

## Example (HDevelop)

```
gen_object_model_3d_from_points (rand(100), rand(100),\
                                 rand(100), ObjectModel3D)
connection_object_model_3d (ObjectModel3D, 'distance_3d', 0.2,\
                            ObjectModel3DConnected)
dev_get_window (WindowHandle)
visualize_object_model_3d (WindowHandle, [ObjectModel3DConnected], [], [],\
                           ['colored'], [12], [], [], [], PoseOut)
```

## Result

`ConnectionObjectModel3d` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`,
`SelectPointsObjectModel3d`

## Possible Successors

`ProjectObjectModel3d`,
`ObjectModel3dToXyz`,
`SelectObjectModel3d`

## See also

`SelectObjectModel3d`,
`SelectPointsObjectModel3d`

## Module

3D Metrology
