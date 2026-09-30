## 2D Metrology

List of Operators ↓

This chapter contains operators for 2D metrology.

### Concept of 2D Metrology

With 2D metrology, you can measure the dimensions of objects that can be
represented by specific geometric primitives. The geometric shapes that can
be measured comprise circles, ellipses, rectangles, and lines. You need
approximate values for the positions, orientations, and dimensions of the
objects to measure. Then, the real edge positions of the objects in the image
are located near the boundaries of the approximate objects. With these edge
positions, the parameters of the geometric shapes are optimized to better fit
to the image data and are returned as measurement result.

The approximate values for the shape parameters of an object as well as some
parameters that control the measurement are stored in a data structure that
is called metrology object. The edges of the object in the image are located
within so-called measure regions. These are rectangular regions that are
arranged perpendicular to the boundaries of the metrology objects. Parameters
that adjust the dimension and distribution of the measure regions are
specified together with the approximate shape parameters for each metrology
object. When the measurement is applied, the edge positions inside all
measure regions are determined and fitted to geometric shapes using a RANSAC
algorithm. All metrology objects, all further information that is necessary
for the measurement, and the measurement results are stored in a data
structure that is called metrology model.

|  |  |
| --- | --- |
| ![figure](../assets/410e14694642624c.svg) | ![figure](../assets/225f6334b7c92740.svg) |
| ( 1) | ( 2) |

The geometric shapes in (1) are measured using
2D Metrology (2):
A metrology model with 4 metrology objects (blue contours) is created.
Using the edge positions (cyan crosses) located within the measure regions
(gray rectangles) for each metrology object, the geometric shapes
(green contours) are fitted and their parameters can be queried.
As shown for the circles, more than one instance per object can be found.
This image is from the example program `apply_metrology_model.hdev`.

In the following, the steps that are required to use 2D metrology are
described briefly.

- **Create the metrology model and specify the image size:** —

  First, a metrology model must be created using

  - [`create_metrology_model`](create_metrology_model.md).

  The metrology model is used as a container for one or more metrology
  objects. For an efficient measurement, after creating the metrology
  model, the image size of the image in which the measurements will be
  performed should be specified using

  - [`set_metrology_model_image_size`](set_metrology_model_image_size.md).
- **Provide approximate values:** —

  Then, metrology objects are added to the metrology model. Each
  metrology object consists of the approximate shape parameters for the
  corresponding object in the image and of the parameters that control
  the measurement. The parameters that control the measurement
  comprise, e.g., parameters that specify the dimension and distribution of
  the measure regions. Furthermore, several generic parameters can be
  adjusted for each metrology object. The metrology objects are
  specified with

  - [`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md) for circles,
  - [`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md) for ellipses,
  - [`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md) for rectangles, and
  - [`add_metrology_object_line_measure`](add_metrology_object_line_measure.md) for lines.
  - [`add_metrology_object_generic`](add_metrology_object_generic.md) allows to create metrology
    objects of different shapes (e.g., ellipse, circle,
    etc.) using one operator.

  To visually inspect the defined metrology objects, you can access
  their XLD contours with the operator
  [`get_metrology_object_model_contour`](get_metrology_object_model_contour.md). To visually inspect the
  created measure regions, you can access their XLD contours with the
  operator [`get_metrology_object_measures`](get_metrology_object_measures.md).
- **Modify the model parameters:** —

  If a camera calibration has been performed, the camera parameters and
  the pose of the measurement plane can be set with

  - [`set_metrology_model_param`](set_metrology_model_param.md).

  Then, the result of the measurements returned by
  [`get_metrology_object_result`](get_metrology_object_result.md) will be in world coordinates. The
  reference coordinate system in which the metrology objects are
  defined can also be changed with [`set_metrology_model_param`](set_metrology_model_param.md).
- **Modify object parameters:** —

  Many parameters can be set when adding the metrology objects to the
  metrology model. Some of them can also be modified afterwards using
  the operator

  - [`set_metrology_object_param`](set_metrology_object_param.md).
- **Align the metrology model:** —

  To translate and rotate the metrology model before the next
  measurement is performed, you can use the operator

  - [`align_metrology_model`](align_metrology_model.md).

  An alignment is temporary and is replaced by the next
  alignment. The metrology model itself is not changed. Note that
  typically the alignment parameters are obtained using shape-based
  matching.
- **Apply the measurement:** —

  The actual measurement in the image is performed with

  - [`apply_metrology_model`](apply_metrology_model.md).

  The operator locates the edges within the measure regions and fits
  the specified geometric shape to the edge positions using a RANSAC
  algorithm. The edges are located internally using the operator
  [`measure_pos`](measure_pos.md) or [`fuzzy_measure_pos`](fuzzy_measure_pos.md) (see also chapter
  [1D Measuring](toc_1dmeasuring.md)). The latter uses fuzzy
  methods and is used only if at least one fuzzy function was set via
  [`set_metrology_object_fuzzy_param`](set_metrology_object_fuzzy_param.md) before applying the
  measurement. If more than one instance of the returned object
  shape is needed (compare image above), the generic parameter
  *`"num_instances"`* must be set to the number of instances
  that should be returned. The parameter can be set when adding the
  individual metrology objects or afterwards with the operator
  [`set_metrology_object_param`](set_metrology_object_param.md).
- **Access the results:** —

  After the measurement, the results can be accessed. The parameters
  of the adapted geometric shapes of the objects are queried with
  the operator

  - [`get_metrology_object_result`](get_metrology_object_result.md).

  Querying only the edges used for the returned result and their
  amplitudes is also done using [`get_metrology_object_result`](get_metrology_object_result.md).

  The row and column coordinates of all located edges can be
  accessed with

  - [`get_metrology_object_measures`](get_metrology_object_measures.md).

  To visualize the adapted geometric shapes, you can access their
  XLD contours with

  - [`get_metrology_object_result_contour`](get_metrology_object_result_contour.md).

### Further operators

In addition to the operators mentioned above, you can copy the metrology
handle with [`copy_metrology_model`](copy_metrology_model.md), write the metrology model to file
with [`write_metrology_model`](write_metrology_model.md), read a model from file again using
[`read_metrology_model`](read_metrology_model.md), and serialize or deserialize a metrology model
using [`serialize_metrology_model`](serialize_metrology_model.md) or
[`deserialize_metrology_model`](deserialize_metrology_model.md).

Furthermore, you can query various information from the metrology model. For
example, you can query the indices of the metrology objects with
[`get_metrology_object_indices`](get_metrology_object_indices.md), query parameters that are valid for the
entire metrology model with [`get_metrology_model_param`](get_metrology_model_param.md), query a fuzzy
parameter of a metrology model with [`get_metrology_object_fuzzy_param`](get_metrology_object_fuzzy_param.md),
query the number of instances of the metrology objects of a metrology model
with [`get_metrology_object_num_instances`](get_metrology_object_num_instances.md), and query the current
configuration of the metrology model with
[`get_metrology_object_param`](get_metrology_object_param.md).

Additionally, you can reset all parameters of a metrology model using
[`reset_metrology_object_param`](reset_metrology_object_param.md) or reset only all fuzzy parameters and fuzzy
functions of a metrology model using
[`reset_metrology_object_fuzzy_param`](reset_metrology_object_fuzzy_param.md).

### Glossary

In the following, the most important terms that are used in the context of 2D
Metrology are described.

- **metrology model** —

  Data structure that contains all metrology objects, all information
  needed for the measurement, and the measurement results.
- **metrology object** —

  Data structure for the object to be measured with 2D metrology. The
  metrology object is represented by a specific geometric shape for
  which the shape parameters are approximately known. Additionally, it
  contains parameters that control the measurement, e.g., parameters
  that specify the dimension and distribution of the measure regions.
- **measure regions** —

  Rectangular regions that are arranged perpendicular to the
  boundaries of the approximate objects. Within these regions the
  edges that are used to get the exact shape parameters of the
  metrology objects are extracted.
- **returned instance of a metrology object** —

  For each metrology object, different instances of the object can be
  returned by the measurement, e.g., if parallel structures of the
  same shape exist near to the boundaries of the approximated
  geometric shape (see image above). The sequence of the returned
  instances is arbitrary, i.e., it is no measure for the quality of
  the fitting.

### Further Information

See also the `“Solution Guide on 2D Measuring”` for further details
about 2D metrology.

---

#### List of Operators

- [`add_metrology_object_circle_measure`](add_metrology_object_circle_measure.md) — Add a circle or a circular arc to a metrology model.

- [`add_metrology_object_ellipse_measure`](add_metrology_object_ellipse_measure.md) — Add an ellipse or an elliptic arc to a metrology model.

- [`add_metrology_object_generic`](add_metrology_object_generic.md) — Add a metrology object to a metrology model.

- [`add_metrology_object_line_measure`](add_metrology_object_line_measure.md) — Add a line to a metrology model.

- [`add_metrology_object_rectangle2_measure`](add_metrology_object_rectangle2_measure.md) — Add a rectangle to a metrology model.

- [`align_metrology_model`](align_metrology_model.md) — Alignment of a metrology model.

- [`apply_metrology_model`](apply_metrology_model.md) — Measure and fit the geometric shapes of all metrology objects of
  a metrology model.

- [`clear_metrology_model`](clear_metrology_model.md) — Delete a metrology model and free the allocated memory.

- [`clear_metrology_object`](clear_metrology_object.md) — Delete metrology objects and free the allocated memory.

- [`copy_metrology_model`](copy_metrology_model.md) — Copy a metrology model.

- [`create_metrology_model`](create_metrology_model.md) — Create the data structure that is needed to measure geometric shapes.

- [`deserialize_metrology_model`](deserialize_metrology_model.md) — Deserialize a serialized metrology model.

- [`get_metrology_model_param`](get_metrology_model_param.md) — Get parameters that are valid for the entire metrology model.

- [`get_metrology_object_fuzzy_param`](get_metrology_object_fuzzy_param.md) — Get a fuzzy parameter of a metrology model.

- [`get_metrology_object_indices`](get_metrology_object_indices.md) — Get the indices of the metrology objects of a metrology model.

- [`get_metrology_object_measures`](get_metrology_object_measures.md) — Get the measure regions and the results of the edge location for the
  metrology objects of a metrology model.

- [`get_metrology_object_model_contour`](get_metrology_object_model_contour.md) — Query the model contour of a metrology object in image coordinates.

- [`get_metrology_object_num_instances`](get_metrology_object_num_instances.md) — Get the number of instances of the metrology objects of a metrology model.

- [`get_metrology_object_param`](get_metrology_object_param.md) — Get one or several parameters of a metrology model.

- [`get_metrology_object_result`](get_metrology_object_result.md) — Get the results of the measurement of a metrology model.

- [`get_metrology_object_result_contour`](get_metrology_object_result_contour.md) — Query the result contour of a metrology object.

- [`read_metrology_model`](read_metrology_model.md) — Read a metrology model from a file.

- [`reset_metrology_object_fuzzy_param`](reset_metrology_object_fuzzy_param.md) — Reset all fuzzy parameters and fuzzy functions of a metrology
  model.

- [`reset_metrology_object_param`](reset_metrology_object_param.md) — Reset all parameters of a metrology model.

- [`serialize_metrology_model`](serialize_metrology_model.md) — Serialize a metrology model.

- [`set_metrology_model_image_size`](set_metrology_model_image_size.md) — Set the size of the image of metrology objects.

- [`set_metrology_model_param`](set_metrology_model_param.md) — Set parameters that are valid for the entire metrology model.

- [`set_metrology_object_fuzzy_param`](set_metrology_object_fuzzy_param.md) — Set fuzzy parameters or fuzzy functions for a metrology model.

- [`set_metrology_object_param`](set_metrology_object_param.md) — Set parameters for the metrology objects of a metrology model.

- [`write_metrology_model`](write_metrology_model.md) — Write a metrology model to a file.
