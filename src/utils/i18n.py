# -*- coding: utf-8 -*-
"""Central i18n utility for stock analysis reports."""
from typing import Dict, Any

I18N_DICT: Dict[str, Dict[str, str]] = {
    # UI Labels
    "dashboard_title": {"zh": "决策仪表盘", "en": "Decision Dashboard", "vi": "Bảng Quyết Định"},
    "analyzed": {"zh": "共分析", "en": "Analyzed", "vi": "Đã phân tích"},
    "stocks_unit": {"zh": "只股票", "en": "stock(s)", "vi": "cổ phiếu"},
    "buy": {"zh": "买入", "en": "Buy", "vi": "Mua"},
    "watch": {"zh": "观望", "en": "Watch", "vi": "Theo dõi"},
    "sell": {"zh": "卖出", "en": "Sell", "vi": "Bán"},
    "summary_title": {"zh": "分析结果摘要", "en": "Summary", "vi": "Tóm tắt"},
    "score": {"zh": "评分", "en": "Score", "vi": "Điểm"},
    "news_section": {"zh": "重要信息速览", "en": "Key Intelligence", "vi": "Tin tức quan trọng"},
    "sentiment": {"zh": "舆情情绪", "en": "Sentiment", "vi": "Cảm xúc thị trường"},
    "earnings": {"zh": "业绩预期", "en": "Earnings Outlook", "vi": "Triển vọng lợi nhuận"},
    "risks": {"zh": "风险警报", "en": "Risk Alerts", "vi": "Cảnh báo rủi ro"},
    "catalysts": {"zh": "利好催化", "en": "Positive Catalysts", "vi": "Điểm tích cực"},
    "latest_news": {"zh": "最新动态", "en": "Latest News", "vi": "Tin mới nhất"},
    "core_conclusion": {"zh": "核心结论", "en": "Core Conclusion", "vi": "Kết luận cốt lõi"},
    "one_sentence": {"zh": "一句话决策", "en": "Key Decision", "vi": "Quyết định then chốt"},
    "time_sensitivity": {"zh": "时效性", "en": "Time Sensitivity", "vi": "Độ khẩn cấp"},
    "position_table_header": {"zh": "持仓情况", "en": "Position", "vi": "Vị thế"},
    "advice_header": {"zh": "操作建议", "en": "Advice", "vi": "Khuyến nghị"},
    "no_position": {"zh": "空仓者", "en": "No Position", "vi": "Chưa có vị thế"},
    "has_position": {"zh": "持仓者", "en": "Has Position", "vi": "Đang giữ cổ phiếu"},
    "data_section": {"zh": "数据透视", "en": "Data Analysis", "vi": "Phân tích dữ liệu"},
    "battle_section": {"zh": "作战计划", "en": "Action Plan", "vi": "Kế hoạch hành động"},
    "sniper_title": {"zh": "狙击点位", "en": "Entry/Exit Points", "vi": "Điểm vào/ra"},
    "ideal_buy": {"zh": "理想买入点", "en": "Ideal Buy", "vi": "Điểm mua lý tưởng"},
    "secondary_buy": {"zh": "次优买入点", "en": "Alt Buy", "vi": "Điểm mua thứ 2"},
    "stop_loss": {"zh": "止损位", "en": "Stop Loss", "vi": "Cắt lỗ"},
    "take_profit": {"zh": "目标位", "en": "Target", "vi": "Mục tiêu"},
    "position_strategy": {"zh": "仓位建议", "en": "Position Sizing", "vi": "Tỷ trọng vốn"},
    "checklist": {"zh": "检查清单", "en": "Checklist", "vi": "Danh sách kiểm tra"},
    "generated_at": {"zh": "报告生成时间", "en": "Generated", "vi": "Thời gian tạo"},
    "model_used": {"zh": "分析模型", "en": "Model", "vi": "Mô hình AI"},
    "current_price": {"zh": "当前价", "en": "Price", "vi": "Giá hiện tại"},
    "bias_rate": {"zh": "乖离率(MA5)", "en": "Bias(MA5)", "vi": "Lệch giá(MA5)"},
    "support": {"zh": "支撑位", "en": "Support", "vi": "Hỗ trợ"},
    "resistance": {"zh": "压力位", "en": "Resistance", "vi": "Kháng cự"},
    "volume": {"zh": "量能", "en": "Volume", "vi": "Khối lượng"},
    "chip": {"zh": "筹码", "en": "Chip Structure", "vi": "Cấu trúc phân bổ"},
    "profit_ratio": {"zh": "获利比例", "en": "Profit Ratio", "vi": "Tỷ lệ lãi"},
    "avg_cost": {"zh": "平均成本", "en": "Avg Cost", "vi": "Giá vốn TB"},
    "concentration": {"zh": "集中度", "en": "Concentration", "vi": "Tập trung"},

    # Values
    "hold": {"zh": "持有", "en": "Hold", "vi": "Giữ"},
    "sideways": {"zh": "震荡", "en": "Sideways", "vi": "Đi ngang"},
    "medium": {"zh": "中", "en": "Medium", "vi": "Trung bình"},
    "low": {"zh": "低", "en": "Low", "vi": "Thấp"},
    "high": {"zh": "高", "en": "High", "vi": "Cao"},
    "wait": {"zh": "观望", "en": "Watch/Wait", "vi": "Theo dõi"},
    "reduce_pos": {"zh": "减仓", "en": "Reduce", "vi": "Giảm vị thế"},
    "add_pos": {"zh": "加仓", "en": "Add Position", "vi": "Tăng vị thế"},
    "strong_buy": {"zh": "强烈买入", "en": "Strong Buy", "vi": "Mua mạnh"},
    "strong_sell": {"zh": "强烈卖出", "en": "Strong Sell", "vi": "Bán mạnh"},
    
    # States
    "ma_alignment": {"zh": "均线排列", "en": "MA Alignment", "vi": "Xếp hạng MA"},
    "bullish_alignment": {"zh": "多头排列", "en": "Bullish Alignment", "vi": "Xu hướng tăng"},
    "bearish_alignment": {"zh": "空头排列", "en": "Bearish Alignment", "vi": "Xu hướng giảm"},
    "entangled": {"zh": "均线缠绕", "en": "Entangled", "vi": "Xoắn nhau"},
    "safe": {"zh": "安全", "en": "Safe", "vi": "An toàn"},
    "warning": {"zh": "警戒", "en": "Warning", "vi": "Cảnh báo"},
    "danger": {"zh": "危险", "en": "Danger", "vi": "Nguy hiểm"},
    "yes": {"zh": "是", "en": "Yes", "vi": "Có"},
    "no": {"zh": "否", "en": "No", "vi": "Không"},

    # Messages
    "analysis_error": {"zh": "分析过程出错", "en": "Analysis Error", "vi": "Lỗi phân tích"},
    "analysis_failed": {"zh": "分析失败，请稍后重试", "en": "Analysis failed, please retry", "vi": "Phân tích thất bại, vui lòng thử lại"},
    "to_be_added": {"zh": "待补充", "en": "TBD", "vi": "Sẽ bổ sung"},
    "no_analysis": {"zh": "无分析结果", "en": "No Results", "vi": "Không có kết quả"},
    "analysis_done": {"zh": "分析完成", "en": "Analysis Complete", "vi": "Đã phân tích xong"},
    "agent_failed": {"zh": "Agent 未能生成有效的决策仪表盘", "en": "Agent failed to generate dashboard", "vi": "Agent không thể tạo bảng quyết định"},
    "week_sensitivity": {"zh": "本周内", "en": "Within this week", "vi": "Trong tuần này"},

    # Units
    "unit_billion_shares": {"zh": "亿股", "en": "B shares", "vi": "Tỷ cp"},
    "unit_million_shares": {"zh": "万股", "en": "M shares", "vi": "Triệu cp"},
    "unit_shares": {"zh": "股", "en": "shares", "vi": "cp"},
    "unit_billion_yuan": {"zh": "亿元", "en": "B CNY", "vi": "Tỷ VNĐ/CNY"},
    "unit_million_yuan": {"zh": "万元", "en": "M CNY", "vi": "Triệu VNĐ/CNY"},
    "unit_yuan": {"zh": "元", "en": "CNY", "vi": "VNĐ/CNY"},

    # Strategy Framework (Market Recap)
    "market_review_title": {"zh": "Tổng kết thị trường", "en": "Market Review", "vi": "Tổng kết thị trường"},
    "strategy_framework": {"zh": "策略框架", "en": "Strategy Framework", "vi": "Khung chiến lược"},
    "trend_regime": {"zh": "趋势结构", "en": "Trend Regime", "vi": "Cấu trúc xu hướng"},
    "capital_sentiment": {"zh": "资金情绪", "en": "Capital Sentiment", "vi": "Tâm lý dòng tiền"},
    "main_sectors": {"zh": "主线板块", "en": "Main Sectors", "vi": "Nhóm ngành chính"},
}

def _t(key: str, lang: str = "en") -> str:
    """Translate a key to the target language."""
    translations = I18N_DICT.get(key, {})
    return translations.get(lang, translations.get("en", key))
