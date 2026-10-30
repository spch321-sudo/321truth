# 321真理點心

國度321空中團契・每日真理點心 PWA。580 篇（第 1–580 篇全部齊全）。

## 上傳到 GitHub Pages

1. 在 GitHub（帳號 spch321-sudo）建立新的 repo，建議名稱：`321truth`。
2. 把這個資料夾裡的**全部檔案與 `data` 資料夾**原樣上傳到 repo 根目錄（Upload files → 整批拖進去）。
3. Settings → Pages → Branch 選 `main`、資料夾 `/ (root)` → Save。
4. 約 1～10 分鐘後即可開啟：`https://spch321-sudo.github.io/321truth/`

## 之後更新

每次更新把新版整批上傳覆蓋，特別是 `index.html`、`app.js`、`sw.js`、`version.json`（`data/` 內容沒改可不傳）。已安裝的手機打開或切回 App 就會自動換成新版；也可以到「我的 → 檢查更新」。

## 檔案說明

| 檔案 | 用途 |
|---|---|
| index.html | 外觀與版面 |
| app.js | 主程式（ES5，WPS／舊手機也能跑） |
| media.js | 美圖工作室的配樂、錄音、錄影、我的作品（進入美圖才載入） |
| lang-zs.json | 簡體介面文字 |
| data/idx-zh.json、data/idx-zs.json | 目錄（繁／簡） |
| data/zh-00…11.json、data/zs-00…11.json | 全部篇章內容，每 50 篇一包 |
| sw.js、version.json | 離線與自動更新 |
| manifest.json、icon-*.png、apple-touch-icon*.png | 加到主畫面的圖示 |

詩歌庫沿用《321互動聖經》（同網域 `../bible/music.json`），不需另外上傳音樂。
