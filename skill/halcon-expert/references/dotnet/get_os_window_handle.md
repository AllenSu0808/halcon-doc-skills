# GetOsWindowHandle (Operator)

## Name

`GetOsWindowHandle` — Get the operating system window handle.

## Warning

**This operator does not work in an HDevelop graphics window opened with
`dev_open_window`.**

## Signature

`static void HOperatorSet.GetOsWindowHandle(HTuple windowHandle, out HTuple OSWindowHandle, out HTuple OSDisplayHandle)`

`IntPtr HWindow.GetOsWindowHandle(out IntPtr OSDisplayHandle)`

## Description

`GetOsWindowHandle` returns the operating system window
handle of the HALCON window *`windowHandle`* in
*`OSWindowHandle`*. Under Unix-like systems, additionally the operating
system display handle is returned in *`OSDisplayHandle`*.
The operating system window handle can be used to access the window
using functions from the operating system, e.g., to draw in a
user-defined manner into the window. Under Windows,
*`OSWindowHandle`* can be cast to a variable of type HWND.
Under Unix-like systems, *`OSWindowHandle`* can be cast into a
variable of type Window, while *`OSDisplayHandle`* can be cast
into a variable of type Display.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`OSWindowHandle`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Operating system window handle.

**`OSDisplayHandle`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Operating system display handle (under Unix-like systems only).

## Example (C)

```
/* Draw a line into a HALCON window under Unix-like systems using X11 calls. */
#include "HalconC.h"
#include <X11/X.h>
#include <X11/Xlib.h>

int main(int argc, char **argv)
{
  Hlong hwin, win, disp;
  Display *display;
  Window window;
  GC gc;
  XGCValues values;
  static char dashes[] = { 20, 20 };

  open_window(0, 0, 500, 500, 0, "visible", "", &hwin);
  get_os_window_handle(hwin, &win, &disp);
  display = (Display *)disp;
  window = (Window)win;
  gc = XCreateGC(display, window, 0, &values);
  XSetFunction(display, gc, GXset);
  XSetLineAttributes(display, gc, 10, LineOnOffDash, CapRound, JoinRound);
  XSetDashes(display, gc, 0, dashes, 2);
  XSetForeground(display, gc, WhitePixel(display, DefaultScreen(display)));
  XSetBackground(display, gc, BlackPixel(display, DefaultScreen(display)));
  XDrawLine(display, win, gc, 20, 20, 480, 480);
  XFlush(display);
  XFreeGC(display, gc);
  wait_seconds(5);
  return 0;
}

/* Draw a line into a HALCON window under Windows using GDI calls. */
#include "HalconC.h"
#include "windows.h"

int main(int argc, char **argv)
{
  Hlong hwin, win, disp;
  HDC hdc;
  HPEN hpen;
  HPEN *hpen_old;
  LOGBRUSH logbrush;
  POINT point;
  static DWORD dashes[] = { 20, 20 };

  open_window(0, 0, 500, 500, 0, "visible", "", &hwin);
  get_os_window_handle(hwin, &win, &disp);
  logbrush.lbColor = RGB(255,255,255);
  logbrush.lbStyle = BS_SOLID;
  hpen =  ExtCreatePen(PS_USERSTYLE|PS_GEOMETRIC, 10, &logbrush, 2, dashes);
  hdc = GetDC((HWND)win);
  hpen_old = (HPEN *)SelectObject(hdc, hpen);
  MoveToEx(hdc, 20, 20, &point);
  LineTo(hdc, 480, 480);
  DeleteObject(SelectObject(hdc, hpen_old));
  ReleaseDC((HWND)win, hdc);
  wait_seconds(5);
  return 0;
}
```

## Result

If the window is valid `GetOsWindowHandle` returns 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.

## Possible Predecessors

`OpenWindow`

## Module

Foundation
