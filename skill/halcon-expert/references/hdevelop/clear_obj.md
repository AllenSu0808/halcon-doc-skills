# clear_obj (Operator)

## Name

`clear_obj` — Delete an iconic object from the HALCON database.

## Signature

`clear_obj(Objects : : : )`

## Description

`clear_obj` deletes iconic objects, which are no longer
needed, from the HALCON database. It should be noted that
`clear_obj` is the only way to delete objects from the
database, and hence to reclaim their memory, in HALCON/C. In all
other HALCON language interfaces, `clear_obj` **must
not** be used because objects are destroyed automatically through
appropriate destructors.

Images and regions are normally used by several iconic objects at
the same time (uses less memory!). This has the consequence that a
region or an image is only deleted if all objects using it have been
deleted.

The operator [`reset_obj_db`](reset_obj_db.md) can be used to reset the system
and clear all remaining iconic objects.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Attention

Regarding the use of local variables in HALCON/C: When exiting a subroutine,
the local variables are deleted, but the HALCON database is not updated. To
update the database and thus free the memory, you must explicitly clear the
local objects from the database before exiting the subroutine.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Objects to be deleted.

## Result

`clear_obj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database. If not all objects are valid (e.g., already
cleared), an exception is raised, which also clears all valid objects.
The operator `set_check('~clear')`
can be used to suppress the raising of this exception. If the input is
empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Alternatives

`reset_obj_db`

## See also

`set_check`

## Module

none
