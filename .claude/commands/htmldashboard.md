# HTML數據儀表板產生器

你是弘爺漢堡的數據視覺化專家。請產生 HTML 格式的數據儀表板。

## 輸入資訊
請提供：
- 數據內容/主題：$ARGUMENTS
- 呈現重點：（選填）
- 視覺風格：（選填）

## Data Visual 框架
將數據轉化為互動式 HTML 儀表板

## 請產出以下內容

### 📊 HTML 數據儀表板

---

## HTML 程式碼

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>弘爺漢堡 - 數據儀表板</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Microsoft JhengHei', sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }
        .dashboard {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            background: #E31837;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .header h1 {
            font-size: 24px;
        }
        .header .update-time {
            font-size: 14px;
            opacity: 0.8;
        }
        .kpi-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .kpi-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .kpi-card .label {
            font-size: 14px;
            color: #666;
        }
        .kpi-card .value {
            font-size: 32px;
            font-weight: bold;
            color: #333;
        }
        .kpi-card .change {
            font-size: 14px;
        }
        .kpi-card .change.up {
            color: #28a745;
        }
        .kpi-card .change.down {
            color: #dc3545;
        }
        .chart-row {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        .chart-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .chart-card h3 {
            margin-bottom: 15px;
            color: #333;
        }
        .table-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }
        th {
            background: #f8f9fa;
            font-weight: 600;
        }
        .status-badge {
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
        }
        .status-good { background: #d4edda; color: #155724; }
        .status-warning { background: #fff3cd; color: #856404; }
        .status-danger { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="dashboard">
        <!-- 標題區 -->
        <div class="header">
            <h1>📊 [儀表板標題]</h1>
            <div class="update-time">更新時間：YYYY/MM/DD HH:mm</div>
        </div>

        <!-- KPI 卡片區 -->
        <div class="kpi-row">
            <div class="kpi-card">
                <div class="label">KPI 1</div>
                <div class="value">00,000</div>
                <div class="change up">↑ 12% vs 上期</div>
            </div>
            <div class="kpi-card">
                <div class="label">KPI 2</div>
                <div class="value">00,000</div>
                <div class="change up">↑ 8% vs 上期</div>
            </div>
            <div class="kpi-card">
                <div class="label">KPI 3</div>
                <div class="value">00.0%</div>
                <div class="change down">↓ 2% vs 上期</div>
            </div>
            <div class="kpi-card">
                <div class="label">KPI 4</div>
                <div class="value">$00,000</div>
                <div class="change up">↑ 15% vs 上期</div>
            </div>
        </div>

        <!-- 表格區 -->
        <div class="table-card">
            <h3>📋 明細表格</h3>
            <table>
                <thead>
                    <tr>
                        <th>項目</th>
                        <th>數值</th>
                        <th>達成率</th>
                        <th>狀態</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>項目 A</td>
                        <td>1,234</td>
                        <td>105%</td>
                        <td><span class="status-badge status-good">達成</span></td>
                    </tr>
                    <tr>
                        <td>項目 B</td>
                        <td>987</td>
                        <td>92%</td>
                        <td><span class="status-badge status-warning">接近</span></td>
                    </tr>
                    <tr>
                        <td>項目 C</td>
                        <td>456</td>
                        <td>76%</td>
                        <td><span class="status-badge status-danger">落後</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
```

---

## 使用說明

1. 將上述程式碼複製到文字編輯器
2. 另存為 `.html` 檔案
3. 以瀏覽器開啟即可檢視
4. 根據實際數據修改數值內容

---

## 客製化區塊

### 配色修改
```css
/* 品牌主色 */
--primary-color: #E31837;  /* 弘爺紅 */
--success-color: #28a745;  /* 達成綠 */
--warning-color: #ffc107;  /* 警示黃 */
--danger-color: #dc3545;   /* 落後紅 */
```

### 新增 KPI 卡片
```html
<div class="kpi-card">
    <div class="label">[指標名稱]</div>
    <div class="value">[數值]</div>
    <div class="change up">↑ [百分比]% vs 上期</div>
</div>
```

---
適用職務：M（主管）、B（數位行銷）
優先級：⭐⭐
版本：V6.6
