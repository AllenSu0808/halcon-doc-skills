# .NET（HalconDotNet）常見陷阱

來源標示：「文件」表示可在 `references/` 查證；「經驗」表示本文件未收錄的一般使用經驗，
使用前請以專案實際的 HalconDotNet 版本確認。

## 專案與環境

1. 以 `using HalconDotNet;` 匯入命名空間；組件版本必須與執行環境安裝的 HALCON 版本一致。（經驗）
2. 執行時需要 HALCON 原生函式庫（安裝時設定的 `HALCONROOT` 與 PATH）；只複製
   `halcondotnet.dll` 會在第一次呼叫時失敗。（經驗）
3. 目標平台用 x64，不要用 AnyCPU 搭配「偏好 32 位元」。（經驗）
4. HDevelop 匯出的 C# 程式以 `ho_`（iconic）與 `hv_`（control）為變數前綴，
   延伸既有匯出程式時沿用相同命名。（經驗）

## 呼叫方式

5. `HOperatorSet` 的每個參數都必須傳入，沒有選用參數或預設值；
   預設值請以 `params` 查 `Default`。（文件：各運算子 Signature）
6. 參數順序固定為：輸入物件、輸出物件、輸入控制、輸出控制；輸出一律是 `out`。（文件）
7. 同一功能有 `HOperatorSet` 靜態版與物件導向版（`HImage.X`、`HShapeModel.X`），
   兩者參數列不同（物件導向版少了 `this` 對應的參數），不要把一種的參數列套到另一種。（文件：`sig`）
8. 物件導向版常有兩個多載：`HTuple` 版（可傳多值）與純量版（`double` / `int` / `string`），
   以 `sig` 確認後再選。（文件）
9. 建立模型的運算子在物件導向 API 中通常是建構子，例如 `new HShapeModel(image, ...)`，
   以 `class HShapeModel` 查看。（文件）
10. `HOperatorSet` 的控制參數型別都是 `HTuple`；`double`、`int`、`string` 與其陣列可隱式轉成
    `HTuple`，不需要手動 `new HTuple(...)`。（經驗）

## 記憶體與生命週期

11. `HObject`、`HImage`、`HRegion`、`HXLDCont` 等 iconic 物件包裝非受控記憶體，
    用 `using` 或明確 `Dispose()` 釋放；大量影像處理時只靠 GC 會造成記憶體暴增。（經驗）
12. 以 `out HObject` 重複輸出到同一個變數前，先 `Dispose()` 舊物件
    （HDevelop 匯出程式的寫法：`ho_Image.Dispose(); HOperatorSet.ReadImage(out ho_Image, ...)`）。（經驗）
13. 迴圈中產生的中間物件（例如每張影像的 `ReduceDomain` 結果）要在迴圈內釋放。（經驗）
14. Handle（模型、量測物件、檔案等）在所有參考被覆寫後會自動清除；需要在特定時間釋放時
    呼叫 `ClearHandle` 或專用的 `ClearShapeModel` 等運算子。（文件：clear_handle）
15. 呼叫 `ClearShapeModel` 之後該 handle 立即失效，不能再使用。（文件：clear_shape_model）
16. `HShapeModel` 等 handle 類別本身也實作 `IDisposable`。（經驗）

## HTuple

17. 讀取單一值用 `.D`（double）、`.I`（int）、`.L`（long）、`.S`（string）；
    陣列用 `.DArr`、`.IArr`、`.LArr`、`.SArr`；長度用 `.Length`。（經驗）
18. 型別不符（例如實際是 double 卻讀 `.I`）會拋例外；不確定時先查 `.Type`，
    或用 `params` 看輸出參數型別。（經驗）
19. `HTuple` 索引從 0 開始，但 `SelectObj` 等 iconic 物件索引從 1 開始。（文件：select_obj）
20. 找不到結果時輸出 `HTuple` 長度為 0（例如 `FindShapeModel` 沒有匹配），
    讀 `[0]` 之前先檢查 `.Length`。（經驗）
21. 多值輸出（例如多個匹配的 Row / Column / Angle / Score）同索引對應同一個結果。（文件）
22. 串接 tuple 用 `TupleConcat`（文件：tuple_concat）；`HTuple` 的 `+` 是逐元素相加
    （對應 `TupleAdd`），不是串接。（經驗）

## 座標、角度與單位

23. 座標順序是 (Row, Column) = (y, x)，與 `System.Drawing.Point(x, y)` 相反。（文件）
24. 大多數角度參數是弧度（參數標頭顯示 `angle.rad`），但也有度數參數（`angle.deg`，
    例如 `RotateImage` 的 `phi`）；一律看 `params` 的標頭再決定單位。（文件：rotate_image）
25. 度與弧度轉換用 `HTuple.TupleRad` / `TupleDeg` 或 `Math.PI / 180`。（文件：tuple_rad）
26. 像素座標以像素中心為整數座標，左上角像素中心為 (0, 0)。（經驗）

## 字串參數

27. 字串參數值必須完全一致（大小寫、底線），先以 `params` 查 `List of values`；
    `check` 會標出不在 `List of values` 內的字串常值。（文件）
28. `'auto'` 只能用在文件列出 `'auto'` 的參數。（文件）
29. 泛用參數（`genParamName` / `genParamValue`）以兩個等長 tuple 成對傳入；
    可用的名稱列在該運算子的 Parameters 或 Description 段落。（文件）

## 顯示與執行緒

30. WinForms / WPF 用 `HSmartWindowControl`（或 WPF 版本）顯示，透過 `.HalconWindow`
    取得 `HWindow`；UI 相關呼叫必須在 UI 執行緒。（經驗）
31. `DispObj` 前以 `SetPart` 設定顯示範圍，否則影像可能只顯示一部分。（文件：set_part）
32. 運算子的執行緒安全等級看 `section <名稱> "Execution Information"`；
    標示為 exclusive 的運算子不能與其他運算子平行執行。（文件）

## 錯誤處理

33. 運算子錯誤以例外拋出（`HOperatorException`，基底 `HalconException`），
    可用 `GetErrorCode()` 取得錯誤碼；不要以空的 `catch` 吞掉。（經驗）
34. 模型檔（例如 `.shm`）由較新版本 HALCON 寫出時，舊版可能讀不回來。（經驗）
35. `ReadImage` 會搜尋 `image_dir` 系統參數的路徑，也會自動嘗試補副檔名；
    路徑錯誤時錯誤訊息只會說找不到檔案。（文件：read_image）
