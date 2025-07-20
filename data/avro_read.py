import avro.io
import avro.datafile
import pprint
import json

filename = "snap-1753000744856000000-2ca17373-0237-4d57-ab33-767b999de5be.avro"

# ファイルをバイナリモードで読み込む
with open(filename, "rb") as f:
    # リーダーを作成
    reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())

    # データを取得。dict型で取得できる
    for data in reader:
        pprint.pprint(data)

    # スキーマを取得
    schema_str = reader.meta['avro.schema']
    schema_json = json.loads(schema_str)
    pprint.pprint(schema_json)