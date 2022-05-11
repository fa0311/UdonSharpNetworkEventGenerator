# UdonSharpNetworkEventGen
Udon#のNetworkEventを自動生成します<br>
ジョークプログラムではありません

## 使い方
```console
python UdonSharpNetworkEventGen.py Name 1000 -o Output.cs
```

出力
```Output.cs
public void NetworkEventName0(){
    NetworkEventName(0);
}
            .
            .
            .

public void NetworkEventName999(){
    NetworkEventName(999);
}
```

詳しい使い方は`--help`