# reset_obj_db (Operator)

## Name

`reset_obj_db` — Reset the HALCON system for iconic objects.

## Signature

`def reset_obj_db(default_image_width: int, default_image_height: int, default_channels: int) -> None`

## Description

The operator `reset_obj_db` reinitializes the HALCON system
for iconic objects (which was set up during the HALCON
initialization process). With this operator the five relations
(gray value objects, region objects, XLD objects, image objects and
object tuples) which are used for image processing with HALCON will
be installed (see also [`count_relation`](count_relation.md)).
In case the HALCON database was enabled
(`set_system('database','true')`) and the relations already exist, all
data entries listed in the relations will get deallocated!

The parameters *`default_image_width`* and *`default_image_height`*
provide the initial values for the global maximum image size. If the first
created object is an image, (e.g., [`read_image`](read_image.md)), the set values
will only be overruled, if they are smaller than the size of the created
object.
If on the other hand the first object to be created is a region,
the values will only be adjusted in case the new image is larger than the
set values.
This is not only the case for the first image which is created or
read: the global image size will always be enlarged, if larger images
are created.

The global image size is of consequence for the opening of windows
([`open_window`](open_window.md)) and the memory estimate and clipping of regions.
Whenever the clip mode is activated, regions will be clipped according
to the global image size (`set_system('clip_region','true')`).
This can lead to problems if images of various sizes are used.
In this case only the fact that a region is smaller or of the same size
as the largest image can be guaranteed.

The parameter *`default_channels`* returns the most frequent
number of channels of an image object. This value can be set to 0 if
for the most part regions are used.
If more channels than those having been set at the initialization are
necessary for one image, the number will be enlarged dynamically for
this image.
If less channels than those having been set at the initialization are
necessary for the image, the superfluous channels will be set as
undefined. For the user this will seem as if they were non existent,
however, memory is allocated unnecessarily.

The parameter values can be queried using the operator [`get_system`](get_system.md).

## Attention

If the operator `reset_obj_db` is not called at the beginning of a
HALCON session, HALCON will be initialized automatically by the operator
`reset_obj_db(128,128,0)` causing side effects on region clipping,
accordingly.
When the database was enabled by the parameter value *"database"* of
the operator [`set_system`](set_system.md), calling `reset_obj_db` will deallocate
all iconic objects.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`default_image_width`** (input_control)  integer `→` int

Default image width (in pixels).

Default:
128

Suggested values:
64, 128, 320, 640, 800, 1280

**`default_image_height`** (input_control)  integer `→` int

Default image height (in pixels).

Default:
128

Suggested values:
64, 128, 240, 480, 600, 1024

**`default_channels`** (input_control)  integer `→` int

Usual number of channels.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7

## Result

The operator `reset_obj_db` returns the value 2 (
H_MSG_TRUE)
if the
parameter values are correct.
Otherwise an exception will be raised.

## See also

`get_channel_info`,
`count_relation`

## Module

Foundation
