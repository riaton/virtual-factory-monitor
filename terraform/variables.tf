variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-1"
}

variable "project" {
  description = "リソース名・トピックのprefix"
  type        = string
  default     = "vf"
}

# Phase 2 の3系統化はこのリストに追記するだけ:
#   ["sensor-temp-01", "sensor-vib-01", "sensor-status-01"]
# ブリッジ (bridge-01) は購読権限が必要で別ポリシーになるため、このリストには入れない
variable "sensor_thing_names" {
  description = "センサー側 IoT Thing 名の一覧"
  type        = set(string)
  default     = ["sensor-temp-01"]
}
