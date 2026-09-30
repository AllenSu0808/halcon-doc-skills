# read_object_model_3d (Operator)

## Name

`read_object_model_3d` — Read a 3D object model from a file.

## Signature

`read_object_model_3d( : : FileName, Scale, GenParamName, GenParamValue : ObjectModel3D, Status)`

## Description

The operator `read_object_model_3d` reads a 3D object model from
the file *`FileName`* and returns a 3D object model handle in
*`ObjectModel3D`*.

The operator supports the following file formats:

- ***'om3'*:** —

  HALCON format for 3D object model. Files with this format can be
  written by [`write_object_model_3d`](write_object_model_3d.md).
  The default file extension for this format is 'om3'.
- ***'dxf'*:** —

  AUTOCAD format.
  HALCON supports only the ASCII version of the format.
  See below for details about reading this file format.
  The default file extension for this format is 'dxf'.
- ***'off'*:** —

  Object File Format. This is a simple ASCII-based format that can hold
  3D points and polygons. The binary OFF format is not supported.
  The default file extension for this format is 'off'.
- ***'ply'*:** —

  Polygon File Format (also Stanford Triangle Format).
  This is a simple format that can hold 3D points, point
  normals, polygons, color information and point-based extended attributes.
  HALCON supports both the ASCII and the binary version of the format.
  If the file to be read contains unsupported information, the additional
  data is ignored and only the supported data is read.
  If the name of a `property` entry of a 'ply' file coincides with
  the name of a standard
  attribute (see [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md)), the property will
  preferably be read into the standard attribute.
  The default file extension for this format is 'ply'.
- ***'obj'*:** —

  OBJ file format, also 'Wavefront OBJ-Format'. This is an
  ASCII-based format that can hold 3D points, polygons, normals,
  texture coordinates, materials and other information.
  HALCON supports points ('v'-lines), point normals ('vn'-lines) and
  polygonal faces ('f'-lines).
  Existing point normals are only returned if there are exactly as many
  point normals as there are points.
  Other entities are ignored.
  The default file extension for this format is 'obj'.
- ***'stl'*,** —
- ***'stl_binary'*,** —
- ***'stl_ascii'*:** —

  STL file format, also 'Stereolithography format',
  'SurfaceTesselationLanguage ', 'StandardTriangulationLanguage', and
  'StandardTesselationLanguage'.
  This format stores triangles and triangle normals.
  However, as triangle normals are not supported by HALCON 3D
  object models, only triangles are read while the triangle normals
  are ignored. Normals are recomputed from the triangles if required.
  HALCON reads both the ASCII and the binary version of this format.
  If *'stl'* is set, HALCON will auto-detect the type. Setting the
  type to *'stl_binary'* or *'stl_ascii'* will enforce the
  corresponding format.
  The default file extension for this format is 'stl'.
- ***'step'*:** —

  STEP file format, also STP or 'Standard for the Exchange of Product Model
  Data'.
  This is a complex format that stores a large variety of geometrical
  definitions which allows an accurate storage of 3D models. Due to the
  limited support for the geometrical structures defined by STEP in HALCON
  3D object models, triangulation is performed on these geometries, resulting
  in models comprised of triangle meshes.
  The default file extensions for this format are 'step' and 'stp'.
- ***'generic_ascii'*:** —

  This format can be used to read different ASCII files containing 3D data in
  tabular form, e.g. 'ptx', 'pts', 'xyz' or 'pcd'. Currently, only
  point based attributes are supported, no triangles or polygons. The
  information for each 3D point is expected to be written in a single line,
  one point at a time. The file format must be further specified by setting
  the generic parameter *'ascii_format'*.

When reading a DXF file, the output parameter *`Status`* contains
information about the number of 3D faces that were read and, if necessary,
warnings that parts of the DXF file could not be interpreted.

The parameter *`Scale`* defines the scale of the file. For example,
if the parameter is set to *'mm'*, all units in the file are
assumed to have the unit *'mm'* and are transformed into the
usual HALCON-internal unit *'m'* by multiplication with *0.001*.
A value of *'100 mm'* thus becomes *'0.1 m'*.
Alternatively, a scaling factor can be passed to *`Scale`*, which is
multiplied with all coordinate values found in the file.
The relation of units to scaling factors is given in the following table:

| Unit | Scaling factor |
| --- | --- |
| m | 1 |
| dm | 0.1 |
| cm | 0.01 |
| mm | 0.001 |
| um, microns | 1e-6 |
| nm | 1e-9 |
| km | 1000 |
| in | 0.0254 |
| ft | 0.3048 |
| yd | 0.9144 |

Note that the parameter *`Scale`* is ignored for files of type
*'om3'* and *'step'*. om3-files are always read without any
scale changes. For step-files, the unit is directly defined in the files,
read along with the stored data and used to scale to the HALCON-internal
unit *'m'*.
For changing the scale manually after reading a 3D object model,
use [`affine_trans_object_model_3d`](affine_trans_object_model_3d.md).

A set of additional optional parameters can be set. The names and values
of the parameters are passed in *`GenParamName`* and
*`GenParamValue`*, respectively. Some of the optional parameters
can only be set for a certain file type. The following values for
*`GenParamName`* are possible:

- ***'file_type'*:** —

  Forces a file type.
  If this parameter is not set, the operator
  `read_object_model_3d` tries to auto-detect the file type
  using the file ending and the file header.
  If the parameter is set, the given file is interpreted as this
  file format.

  List of values:
   *'om3'*, *'dxf'*,
  *'off'*, *'ply'*,
  *'obj'*, *'stl'*,
  *'step'*, *'generic_ascii'*.
- ***'convert_to_triangles'*:** —

  Convert all faces to triangles.
  If this parameter is set to *'true'*, all faces read from
  the file are converted to triangles.

  *Valid for formats:* *'dxf'*, *'ply'*,
  *'off'*, *'obj'*.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'invert_normals'*:** —

  Invert normals and face orientations.
  If this parameter is set to *'true'*, the orientation of
  all normals and faces is inverted.

  *Valid for formats:* *'dxf'*, *'ply'*,
  *'off'*, *'obj'*,
  *'stl'*, *'step'*,
  *'generic_ascii'*.

  List of values:
   *'true'*, *'false'*.

  Default:
   *'false'*.
- ***'max_approx_error'*, *'min_num_points'*:** —

  DXF-specific parameters (see below).

  *Valid for formats:* *'dxf'*.
- ***'max_surface_deviation'*:** —

  STEP-specific parameter.

  Specifies the maximum allowed deviation (in *'m'*) from the
  model surface during the triangulation. A smaller value will generate
  a more accurate model but will also increase the reading time and the
  number of points and triangles in the resulting model. Set the parameter
  to *'auto'* in order to estimate it automatically depending on the
  size of the model.

  *Valid for formats:* *'step'*.

  Suggested values:
   *'auto'*, *0.0001*, *0.00001*.

  Default:
   *'auto'*.

  Restriction:
   *'max_surface_deviation'* > *0*
- ***'split_level'*:** —

  STEP-specific parameter.

  STEP files can contain definitions of independent model components.
  With this parameter, each component can be imported as a HALCON 3D object
  model. If the parameter is set to *0*, the file is imported as a
  single model. With *1* the model components are roughly separated
  from each other, while *2* separates the model components at a more
  detailed level.

  *Valid for formats:* *'step'*.

  List of values:
   *0*, *1*, *2*.

  Default:
   *0*.
- ***'ascii_format'*:** —

  generic_ascii-specific parameter.

  Specifies the format of the ASCII file to be read. As value, a dict containing
  information about the file content must be provided. The dict defines the columns
  to be read and meta-data like the first line number containing point information.
  Examples are given at the bottom of the operator reference or in the HDevelop
  example `read_object_model_3d_generic_ascii.hdev`.
  The following parameters can be set as dict keys:

  - ***'columns'*: (mandatory)** —

    Defines the column attributes in the read file, given as a tuple of
    strings. All point-related standard and extended attributes as
    listed in the reference of [`set_object_model_3d_attrib`](set_object_model_3d_attrib.md) are
    supported. At least, *'point_coord_x'*, *'point_coord_y'*
    and *'point_coord_z'* must be set. When setting normals, all
    three components *'point_normal_x'*, *'point_normal_y'*
    and *'point_normal_z'* must be set. Ignoring columns is possible
    by setting *''* at the according tuple position.

    Suggested values:
     *['point_coord_x', 'point_coord_y', 'point_coord_z']*,
    *['point_normal_x', 'point_normal_y', 'point_normal_z']*,
    *'red'*, *'green'*, *'blue'*,
    *'&my_custom_attrib'*, *''*.
  - ***'separator'*: (mandatory)** —

    Defines the separator between the columns. Currently, whitespaces (blanks or
    tabs), semicolons and commas are supported.

    List of values:
     *' '*, *';'*, *','*.
  - ***'first_point_line'*: (optional)** —

    Describes the number of the first line to be read from the file and can e.g.
    be used to skip header information. The top line in the file corresponds to
    *'first_point_line'* *1*.

    Default:
     *1*.

    Restriction:
     *'first_point_line'* > *0*
  - ***'last_point_line'*: (optional)** —

    Describes the number of the last line to be read from the file and can e.g.
    be used to skip unsupported information. The top line in the file
    corresponds to *'last_point_line'* *1*. When
    *'last_point_line'* is set to *-1*, all lines are read.

    Default:
     *-1*.

    Restriction:
     *'last_point_line'* >= -1
  - ***'comment'*: (optional)** —

    Describes the start of comments in the read file. Information behind the
    comment start are ignored when reading the file.

    Suggested values:
     *'#'*, *'*'*, *'/'*,
    *'comment'*.

  *Valid for formats:* *'generic_ascii'*.
- ***'xyz_map_width'*:** —

  Creates for the read 3D object model a mapping that assigns an image
  coordinate to each read 3D point, as in
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
  It is assumed that the read file contains the 3D points row-wise.
  The passed value is used as width of the image.
  The height of the image is computed automatically.
  If this parameter is set, the read 3D object model can be projected
  by [`object_model_3d_to_xyz`](object_model_3d_to_xyz.md) using the method
  *'from_xyz_map'*.
  Only one of the two parameters *'xyz_map_width'* and
  *'xyz_map_height'* can be set.

  *Valid for formats:* *'ply'*, *'off'*,
  *'obj'*, *'generic_ascii'*.

  Default:
   *-1*.

  Restriction:
   *'xyz_map_width'* > 0
- ***'xyz_map_height'*:** —

  As *'xyz_map_width'*, but assuming that the 3D points are
  aligned column-wise.
  The width of the image is computed automatically.
  Only one of the two parameters *'xyz_map_width'* and
  *'xyz_map_height'* can be set.

  *Valid for formats:* *'ply'*, *'off'*,
  *'obj'*, *'generic_ascii'*.

  Default:
   *-1*.

  Restriction:
   *'xyz_map_height'* > 0

Note that in many cases, it is recommended to use the 2D mapping data,
if available, for speed and robustness reasons. This is beneficial
especially when using [`sample_object_model_3d`](sample_object_model_3d.md),
[`surface_normals_object_model_3d`](surface_normals_object_model_3d.md), or when preparing a 3D object
model for surface-based matching, e.g., smoothing, removing outliers, and
reducing the domain.

The operator `read_object_model_3d` supports the following
DXF entities:

- POLYLINE

  - Polyface meshes (Polyline flag 64)
  - 3D Polylines (Polyline flag 8,9)
  - 2D Polylines (Polyline flag 0)
- LWPOLYLINE

  - 2D Polylines
- 3DFACE
- LINE
- CIRCLE
- ARC
- SOLID
- BLOCK
- INSERT

The two-dimensional linear DXF entities LINE, CIRCLE and ARC are not
interpreted as faces. Only if these elements are extruded, the resulting
faces are inserted in the 3D object model. All elements that represent
no faces but lines are added as 3D lines to the 3D object model.

The curved surface of extruded DXF entities of the type CIRCLE and ARC is
approximated by planar faces. The accuracy of this approximation can be
controlled with the two generic parameters *'min_num_points'* and
*'max_approx_error'*. The parameter *'min_num_points'* defines
the minimum number of sampling points that are used for the approximation of
the DXF element CIRCLE or ARC. Note that the parameter
*'min_num_points'* always refers to the full circle, even for ARCs,
i.e., if *'min_num_points'* is set to *50* and a DXF entity of
the type ARC is read that represents a semi-circle, this semi-circle is
approximated by at least 25 sampling points. The parameter
*'max_approx_error'* defines the maximum deviation of the XLD contour
from the ideal circle. The determination of this deviation is carried out in
the units used in the DXF file. For the determination of the accuracy of the
approximation both criteria are evaluated. Then, the criterion that leads to
the more accurate approximation is used.

Internally, the following default values are used for the generic
parameters:

- *'min_num_points'* = *20*
- *'max_approx_error'* = *0.25*

To achieve a more accurate approximation, either the value for
*'min_num_points'* must be increased or the value for
*'max_approx_error'* must be decreased.

One possible way to create a suitable DXF file is to create a 3D model of the
object with the CAD program AutoCAD. Ensure that the surface of the object
is modeled, not only its edges. Lines that, e.g., define object edges, will
not be used by HALCON, because they do not define the surface of the object.
Once the modeling is completed, you can store the model in DWG format. To
convert the DWG file into a DXF file that is suitable for HALCON's 3D
matching, carry out the following steps:

- Export the 3D CAD model to a 3DS file using the 3dsout command
  of AutoCAD. This will triangulate the object's surface, i.e.,
  the model will only consist of planes. (Users of AutoCAD 2007
  or newer versions can download this command utility from
  Autodesk's web site.)
- Open a new empty sheet in AutoCAD.
- Import the 3DS file into this empty sheet with the 3dsin command
  of AutoCAD.
- Save the object into a DXF R12 file.

Users of other CAD programs should ensure that the surface of the 3D model
is triangulated before it is exported into the DXF file. If the CAD program
is not able to carry out the triangulation, it is often possible to save
the 3D model in the proprietary format of the CAD program and to convert
it into a suitable DXF file by using a CAD file format converter that is
able to perform the triangulation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

Filename of the file to be read.

Default:
'mvtec_bunny_normals'

Suggested values:
'mvtec_bunny', 'glass_mug', 'bmc_mini', 'pipe_joint', 'clamp_sloped', 'tile_spacer', 'engine_part_bearing'

File extension:
.`off`, .`ply`, .`dxf`, .`om3`, .`obj`, .`stl`, .`step`, .`stp`

**`Scale`** (input_control)  number `→`  (string / real / integer)

Scale of the data in the file.

Default:
'm'

Suggested values:
'm', 'cm', 'mm', 'microns', 'um', 'nm', 'km', 'in', 'ft', 'yd', 1.0, 0.01, 0.001, 1.0e-6, 0.0254, 0.3048, 0.9144

**`GenParamName`** (input_control)  string(-array) `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'ascii_format', 'convert_to_triangles', 'file_type', 'invert_normals', 'max_approx_error', 'max_surface_deviation', 'min_num_points', 'split_level', 'xyz_map_height', 'xyz_map_width'

**`GenParamValue`** (input_control)  string(-array) `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
'true', 'false', 1, 0, 'auto', 'om3', 'off', 'ply', 'dxf', 'obj', 'stl', 'stl_binary', 'stl_ascii', 'step', 'generic_ascii'

**`ObjectModel3D`** (output_control)  object_model_3d(-array) `→`  (handle)

Handle of the 3D object model.

**`Status`** (output_control)  string(-array) `→`  (string)

Status information.

## Example (HDevelop)

```
* Example how to use file_type generic_ascii and generic parameter ascii_format to read the point attributes from a ply file.
FileFormat := dict{}
FileFormat.separator := ' '
FileFormat.columns := ['point_coord_x', 'point_coord_y', 'point_coord_z', 'point_normal_x', 'point_normal_y', 'point_normal_z']
FileFormat.first_point_line := 14
FileFormat.last_point_line := 2273
FileFormat.comment := 'comment'
read_object_model_3d ('glass_mug.ply', 'm', ['file_type', 'ascii_format'], ['generic_ascii', FileFormat], ObjectModel3D, Status)
```

## Result

The operator `read_object_model_3d` returns the value
2 (
H_MSG_TRUE)
if the given parameters are correct, the file can be read,
and the file is valid.
If the file format is unknown or cannot be determined, the error
9512 is raised.
If the file is invalid, the error 9510 is raised.
If necessary, an exception will be raised.

## Possible Predecessors

`write_object_model_3d`

## Possible Successors

`affine_trans_object_model_3d`,
`object_model_3d_to_xyz`,
`prepare_object_model_3d`

## Alternatives

`xyz_to_object_model_3d`

## See also

`write_object_model_3d`,
`clear_object_model_3d`

## Module

3D Metrology
