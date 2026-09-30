# dev_clear_obj (Operator)

## Name

`dev_clear_obj` — Delete an iconic object from the HALCON database.

## Signature

`dev_clear_obj(Objects : : : )`

## Description

`dev_clear_obj` deletes iconic objects, which are no longer
needed, from the HALCON database.

## Attention

Never use [`clear_obj`](clear_obj.md) to clear objects in HDevelop. The
operator `dev_clear_obj` has to be used instead.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Objects to be deleted.

## Result

`dev_clear_obj` returns always 2 (
H_MSG_TRUE)
.

## See also

`clear_obj`,
`dev_set_check`,
`reset_obj_db`

## Module

Foundation
