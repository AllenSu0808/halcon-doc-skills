# SetDrawingObjectCallback (Operator)

## Name

`SetDrawingObjectCallback` — Add a callback function to a drawing object.

## Signature

`static void HOperatorSet.SetDrawingObjectCallback(HTuple drawHandle, HTuple drawObjectEvent, HTuple callbackFunction)`

`void HDrawingObject.SetDrawingObjectCallback(HTuple drawObjectEvent, HTuple callbackFunction)`

`void HDrawingObject.SetDrawingObjectCallback(string drawObjectEvent, IntPtr callbackFunction)`

## Description

`SetDrawingObjectCallback` adds the callback function
*`callbackFunction`* to be called on the event(s) defined in
*`drawObjectEvent`* to the drawing object *`drawHandle`*.
An event is an action, i.e., a user interaction with the
mouse or a call to a HALCON operator, e.g.,
[`AttachDrawingObjectToWindow`](attach_drawing_object_to_window.md)), that changes the current state of a
given drawing object. The operator `SetDrawingObjectCallback` allows
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
Then the input parameters *`drawObjectEvent`* and *`callbackFunction`*
must have the same length. It is also possible to use the same callback
for different events. Then *`drawObjectEvent`* has an
arbitrary length and *`callbackFunction`* contains one single value.

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
[`DispObj`](disp_obj.md), for otherwise a deadlock may occur.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`drawHandle`** (input_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

**`drawObjectEvent`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Events to be captured.

Suggested values:
"on_resize", "on_drag", "on_attach", "on_detach", "on_select"

**`callbackFunction`** (input_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

Callback functions.

## Result

`SetDrawingObjectCallback` returns 2 (
H_MSG_TRUE)
, if *`drawHandle`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`AttachDrawingObjectToWindow`

## Possible Successors

`CloseWindow`,
`ClearDrawingObject`,
`DetachDrawingObjectFromWindow`,
`GetDrawingObjectIconic`,
`GetDrawingObjectParams`

## See also

`CreateDrawingObjectRectangle1`,
`AttachDrawingObjectToWindow`,
`DetachDrawingObjectFromWindow`

## Module

Foundation
