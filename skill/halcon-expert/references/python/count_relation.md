# count_relation (Operator)

## Name

`count_relation` — Number of entries in the HALCON database.

## Signature

`def count_relation(relation_name: str) -> int`

## Description

`count_relation` returns the number of entries *`num_of_tuples`*
in the relation *`relation_name`* of the HALCON database since the
database was switched on with the [`set_system`](set_system.md) parameter
*"database"*.
If the database is disabled, *`num_of_tuples`* is 0 and in addition
a warning is raised if *"do_low_error"* is set with
[`set_system`](set_system.md).
The state of the database can be
queried by the parameter *"database"* of [`get_system`](get_system.md).

The HALCON database is organized in five tables called relations. The
entries in this relations are called tuples (not to mix up
with HALCON tuples naming object arrays). If enabled,
the HALCON database contains the basic relations for region data,
image matrices, and XLDs, as well as the container relations for HALCON
objects and HALCON tuples (i.e., object arrays).
The HALCON objects region and image are constructed from elements from
the region-data relations and the image-matrix relations.
A region consists of a
pointer to a tuple in the region-data relation. An image consists
of a pointer to a tuple in the region-data relation and
additionally of one or more pointers to tuples in the matrix relation.
Multi-channel images have multiple matrix pointers.

Both regions and images are called objects. A region can be considered
as the special case of an iconic object having no image matrices.
For reasons of an efficient memory management, the tuples of the
region-data relation and the image-matrix relation
will be used by different objects together.
Therefore there may be more images than image matrices.
Only the three low-level relations *"image"*, *"region"*,
and *"XLD"* are of relevance to the memory consumption.
Image objects (regions as well as images) consist only of references
on region and matrix data and therefore only need a couple of bytes
of memory.

Possible values for *`relation_name`*:

- **'image':** —

  Image matrices. One matrix may be the component of multiple images
  (no redundant storage).
- **'region':** —

  Regions and image domains.
  One region may be the component of multiple image objects
  (no redundant storage).
- **'XLD':** —

  eXtended Line Description: Contours, polygons, parallels,
  lines, etc. XLD data types don't have gray values and are stored
  with subpixel accuracy.
- **'object':** —

  Iconic objects. Composed of a region (see *"region"*) and
  optionally image matrices (see *"image"*).
- **'tuple':** —

  In the compact mode, tuples of iconic objects are stored as a
  surrogate in this relation.
  Instead of working with the individual object keys, only this
  tuple key is used. It depends on the host language, whether the
  objects are passed individually (e.g., C++) or as tuples (e.g.,
  C).

Certain database objects will be created already by the operator
[`reset_obj_db`](reset_obj_db.md) and therefore have to be available all the time
(the undefined gray value component, the objects 'full'
(FULL_REGION in HALCON/C) and 'empty' (EMPTY_REGION in HALCON/C)
as well as the herein included empty and full region).
By calling [`get_channel_info`](get_channel_info.md), the operator therefore appears
correspondingly also as 'creator' of the full and empty region.
The operator can be used for example to check the completeness
of the [`clear_obj`](clear_obj.md) operation.

## Attention

Collecting database information is not thread-safe when passing iconic
objects between threads, meaning when deleting objects in a different
thread than generating them.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`relation_name`** (input_control)  string `→` str

Relation of interest of the HALCON database.

Default:
"object"

List of values:
"XLD", "image", "object", "region", "tuple"

**`num_of_tuples`** (output_control)  integer `→` int

Number of tuples in the relation.

## Example (HDevelop)

```
* Close the graphics window in order to close the graphics stack,
* which would influence the measurement.
dev_close_window ()
* Enable the measurement.
set_system ('database','true')
*
count_relation ('image', I1)
count_relation ('region', R1)
count_relation ('XLD', X1)
count_relation ('object', O1)
count_relation ('tuple', T1)
*
* Result:
* I1 = 0
* R1 = 0
* X1 = 0
* O1 = 0
* T1 = 0
*
read_image (Patras, 'patras')
*
count_relation ('image', I2)
count_relation ('region', R2)
count_relation ('XLD', X2)
count_relation ('object', O2)
count_relation ('tuple', T2)
*
* I2 = 3  (three channels of the rgb image 'patras')
* R2 = 1  (the image domain of the image 'patras')
* X2 = 0  (no XLD data)
* O2 = 1  (the iconic object holding the channels and the domain)
* T2 = 0  (no empty object or object array )
```

## Result

If the parameter is correct, the operator `count_relation`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`reset_obj_db`

## Possible Successors

`set_system`

## See also

`clear_obj`

## Module

Foundation
