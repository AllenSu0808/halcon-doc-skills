# set_drawing_object_callback (Operator)

## Name

`set_drawing_object_callback` — Add a callback function to a drawing object.

## Signature

`def set_drawing_object_callback(draw_handle: HHandle, draw_object_event: MaybeSequence[str], callback_function: MaybeSequence[int]) -> None`

## Description

`set_drawing_object_callback` adds the callback function
*`callback_function`* to be called on the event(s) defined in
*`draw_object_event`* to the drawing object *`draw_handle`*.
An event is an action, i.e., a user interaction with the
mouse or a call to a HALCON operator, e.g.,
[`attach_drawing_object_to_window`](attach_drawing_object_to_window.md)), that changes the current state of a
given drawing object. The operator `set_drawing_object_callback` allows
to define how to react to those events.

The following predefined events are available:

- ***"on_attach"*** —

  The corresponding callback will be called right after the object
  has been attached to the HALCON window and is ready for interaction.
- ***"on_detach"*** —

  The corresponding callback will be called right after the object
  has been detached from the window and is no longer available for interaction.
- ***"on_drag"*** —

  The corresponding callback will be called right after the object
  has been dragged with mouse interaction.
- ***"on_resize"*** —

  The corresponding callback will be called right after the object
  has been resized with mouse interaction.
- ***"on_select"*** —

  The corresponding callback will be called right after the object
  has been selected with mouse interaction.

It is possible to specify a particular callback for each desired event.
Then the input parameters *`draw_object_event`* and *`callback_function`*
must have the same length. It is also possible to use the same callback
for different events. Then *`draw_object_event`* has an
arbitrary length and *`callback_function`* contains one single value.

The callback is an integer of long type containing a pointer to a C function
with the following signature:

Herror HDrawObjectCallback(Hphandle DrawHandle, Hphandle WindowHandle, char* type)

On Windows systems, the __stdcall naming convention is used:

Herror __stdcall HDrawObjectCallback(Hphandle DrawHandle, Hphandle WindowHandle, char* type)

The first parameter of the callback function contains the handle to the draw
object that generated the event, the second one contains the handle of the
window where the interaction took place. Finally, the third parameter
indicates which event occurred.

## Attention

No graphical operator should be called within the callback, like for example
[`disp_obj`](disp_obj.md), for otherwise a deadlock may occur.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`draw_handle`** (input_control)  drawing_object `→` HHandle

Handle of the drawing object.

**`draw_object_event`** (input_control)  string(-array) `→` MaybeSequence[str]

Events to be captured.

Suggested values:
"on_resize", "on_drag", "on_attach", "on_detach", "on_select"

**`callback_function`** (input_control)  pointer(-array) `→` MaybeSequence[int]

Callback functions.

## Result

`set_drawing_object_callback` returns 2 (
H_MSG_TRUE)
, if *`draw_handle`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`attach_drawing_object_to_window`

## Possible Successors

`close_window`,
`clear_drawing_object`,
`detach_drawing_object_from_window`,
`get_drawing_object_iconic`,
`get_drawing_object_params`

## See also

`create_drawing_object_rectangle1`,
`attach_drawing_object_to_window`,
`detach_drawing_object_from_window`

## Module

Foundation
