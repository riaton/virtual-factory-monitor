# terraform/ — タスク1: 適用と疎通確認

## 適用
```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars   # 必要なら region を変更
terraform init
terraform validate
terraform plan
terraform apply
```
成功すると `../certs/sensor-temp-01/` に certificate.pem / private.key / AmazonRootCA1.pem が置かれ、
`../.env` に IOT_ENDPOINT が書き出される。

## 疎通確認 (センサー実装前の仮送信)
1. AWS コンソール → IoT Core → MQTT テストクライアント → トピック `vf/#` を購読
2. 手元から 1 メッセージ送る (mosquitto_pub の例):
```bash
source ../.env
mosquitto_pub \
  --cafile ../certs/sensor-temp-01/AmazonRootCA1.pem \
  --cert   ../certs/sensor-temp-01/certificate.pem \
  --key    ../certs/sensor-temp-01/private.key \
  -h "$IOT_ENDPOINT" -p 8883 \
  -i sensor-temp-01 \
  -t vf/machine-01/sensor-temp-01 \
  -m '{"hello":"vf"}'
```
3. コンソールの購読画面にメッセージが表示されたら疎通完了

### 検証ポイント (ポリシーの縛りが効いていることの確認)
- `-i` を `sensor-temp-01` 以外にすると**接続拒否**される (クライアント ID = Thing 名の縛り)
- `-t` を `vf/machine-01/other-sensor` にすると**切断される** (自分名義のトピックのみ publish 可)
この 2 つの「失敗すること」の確認まで含めて疎通確認完了とする。

## コミット前の受け入れ試験
`git status` に certs/・.env・tfstate が**一切表示されない**こと。

## 撤収
```bash
terraform destroy
```
