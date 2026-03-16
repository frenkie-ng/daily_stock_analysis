# -*- coding: utf-8 -*-
import os
import logging
from datetime import datetime
from src.config import get_config
from src.utils.i18n import _t

logger = logging.getLogger(__name__)

def print_system_status():
    """Print a localized system status and configuration audit."""
    config = get_config()
    lang = config.report_language
    
    print("=" * 60)
    print(f"🚀 {_t('system_start', lang)}")
    print("=" * 60)
    print(f"⏰ {_t('runtime', lang)}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 {_t('mode', lang)}: {os.getenv('MODE', 'full')}")
    print(f"🌐 {_t('stock', lang)} Language: {lang}")
    print(f"📊 {_t('position_table_header', lang)}: {os.getenv('STOCK_LIST', 'N/A')}")
    print(f"📝 {_t('advice_header', lang)}: {os.getenv('REPORT_TYPE', 'simple')}")
    print("")
    
    print("=" * 60)
    print(f"📋 {_t('config_audit', lang)}")
    print("=" * 60)
    
    # AI Config Check
    ai_configured = any([
        os.getenv("LITELLM_CONFIG"),
        os.getenv("LITELLM_API_KEY"),
        os.getenv("GEMINI_API_KEY"),
        os.getenv("OPENAI_API_KEY")
    ])
    ai_status = "✅" if ai_configured else "❌"
    print(f"AI Configuration: {ai_status}")
    
    # Notification Check
    notif_configured = any([
        os.getenv("DISCORD_WEBHOOK_URL"),
        os.getenv("TELEGRAM_BOT_TOKEN"),
        os.getenv("WECHAT_WEBHOOK_URL"),
        os.getenv("FEISHU_WEBHOOK_URL")
    ])
    notif_status = "✅" if notif_configured else "⚪"
    print(f"Notification Channels: {notif_status}")
    print("=" * 60)
    print("")

if __name__ == "__main__":
    print_system_status()
