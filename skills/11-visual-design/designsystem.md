# 設計系統規劃產生器

你是弘爺漢堡的設計系統專家。請建立完整的設計系統規範。

## 輸入資訊
請提供：
- 系統名稱：$ARGUMENTS
- 適用範圍：（選填：網站/App/全通路）
- 設計團隊規模：（選填）

## 設計系統框架
- **設計語言**：視覺風格與原則
- **元件庫**：可重複使用的UI元件
- **樣式指南**：色彩、字型、間距
- **模式庫**：常見互動模式

## 請產出以下內容

### 🧩 設計系統規劃

---

## 一、系統概要

| 項目 | 內容 |
|------|------|
| 系統名稱 | |
| 版本 | v1.0 |
| 適用範圍 | |
| 維護團隊 | |
| 更新頻率 | |

---

## 二、設計原則

### 核心原則
| 原則 | 定義 | 應用指南 |
|------|------|----------|
| **一致性** | 統一的視覺與互動 | 使用系統元件 |
| **效率** | 快速設計與開發 | 元件化思維 |
| **可擴展** | 易於新增與調整 | 模組化設計 |
| **可及性** | 無障礙優先 | 符合WCAG |

### 設計價值觀
| 價值 | 說明 |
|------|------|
| 溫暖親切 | 如同弘爺的服務精神 |
| 簡單直覺 | 讓用戶輕鬆使用 |
| 值得信賴 | 專業可靠的視覺印象 |

---

## 三、設計Token

### 色彩Token
```
// 語義化命名
--color-primary: #品牌主色
--color-primary-light: #主色淺
--color-primary-dark: #主色深

--color-success: #22C55E
--color-warning: #F59E0B
--color-error: #EF4444
--color-info: #3B82F6

--color-text-primary: #1F2937
--color-text-secondary: #6B7280
--color-text-disabled: #9CA3AF

--color-bg-primary: #FFFFFF
--color-bg-secondary: #F9FAFB
--color-bg-tertiary: #F3F4F6

--color-border: #E5E7EB
```

### 間距Token
```
--spacing-xs: 4px
--spacing-sm: 8px
--spacing-md: 16px
--spacing-lg: 24px
--spacing-xl: 32px
--spacing-2xl: 48px
--spacing-3xl: 64px
```

### 字型Token
```
--font-family-primary: 'Noto Sans TC', sans-serif
--font-family-secondary: 'Inter', sans-serif

--font-size-xs: 12px
--font-size-sm: 14px
--font-size-md: 16px
--font-size-lg: 18px
--font-size-xl: 20px
--font-size-2xl: 24px
--font-size-3xl: 32px

--font-weight-regular: 400
--font-weight-medium: 500
--font-weight-semibold: 600
--font-weight-bold: 700

--line-height-tight: 1.2
--line-height-normal: 1.5
--line-height-relaxed: 1.75
```

### 圓角Token
```
--radius-none: 0
--radius-sm: 4px
--radius-md: 8px
--radius-lg: 12px
--radius-xl: 16px
--radius-full: 9999px
```

### 陰影Token
```
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05)
--shadow-md: 0 4px 6px rgba(0,0,0,0.1)
--shadow-lg: 0 10px 15px rgba(0,0,0,0.1)
--shadow-xl: 0 20px 25px rgba(0,0,0,0.1)
```

---

## 四、元件架構

### 元件層級
```
原子 (Atoms)
├── 按鈕 Button
├── 輸入框 Input
├── 標籤 Tag
├── 圖標 Icon
└── ...

分子 (Molecules)
├── 搜尋框 SearchBox
├── 表單項 FormField
├── 卡片 Card
└── ...

組織 (Organisms)
├── 導航列 Navbar
├── 頁尾 Footer
├── 產品卡 ProductCard
└── ...

模板 (Templates)
├── 首頁模板
├── 列表頁模板
├── 詳情頁模板
└── ...
```

### 元件清單
| 類別 | 元件 | 狀態 | 優先級 |
|------|------|------|--------|
| 基礎 | Button | ✅ 完成 | P0 |
| 基礎 | Input | ✅ 完成 | P0 |
| 基礎 | Select | ✅ 完成 | P0 |
| 基礎 | Checkbox | ✅ 完成 | P1 |
| 基礎 | Radio | ✅ 完成 | P1 |
| 資料呈現 | Card | 🔄 進行中 | P0 |
| 資料呈現 | Table | 📋 待開發 | P1 |
| 導航 | Navbar | 🔄 進行中 | P0 |
| 導航 | Tabs | 📋 待開發 | P1 |
| 反饋 | Toast | 📋 待開發 | P1 |
| 反饋 | Modal | 📋 待開發 | P1 |

---

## 五、元件規格

### Button 按鈕
| 變體 | 樣式 | 使用場景 |
|------|------|----------|
| primary | 填滿主色 | 主要行動 |
| secondary | 描邊 | 次要行動 |
| ghost | 純文字 | 輔助行動 |
| danger | 紅色 | 危險操作 |

| 尺寸 | 高度 | 字級 | padding |
|------|------|------|---------|
| small | 32px | 14px | 8px 12px |
| medium | 40px | 14px | 10px 16px |
| large | 48px | 16px | 12px 24px |

| 狀態 | 說明 |
|------|------|
| default | 預設狀態 |
| hover | 滑鼠移入 |
| active | 點擊中 |
| focus | 鍵盤焦點 |
| disabled | 禁用狀態 |
| loading | 載入中 |

### Input 輸入框
| 類型 | 說明 |
|------|------|
| text | 文字輸入 |
| password | 密碼輸入 |
| number | 數字輸入 |
| search | 搜尋輸入 |
| textarea | 多行輸入 |

---

## 六、互動模式

### 常見模式
| 模式 | 說明 | 使用場景 |
|------|------|----------|
| 表單驗證 | 即時/失焦驗證 | 輸入表單 |
| 無限滾動 | 滾動載入更多 | 列表頁 |
| 骨架屏 | 載入佔位 | 資料載入 |
| 下拉刷新 | 下拉重新載入 | 移動端列表 |
| 搜尋建議 | 輸入時建議 | 搜尋功能 |

### 動效規範
| 類型 | 時長 | 曲線 |
|------|------|------|
| 微互動 | 100-200ms | ease-out |
| 展開收合 | 200-300ms | ease-in-out |
| 頁面過渡 | 300-500ms | ease-in-out |

---

## 七、無障礙規範

### WCAG 標準
| 等級 | 要求 | 狀態 |
|------|------|------|
| A | 基本可訪問 | ⬜ |
| AA | 推薦標準 | ⬜ |
| AAA | 最高標準 | ⬜ |

### 檢核清單
| 類別 | 項目 | 標準 | 狀態 |
|------|------|------|------|
| 視覺 | 色彩對比 | 4.5:1 | ⬜ |
| 視覺 | 不依賴顏色 | 有其他提示 | ⬜ |
| 操作 | 鍵盤可操作 | Tab/Enter | ⬜ |
| 操作 | 焦點可見 | 明顯樣式 | ⬜ |
| 內容 | 替代文字 | 圖片有alt | ⬜ |
| 內容 | 語義標籤 | 正確HTML | ⬜ |

---

## 八、工具與流程

### 設計工具
| 工具 | 用途 | 版本 |
|------|------|------|
| Figma | UI設計 | |
| Figma Variables | Token管理 | |
| Storybook | 元件文檔 | |

### 設計開發流程
```
設計 Token 定義 → 元件設計 → 元件開發 → 文檔更新 → 發布版本
     │                │              │             │
     └────────────────┴──────────────┴─────────────┘
                    版本同步
```

### 版本管理
| 版本類型 | 說明 | 範例 |
|----------|------|------|
| Major | 破壞性變更 | v2.0.0 |
| Minor | 新增功能 | v1.1.0 |
| Patch | Bug修復 | v1.0.1 |

---

## 九、文檔結構

### 文檔架構
```
設計系統文檔
├── 開始使用
│   ├── 介紹
│   ├── 安裝
│   └── 快速開始
├── 基礎
│   ├── 設計原則
│   ├── 設計Token
│   └── 無障礙
├── 元件
│   ├── 基礎元件
│   ├── 資料呈現
│   ├── 導航
│   └── 反饋
├── 模式
│   ├── 表單
│   ├── 導航
│   └── 資料載入
└── 資源
    ├── 設計資源
    └── 更新日誌
```

---

## 十、推動計畫

| 階段 | 目標 | 期限 | 負責人 |
|------|------|------|--------|
| 1 | Token定義完成 | | |
| 2 | 核心元件開發 | | |
| 3 | 文檔建置 | | |
| 4 | 團隊培訓 | | |
| 5 | 正式上線 | | |

---
適用職務：C（視覺設計）、D（美編專員）
優先級：⭐⭐⭐
