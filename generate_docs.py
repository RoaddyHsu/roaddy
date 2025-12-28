#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
弘爺漢堡 AI Agent 指令系統 - 文檔產生器
"""

import json
import csv

def load_data():
    """載入指令資料"""
    with open("/home/user/roaddy/commands_data_v2.json", 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_md(data):
    """產生MD文檔"""
    # 分類順序
    category_order = [
        "行銷企劃", "數位行銷", "數據分析", "視覺設計",
        "專案管理", "經營管理", "客戶經營", "供應商管理",
        "加盟與展覽", "IP授權專項", "溝通協作", "學習系統"
    ]

    # 按分類分組
    categorized = {}
    for item in data:
        cat = item["主分類"]
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(item)

    # 計算統計
    total = len(data)

    md_content = """# 弘爺漢堡 AI Agent 指令系統總覽

> 共計 **{total}** 個指令，依 **{cat_count}** 大類別整理

## 指令統計

| 分類 | 指令數量 |
|------|----------|
""".format(total=total, cat_count=len(category_order))

    for cat in category_order:
        if cat in categorized:
            md_content += f"| {cat} | {len(categorized[cat])} |\n"

    md_content += f"| **總計** | **{total}** |\n\n"

    md_content += """---

## 適用職務說明

| 代碼 | 職務名稱 |
|------|----------|
| M | 主管 |
| A | 行銷企劃 |
| B | 數位行銷 |
| C | 視覺設計 |
| D | 美編專員 |
| E | 團購PM |

---

## 指令清單

"""

    # 編號計數器
    num = 1

    for cat in category_order:
        if cat not in categorized:
            continue

        md_content += f"### {cat}\n\n"
        md_content += "| 編號 | 指令 | 功能說明 | 預期產出 | 次分類 | 標籤 | 框架 | 適用 | 優先級 |\n"
        md_content += "|------|------|----------|----------|--------|------|------|------|--------|\n"

        for item in categorized[cat]:
            # 簡化適用職務顯示
            roles = item["適用"]
            if "M（主管）" in roles:
                roles = roles.replace("M（主管）", "M")
            if "A（行銷企劃）" in roles:
                roles = roles.replace("A（行銷企劃）", "A")
            if "B（數位行銷）" in roles:
                roles = roles.replace("B（數位行銷）", "B")
            if "C（視覺設計）" in roles:
                roles = roles.replace("C（視覺設計）", "C")
            if "D（美編專員）" in roles:
                roles = roles.replace("D（美編專員）", "D")
            if "E（團購PM）" in roles:
                roles = roles.replace("E（團購PM）", "E")
            roles = roles.replace("、", ",")

            md_content += f"| {num} | `{item['指令']}` | {item['功能說明']} | {item['預期產出']} | {item['次分類']} | {item['標籤']} | {item['框架']} | {roles} | {item['優先級']} |\n"
            num += 1

        md_content += "\n"

    md_content += """---

## 快速導覽

### 依標籤分類

- **產生器**：自動產出完整內容
- **分析器**：進行數據或策略分析
- **規劃器**：制定計畫與排程
- **優化器**：改善既有內容
- **設計器**：設計視覺或互動機制
- **檢核表**：檢查清單工具

### 依框架分類

| 框架 | 適用指令 |
|------|----------|
| AIDA | /aida |
| FAB | /fab |
| PAS | /pas |
| SWOT | /swot |
| OKR | /okr |
| RACI | /raci |
| RFM | /rfm |
| AARRR | /adfunnel, /funnel |
| BSC | /bsc, /storekpi |

---

*文檔產生時間：2024年*
*弘爺漢堡 AI Agent 系統 v2.0*
"""

    return md_content

def generate_csv(data):
    """產生CSV文檔"""
    rows = []
    num = 1

    category_order = [
        "行銷企劃", "數位行銷", "數據分析", "視覺設計",
        "專案管理", "經營管理", "客戶經營", "供應商管理",
        "加盟與展覽", "IP授權專項", "溝通協作", "學習系統"
    ]

    # 按分類分組
    categorized = {}
    for item in data:
        cat = item["主分類"]
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(item)

    for cat in category_order:
        if cat not in categorized:
            continue
        for item in categorized[cat]:
            # 簡化適用職務
            roles = item["適用"]
            if "M（主管）" in roles:
                roles = roles.replace("M（主管）", "M")
            if "A（行銷企劃）" in roles:
                roles = roles.replace("A（行銷企劃）", "A")
            if "B（數位行銷）" in roles:
                roles = roles.replace("B（數位行銷）", "B")
            if "C（視覺設計）" in roles:
                roles = roles.replace("C（視覺設計）", "C")
            if "D（美編專員）" in roles:
                roles = roles.replace("D（美編專員）", "D")
            if "E（團購PM）" in roles:
                roles = roles.replace("E（團購PM）", "E")
            roles = roles.replace("、", ",")

            rows.append({
                "編號": num,
                "指令": item["指令"],
                "功能說明": item["功能說明"],
                "預期產出": item["預期產出"],
                "主分類": item["主分類"],
                "次分類": item["次分類"],
                "標籤": item["標籤"],
                "框架": item["框架"],
                "適用": roles,
                "優先級": item["優先級"]
            })
            num += 1

    return rows

def main():
    # 載入資料
    data = load_data()
    print(f"載入 {len(data)} 個指令")

    # 產生MD
    md_content = generate_md(data)
    with open("/home/user/roaddy/指令系統總覽.md", 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("已產生: 指令系統總覽.md")

    # 產生CSV (UTF-8 BOM for Excel)
    csv_rows = generate_csv(data)
    with open("/home/user/roaddy/指令系統清單.csv", 'w', encoding='utf-8-sig', newline='') as f:
        fieldnames = ["編號", "指令", "功能說明", "預期產出", "主分類", "次分類", "標籤", "框架", "適用", "優先級"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)
    print("已產生: 指令系統清單.csv")

    print("\n完成！")

if __name__ == "__main__":
    main()
