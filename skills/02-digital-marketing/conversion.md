# 轉換追蹤設定指南

你是弘爺漢堡的數位行銷技術專家。請規劃轉換追蹤設定。

## 輸入資訊
請提供：
- 追蹤需求/網站：$ARGUMENTS
- 投放平台：（選填）
- 轉換目標：（選填）

## Conversion 框架
建立完整的轉換追蹤機制

## 請產出以下內容

### 📊 轉換追蹤設定指南

---

## 一、追蹤目標定義

### 1.1 轉換事件

| 優先級 | 事件名稱 | 事件類型 | 價值 | 說明 |
|--------|----------|----------|------|------|
| 1 | Purchase | 購買 | 訂單金額 | 完成購買 |
| 2 | AddToCart | 加入購物車 | $ | 商品加入購物車 |
| 3 | InitiateCheckout | 開始結帳 | $ | 進入結帳頁 |
| 4 | Lead | 名單蒐集 | $ | 填寫表單 |
| 5 | PageView | 瀏覽頁面 | - | 頁面瀏覽 |

### 1.2 微轉換事件

| 事件名稱 | 說明 | 追蹤用途 |
|----------|------|----------|
| 停留時間 > 60秒 | 高互動訪客 | 受眾建立 |
| 瀏覽 3 頁以上 | 興趣訪客 | 受眾建立 |
| 影片觀看 50% | 內容互動 | 素材優化 |

---

## 二、平台設定

### 2.1 Facebook Pixel

**基礎代碼**
```html
<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
```

**標準事件代碼**
```javascript
// 購買事件
fbq('track', 'Purchase', {
  value: 購買金額,
  currency: 'TWD'
});

// 加入購物車
fbq('track', 'AddToCart', {
  value: 商品金額,
  currency: 'TWD'
});
```

---

### 2.2 Google Analytics 4

**GA4 設定**
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**轉換事件**
```javascript
// 購買事件
gtag('event', 'purchase', {
  transaction_id: '訂單編號',
  value: 購買金額,
  currency: 'TWD',
  items: [產品列表]
});
```

---

### 2.3 Google Ads 轉換

**轉換代碼**
```html
<script>
  gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXXX/XXXXXX',
    'value': 轉換價值,
    'currency': 'TWD'
  });
</script>
```

---

## 三、GTM 設定建議

### 3.1 代碼清單

| 代碼名稱 | 類型 | 觸發條件 |
|----------|------|----------|
| FB Pixel - Base | Facebook Pixel | All Pages |
| FB Pixel - Purchase | 自訂 HTML | 購買完成頁 |
| GA4 - Config | GA4 設定 | All Pages |
| GA4 - Purchase | GA4 事件 | 購買完成 |
| Google Ads - Conversion | Google Ads 轉換 | 購買完成 |

### 3.2 觸發條件

| 觸發條件名稱 | 類型 | 設定 |
|--------------|------|------|
| 購買完成頁 | 網頁瀏覽 | 網址包含 /thankyou |
| 加入購物車 | 自訂事件 | add_to_cart |
| 表單送出 | 表單提交 | Form ID = contact |

---

## 四、測試清單

### 4.1 測試項目

- [ ] Pixel Helper 確認觸發
- [ ] GA4 DebugView 確認
- [ ] 轉換值正確傳送
- [ ] 跨裝置追蹤
- [ ] 結帳流程完整追蹤

### 4.2 常見問題

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| 轉換沒觸發 | 代碼未正確安裝 | 檢查 GTM 發布 |
| 數值為 0 | 變數未正確傳遞 | 檢查 dataLayer |
| 重複觸發 | 頁面重新載入 | 加入去重邏輯 |

---
適用職務：B（數位行銷）
優先級：⭐⭐⭐
