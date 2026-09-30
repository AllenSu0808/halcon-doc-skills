# write_object_model_3d (Operator)

## Name

`write_object_model_3d` — Writes a 3D object model to a file.

## Signature

`write_object_model_3d( : : ObjectModel3D, FileType, FileName, GenParamName, GenParamValue : )`

## Description

The operator `write_object_model_3d` writes the 3D object model
*`ObjectModel3D`* to the file *`FileName`*. The object model
can be read again with [`read_object_model_3d`](read_object_model_3d.md), or can be
imported into an appropriate CAD program. Please note, that primitives
may only be stored in the HALCON format *'om3'*. Should it be
necessary to store the primitives in another format, the operator
[`sample_object_model_3d`](sample_object_model_3d.md) has to be called beforehand. However,
this results in a transformation of the primitives into 3D points and
therefore only corresponds to an approximation of the primitives.

All coordinates are written in meters. If the file is read later using
[`read_object_model_3d`](read_object_model_3d.md), the parameter Scale must be set to
*'m'* to avoid scaling the data.

The parameter *`FileType`* determines the type of the file. The
following types are supported by this operator:

- ***'om3'*:** —

  HALCON format for object model 3D. Files with this format can be
  read by [`read_object_model_3d`](read_object_model_3d.md).
  The default file extension for this format is 'om3'.
- ***'dxf'*:** —

  AUTOCAD format. See [`read_object_model_3d`](read_object_model_3d.md) for details
  about reading this file format.
  The default file extension for this format is 'dxf'.
- ***'off'*:** —

  Object File Format. This is an ASCII-based format that can hold
  3D points and polygons.
  The default file extension for this format is 'off'.
- ***'ply'*,** —
- ***'ply_binary'*:** —

  Polygon File Format (also Stanford Triangle Format).
  This is a simple format that can hold 3D points, point
  normals, polygons, color information and point-based extended attributes.
  HALCON supports the writing of both the ASCII and the binary version of
  this format.
  The default file extension for this format is 'ply'.
- ***'obj'*:** —

  OBJ file format, also Wavefront OBJ-Format. This is an
  ASCII-based format that can hold 3D points, polygons, normals,
  and triangles, which are stored as polygons.
  The default file extension for this format is 'obj'.
- ***'stl'*,** —
- ***'stl_binary'*,** —
- ***'stl_ascii'*:** —

  STL file format, also 'Stereolithography format',
  'SurfaceTesselationLanguage ', 'StandardTriangulationLanguage', and
  'StandardTesselationLanguage'.
  This format stores triangles and triangle normals. However, as
  triangle normals are not supported by HALCON 3D object models and
  point normals (which are, for example, calculated by
  [`surface_normals_object_model_3d`](surface_normals_object_model_3d.md)) are not supported by the STL
  format, no normals are written to file. If the 3D object model contains
  polygons, they are converted to triangles before before writing them to
  disc. If the file type is set to *'stl'* or *'stl_binary'*,
  the binary version of STL is written while *'stl_ascii'* selects
  the ASCII version. The default file extension for this format is 'stl'.

A set of additional optional parameters can be set. The names and values
of the parameters are passed in *`GenParamName`* and
*`GenParamValue`*, respectively. Some of the optional parameters
can only be set for a certain file type. The following values for
*`GenParamName`* are possible:

- ***'invert_normals'*:** —

  Invert normals and face orientation before saving the 3D object model.
  If this value is set to *'true'*, for the formats *'off'*,
  *'ply'*, *'obj'*, and *'stl'* the orientation of
  faces (triangles and polygons) is inverted . For formats that support
  point normals (*'ply'*,*'obj'*), all normals are inverted
  before writing them to disc. Note that for the types *'om3'* and
  *'dxf'* the parameter has no effect.

  *Valid for formats:* *'off'*, *'ply'*,
  *'obj'*, *'stl'*.
  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model.

**`FileType`** (input_control)  string `→`  (string)

Type of the file that is written.

Default:
'om3'

List of values:
'dxf', 'obj', 'off', 'om3', 'ply', 'ply_binary', 'stl', 'stl_ascii', 'stl_binary'

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file that is written.

File extension:
.`off`, .`ply`, .`dxf`, .`om3`, .`obj`, .`stl`

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'invert_normals'

**`GenParamValue`** (input_control)  string(-array) `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
'true', 'false'

## Result

The operator `write_object_model_3d` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct and the file can be written.
If necessary, an exception will be raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`

## Possible Successors

`read_object_model_3d`

## See also

`read_object_model_3d`

## Module

3D Metrology
