"""
Google Search API 客戶端
"""

import os
import requests
from typing import List, Dict, Optional
from ..utils.logger import logger


class GoogleSearchClient:
    """Google Search API 客戶端"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        search_engine_id: Optional[str] = None,
    ):
        """
        初始化 Google Search 客戶端

        Args:
            api_key: Google API 金鑰
            search_engine_id: 搜尋引擎 ID
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.search_engine_id = search_engine_id or os.getenv(
            "GOOGLE_SEARCH_ENGINE_ID"
        )

        if not self.api_key or not self.search_engine_id:
            logger.warning(
                "Google Search API 未配置，請設定 GOOGLE_API_KEY 和 GOOGLE_SEARCH_ENGINE_ID"
            )

        logger.info("Google Search 客戶端初始化完成")

    def search(
        self,
        query: str,
        num: int = 10,
        start: int = 1,
        search_type: Optional[str] = None,
    ) -> List[Dict[str, str]]:
        """
        執行搜尋

        Args:
            query: 搜尋關鍵字
            num: 返回結果數量
            start: 起始位置
            search_type: 搜尋類型（None=網頁, "image"=圖片）

        Returns:
            搜尋結果列表
        """
        if not self.api_key or not self.search_engine_id:
            logger.error("Google Search API 未配置")
            return []

        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": self.api_key,
                "cx": self.search_engine_id,
                "q": query,
                "num": num,
                "start": start,
            }

            if search_type:
                params["searchType"] = search_type

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            items = data.get("items", [])

            results = []
            for item in items:
                result = {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", ""),
                }

                if search_type == "image":
                    result["image_url"] = item.get("link", "")

                results.append(result)

            logger.info(f"Google 搜尋成功，找到 {len(results)} 個結果")
            return results

        except Exception as e:
            logger.error(f"Google Search API 請求失敗: {e}")
            return []

    def search_news(self, query: str, num: int = 10) -> List[Dict[str, str]]:
        """
        搜尋新聞

        Args:
            query: 搜尋關鍵字
            num: 返回結果數量

        Returns:
            新聞結果列表
        """
        # 在搜尋詞後加上 "news" 來搜尋新聞
        news_query = f"{query} news"
        return self.search(news_query, num=num)

    def search_images(self, query: str, num: int = 10) -> List[Dict[str, str]]:
        """
        搜尋圖片

        Args:
            query: 搜尋關鍵字
            num: 返回結果數量

        Returns:
            圖片結果列表
        """
        return self.search(query, num=num, search_type="image")
