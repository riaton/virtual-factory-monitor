"""疑似センサー: 測定値を生成し IoT Core へ MQTT publish する。

Phase 1 (縦貫スライス) で実装:
- MEASURE 環境変数に応じた値生成 (temperature / vibration_rms / machine_state)
- ペイロード: equipment_id, sensor_id, ts(デバイス発生時刻 epoch ms), seq(単調増加), measure, value
  (docs/data-model.md の判断 2-1, 2-3 に対応)
Phase 2 (横展開) で実装:
- 送信バッファ: 断時にローカル蓄積し再接続後に再送 (一点豪華主義)
- 故障モード注入: 欠損・重複送信・時刻ズレ (設定で操作可能に)
"""
# TODO(Phase1)
