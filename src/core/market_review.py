# -*- coding: utf-8 -*-
"""
===================================
股票智能分析系统 - 大盘复盘模块（支持 A 股 / 美股）
===================================

职责：
1. 根据 MARKET_REVIEW_REGION 配置选择市场区域（cn / us / both）
2. 执行大盘复盘分析并生成复盘报告
3. 保存和发送复盘报告
"""

import logging
from datetime import datetime
from typing import Optional

from src.config import get_config
from src.notification import NotificationService
from src.market_analyzer import MarketAnalyzer
from src.search_service import SearchService
from src.analyzer import GeminiAnalyzer


def _market_review_title() -> str:
    """Return translated market review title based on REPORT_LANGUAGE."""
    lang = getattr(get_config(), 'report_language', 'en')
    return {'zh': '大盘复盘', 'vi': 'Tổng kết thị trường', 'en': 'Market Review'}.get(lang, 'Market Review')


logger = logging.getLogger(__name__)


def run_market_review(
    notifier: NotificationService,
    analyzer: Optional[GeminiAnalyzer] = None,
    search_service: Optional[SearchService] = None,
    send_notification: bool = True,
    merge_notification: bool = False,
    override_region: Optional[str] = None,
) -> Optional[str]:
    """
    执行大盘复盘分析

    Args:
        notifier: 通知服务
        analyzer: AI分析器（可选）
        search_service: 搜索服务（可选）
        send_notification: 是否发送通知
        merge_notification: 是否合并推送（跳过本次推送，由 main 层合并个股+大盘后统一发送，Issue #190）
        override_region: 覆盖 config 的 market_review_region（Issue #373 交易日过滤后有效子集）

    Returns:
        复盘报告文本
    """
    logger.info("Starting market review analysis...")
    config = get_config()
    region = (
        override_region
        if override_region is not None
        else (getattr(config, 'market_review_region', 'cn') or 'cn')
    )
    if region not in ('cn', 'us', 'both'):
        region = 'cn'

    try:
        if region == 'both':
            # 顺序执行 A 股 + 美股，合并报告
            cn_analyzer = MarketAnalyzer(
                search_service=search_service, analyzer=analyzer, region='cn'
            )
            us_analyzer = MarketAnalyzer(
                search_service=search_service, analyzer=analyzer, region='us'
            )
            logger.info("Generating A-Share market review report...")
            cn_report = cn_analyzer.run_daily_review()
            logger.info("Generating US market review report...")
            us_report = us_analyzer.run_daily_review()
            review_report = ''
            _title = _market_review_title()
            if cn_report:
                review_report = f"# {_title} (A-Share)\n\n{cn_report}"
            if us_report:
                if review_report:
                    review_report += f"\n\n---\n\n> US {_title}\n\n"
                review_report += f"# {_title} (US)\n\n{us_report}"
            if not review_report:
                review_report = None
        else:
            market_analyzer = MarketAnalyzer(
                search_service=search_service,
                analyzer=analyzer,
                region=region,
            )
            review_report = market_analyzer.run_daily_review()
        
        if review_report:
            # 保存报告到文件
            date_str = datetime.now().strftime('%Y%m%d')
            report_filename = f"market_review_{date_str}.md"
            _title = _market_review_title()
            filepath = notifier.save_report_to_file(
                f"# 🎯 {_title}\n\n{review_report}",
                report_filename
            )
            logger.info(f"Market review report saved: {filepath}")

            if merge_notification and send_notification:
                logger.info("Merge mode: skipping market review push, will send combined later")
            elif send_notification and notifier.is_available():
                report_content = f"🎯 {_title}\n\n{review_report}"

                success = notifier.send(report_content, email_send_to_all=True)
                if success:
                    logger.info("大盘复盘推送成功")
                else:
                    logger.warning("大盘复盘推送失败")
            elif not send_notification:
                logger.info("已跳过推送通知 (--no-notify)")
            
            return review_report
        
    except Exception as e:
        logger.error(f"Market review analysis failed: {e}")
    
    return None
