"""チャット CLI: InfluxDB にクエリし、結果を Bedrock に渡して設備の異常を日本語で説明する。

Phase 3 で実装 (ADR-003):
- InfluxDB クエリ (直近の測定値・seqギャップ・遅延)
- Bedrock 呼び出しとプロンプト設計 (試行 4h の主戦場)
起動: docker compose run chat
"""
# TODO(Phase3)
