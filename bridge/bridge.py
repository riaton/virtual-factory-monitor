"""ブリッジ: IoT Core を MQTT 購読し InfluxDB へ書き込む常駐サービス。

Phase 1 で実装:
- 購読トピックからペイロード受信 → InfluxDB へポイント書き込み
- ポイント時刻はペイロードの ts (デバイス発生時刻) を採用 = 重複吸収のキー (ADR-001, data-model 2-1)
- ingested_at フィールドに受信時刻を併記 (遅延・時刻ズレの観測量)
- 独自の X.509 証明書を持つ IoT Thing として接続 (デバイス3 + 購読側1)
"""
# TODO(Phase1)
