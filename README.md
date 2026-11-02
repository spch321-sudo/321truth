# 321真理點心

## 2026-11-02 一起共讀改走自己的中繼站
- 共讀連線由 PeerJS／WebRTC（公用信令伺服器）改為 Cloudflare Worker 中繼站（wss://coread-321.spch321.workers.dev），peerjs.min.js 換成相容介面的精簡連線層；連得上、後到的人一加入就同步到帶領者目前的位置、斷線自動重連。共讀功能與協定不變。

國度321空中團契・每日真理點心 PWA。609 篇（第 1–609 篇全部齊全）。

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
| data/idx-zh.json、data/idx-zs.json、data/idx-en.json | 目錄（繁／簡／English） |
| data/en-NN.json、lang-en.json | 英文版課文（609 篇）與英文介面 |
| data/zh-00…12.json、data/zs-00…12.json | 全部篇章內容，每 50 篇一包 |
| sw.js、version.json | 離線與自動更新 |
| manifest.json、icon-*.png、apple-touch-icon*.png | 加到主畫面的圖示 |

詩歌庫沿用《321互動聖經》（同網域 `../bible/music.json`），不需另外上傳音樂。


## 更新紀錄
- 英文版：右上角「繁｜简｜EN」切換，609 篇全文與介面、小智、朗讀（英文語音）皆有英文。
- 小智回答選項：回答長度（簡要／適中／詳細）、慕道友六種信仰背景、可收合選項列；改長度或背景會依新設定重新回答。
- 英文版經文採用 World English Bible（WEB，公有領域），逐節取自官方 USFM 檔；英文解說與禱告為翻譯。
- 一起共讀（複製自《321慕道生活》）：右上角 📡，帶領者翻到哪一篇、捲到哪一段、點哪一句、朗讀到哪裡，加入者的手機同步跟著走；6 碼代碼／QR／邀請連結；手機對手機直連（PeerJS／WebRTC），不經伺服器。需要 `peerjs.min.js`、`qrcode.js`。
