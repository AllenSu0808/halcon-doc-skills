# HWindow (Class)

## Name

`HWindow` — Represents an instance of a HALCON window.

## Constructors

|  |  |  |
| --- | --- | --- |
| `OpenWindow` |  | Open a graphics window. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AttachBackgroundToWindow` |  | Attach a background image to a window. |
| `AttachDrawingObjectToWindow` |  | Attach an existing drawing object to a window. |
| `ClearRectangle` |  | Delete a rectangle on the output window. |
| `ClearWindow` |  | Delete the contents of an output window. |
| `CloseWindow` |  | Close an output window. |
| `ConvertCoordinatesImageToWindow` |  | Convert image coordinates to window coordinates |
| `ConvertCoordinatesWindowToImage` |  | Convert window coordinates to image coordinates |
| `CopyRectangle` |  | Copy all pixels within rectangles between output windows. |
| `DetachBackgroundFromWindow` |  | Detach the background image from a window. |
| `DetachDrawingObjectFromWindow` |  | Detach an existing drawing object from a window. |
| `DevClearWindow` |  | Clear the contents of the active graphics window. |
| `DevCloseWindow` |  | Close the active floating graphics window. |
| `DevDispText` |  | Display text in the current graphics window. |
| `DevDisplay` |  | Displays image objects in the current graphics window. |
| `DevGetWindow` |  | Return the handle of the active graphics window. |
| `DevOpenWindow` |  | Open a new graphics window. |
| `DevSetColor` |  | Set one or more output colors. |
| `DevSetColored` |  | Set multiple output colors. |
| `DevSetContourStyle` |  | Define the contour display fill style. |
| `DevSetDraw` |  | Define the region fill mode. |
| `DevSetLineWidth` |  | Define the line width for region contour output. |
| `DevSetLut` |  | Set “look-up-table” (lut). |
| `DevSetPaint` |  | Define the gray value output mode. |
| `DevSetPart` |  | Modify the displayed image part. |
| `DevSetShape` |  | Define the region output shape. |
| `DevSetWindow` |  | Activate a graphics window. |
| `DevSetWindowExtents` |  | Change position and size of the active floating graphics window. |
| `DevUpdateWindow` |  | Switches the automatic output of iconic output objects into the graphics window during program execution on or off. |
| `DispArc` |  | Displays circular arcs in a window. |
| `DispArrow` |  | Displays arrows in a window. |
| `DispCaltab` |  | Project and visualize the 3D model of the calibration plate in the image. |
| `DispChannel` |  | Displays images with several channels. |
| `DispCircle` |  | Displays circles in a window. |
| `DispColor` |  | Displays a color (RGB) image |
| `DispCross` |  | Displays crosses in a window. |
| `DispDistribution` |  | Displays a noise distribution. |
| `DispEllipse` |  | Displays ellipses. |
| `DispImage` |  | Displays gray value images. |
| `DispLine` |  | Draws lines in a window. |
| `DispLut` |  | Graphical view of the look-up-table (lut). |
| `DispObj` |  | Displays image objects (image, region, XLD). |
| `DispPolygon` |  | Displays a polyline. |
| `DispRectangle1` |  | Display of rectangles aligned to the coordinate axes. |
| `DispRectangle2` |  | Displays arbitrarily oriented rectangles. |
| `DispRegion` |  | Displays regions in a window. |
| `DispText` |  | Display text in a window. |
| `DispXld` |  | Display an XLD object. |
| `DragRegion1` |  | Interactive moving of a region. |
| `DragRegion2` |  | Interactive movement of a region with fixpoint specification. |
| `DragRegion3` |  | Interactive movement of a region with restriction of positions. |
| `DrawCircle` |  | Interactive drawing of a circle. |
| `DrawCircleMod` |  | Interactive drawing of a circle. |
| `DrawEllipse` |  | Interactive drawing of an ellipse. |
| `DrawEllipseMod` |  | Interactive drawing of an ellipse. |
| `DrawLine` |  | Draw a line. |
| `DrawLineMod` |  | Draw a line. |
| `DrawNurbs` |  | Interactive drawing of a NURBS curve. |
| `DrawNurbsInterp` |  | Interactive drawing of a NURBS curve using interpolation. |
| `DrawNurbsInterpMod` |  | Interactive modification of a NURBS curve using interpolation. |
| `DrawNurbsMod` |  | Interactive modification of a NURBS curve. |
| `DrawPoint` |  | Draw a point. |
| `DrawPointMod` |  | Draw a point. |
| `DrawPolygon` |  | Interactive drawing of a polygon row. |
| `DrawRectangle1` |  | Draw a rectangle parallel to the coordinate axis. |
| `DrawRectangle1Mod` |  | Draw a rectangle parallel to the coordinate axis. |
| `DrawRectangle2` |  | Interactive drawing of any orientated rectangle. |
| `DrawRectangle2Mod` |  | Interactive drawing of any orientated rectangle. |
| `DrawRegion` |  | Interactive drawing of a closed region. |
| `DrawXld` |  | Interactive drawing of a contour. |
| `DrawXldMod` |  | Interactive modification of a contour. |
| `DumpWindow` |  | Write the window content to a file. |
| `DumpWindowImage` |  | Write the window content in an image object. |
| `Endif` |  | End of if command. |
| `Endswitch` |  | Ends a multiway branch block. |
| `FlushBuffer` |  | Flush the contents of a window. |
| `GetContourStyle` |  | Get the current contour display fill style. |
| `GetDraw` |  | Get the current region fill mode. |
| `GetFix` |  | Get mode of fixing of current look-up-table (lut). |
| `GetFixedLut` |  | Get fixing of “look-up-table” (lut) for “real color images” |
| `GetFont` |  | Get the current font. |
| `GetFontExtents` |  | Get the maximum size of all characters of a font. |
| `GetHsi` |  | Get the HSI coding of the current color. |
| `GetIcon` |  | Query the icon for region output |
| `GetLineApprox` |  | Get the current approximation error for contour display. |
| `GetLineStyle` |  | Get the current graphic mode for contours. |
| `GetLineWidth` |  | Get the current line width for contour display. |
| `GetLut` |  | Get current look-up-table (lut). |
| `GetLutStyle` |  | Get modification parameters of look-up-table (lut). |
| `GetMbutton` |  | Wait until a mouse button is pressed. |
| `GetMbuttonSubPix` |  | Wait until a mouse button is pressed and get the subpixel mouse position. |
| `GetMposition` |  | Query the mouse position. |
| `GetMpositionSubPix` |  | Query the subpixel mouse position. |
| `GetMshape` |  | Query the current mouse pointer shape. |
| `GetOsWindowHandle` |  | Get the operating system window handle. |
| `GetPaint` |  | Get the current display mode for gray values. |
| `GetPart` |  | Get the image part. |
| `GetPartStyle` |  | Get the current interpolation mode for gray value display. |
| `GetPixel` |  | Get the current color lookup table index. |
| `GetRgb` |  | Get the current color in RGB-coding. |
| `GetRgba` |  | Get the current color in RGBA-coding. |
| `GetShape` |  | Get the current region output shape. |
| `GetStringExtents` |  | Get the spatial size of a string. |
| `GetTposition` |  | Get cursor position. |
| `GetTshape` |  | Get the shape of the text cursor. |
| `GetWindowBackgroundImage` |  | Gets a copy of the background image of the window. |
| `GetWindowExtents` |  | Information about a window's size and position. |
| `GetWindowParam` |  | Get window parameters. |
| `GetWindowPointer3` |  | Access to a window's pixel data. |
| `GetWindowType` |  | Get the window type. |
| `MoveRectangle` |  | Copy inside an output window. |
| `NewExternWindow` |  | Create a virtual graphics window under Windows. |
| `NewLine` |  | Set the position of the text cursor to the beginning of the next line. |
| `OpenTextwindow` |  | Open a textual window. |
| `OpenWindow` |  | Open a graphics window. |
| `QueryAllColors` |  | Query all color names. |
| `QueryColor` |  | Query all color names displayable in the window. |
| `QueryFont` |  | Query the available fonts. |
| `QueryGray` |  | Query the displayable gray values. |
| `QueryLut` |  | Query all available look-up-tables (lut). |
| `QueryMshape` |  | Query all available mouse pointer shapes. |
| `QueryPaint` |  | Query the gray value display modes. |
| `QueryTshape` |  | Query all shapes available for text cursors. |
| `ReadChar` |  | Read a character from a window. |
| `ReadString` |  | Read a string in a text window. |
| `SendMouseDoubleClickEvent` |  | Send an event to a buffer window signaling a mouse double click event. |
| `SendMouseDownEvent` |  | Send an event to a window buffer signaling a mouse down event. |
| `SendMouseDragEvent` |  | Send an event to a buffer window signaling a mouse drag event. |
| `SendMouseUpEvent` |  | Send an event to a buffer window signaling a mouse up event. |
| `SetColor` |  | Set output color. |
| `SetColored` |  | Set multiple output colors. |
| `SetComprise` |  | Define the image matrix output clipping. |
| `SetContentUpdateCallback` |  | Sets the callback for content updates in buffer window. |
| `SetContourStyle` |  | Define the contour display fill style. |
| `SetDraw` |  | Define the region fill mode. |
| `SetFix` |  | Set fixing of “look-up-table” (lut) |
| `SetFixedLut` |  | Fix “look-up-table” (lut) for “real color images”. |
| `SetFont` |  | Set the font used for text output. |
| `SetGray` |  | Define gray values for region output. |
| `SetHsi` |  | Define output colors (HSI-coded). |
| `SetIcon` |  | Icon definition for region output. |
| `SetLineApprox` |  | Define the approximation error for contour display. |
| `SetLineStyle` |  | Define a contour output pattern. |
| `SetLineWidth` |  | Define the line width for region contour output. |
| `SetLut` |  | Set “look-up-table” (lut). |
| `SetLutStyle` |  | Changing the look-up-table (lut). |
| `SetMshape` |  | Set the current mouse pointer shape. |
| `SetPaint` |  | Define the gray value output mode. |
| `SetPart` |  | Modify the displayed image part. |
| `SetPartStyle` |  | Define an interpolation method for gray value output. |
| `SetPixel` |  | Define a color lookup table index. |
| `SetRgb` |  | Set the color definition via RGB values. |
| `SetRgba` |  | Set the color definition via RGBA values. |
| `SetShape` |  | Define the region output shape. |
| `SetTposition` |  | Set the position of the text cursor. |
| `SetTshape` |  | Set the shape of the text cursor. |
| `SetWindowDc` |  | Set the device context of a virtual graphics window (Windows NT). |
| `SetWindowExtents` |  | Modify position and size of a window. |
| `SetWindowParam` |  | Set window parameters. |
| `SlideImage` |  | Interactive output from two window buffers. |
| `Stop` |  | Stop program execution. |
| `UnprojectCoordinates` |  | Calculates image coordinates for a point in a 3D plot window. |
| `UpdateWindowPose` |  | Modify the pose of a 3D plot. |
| `WriteLut` |  | Write look-up-table (lut) as file. |
| `WriteString` |  | Print text in a window. |
