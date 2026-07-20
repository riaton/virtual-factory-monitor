output "iot_endpoint" {
  description = "IoT Core データエンドポイント (アカウント固有。公開文書に載せない)"
  value       = data.aws_iot_endpoint.data.endpoint_address
}

output "provisioned_things" {
  value = [for t in aws_iot_thing.sensor : t.name]
}
