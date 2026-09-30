# create_metrology_model (Operator)

## Name

`create_metrology_model` — Create the data structure that is needed to measure geometric shapes.

## Signature

`create_metrology_model( : : : MetrologyHandle)`

## Description

`create_metrology_model` creates a metrology model, i.e., the
data structure that is needed to measure objects with a specific
geometric shape (metrology object) via 2D metrology, and returns it
in the handle *`MetrologyHandle`*.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Attention

Note, that after calling the operator `create_metrology_model`
the operator [`set_metrology_model_image_size`](set_metrology_model_image_size.md) should be called
for efficiency reasons.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`MetrologyHandle`** (output_control)  metrology_model `→`  (handle)

Handle of the metrology model.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
create_metrology_model (MetrologyHandle)
get_image_size (Image, Width, Height)
set_metrology_model_image_size (MetrologyHandle, Width, Height)
add_metrology_object_rectangle2_measure (MetrologyHandle, 270, 230, 0, 30, \
                                  25, 10, 2, 1, 30, [], [], Index)
apply_metrology_model (Image, MetrologyHandle)
get_metrology_object_result (MetrologyHandle, Index, 'all', 'result_type', \
                      'all_param', Rectangle)
get_metrology_object_result_contour (Contour, MetrologyHandle, \
                                    Index, 'all', 1.5)
```

## Result

If the parameters are valid, the operator `create_metrology_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_metrology_model_image_size`

## Module

2D Metrology
