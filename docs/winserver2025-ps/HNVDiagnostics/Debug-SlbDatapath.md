---
description: 使用这个主题来借助 Windows PowerShell 帮助管理 Windows 和 Windows Server 技术。
external help file: SlbDatapathTracing.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/debug-slbdatapath?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Debug-SlbDatapath
---

# 调试 SlbDataPath

## 摘要
从SLB MUX和DIP主机收集日志。

## 语法

```
Debug-SlbDatapath [[-OperationId] <String>] [-SourceIP] <String> [-TargetVIP] <String> [-PortNumber] <UInt16>
 [-Muxes] <Hashtable[]> [-Dips] <Hashtable[]> [[-TraceFolderPath] <String>] [<CommonParameters>]
```

## 描述
`Debug-SlbDatapath` cmdlet 用于收集来自软件负载均衡（SLB）多路复用器（MUX）以及数据包在指定流中经过的动态 IP 地址（DIP）主机的日志。

## 示例

### 示例 1：获取 MUX 和 DIP 主机的日志
```
PS C:\> for ($mux in $VipHostMapping.MuxList) {
    $secpasswd = ConvertTo-SecureString <plaintext password> -AsPlainText -Force
    $creds = New-Object System.Management.Automation.PSCredential (<username>, $secpasswd)
    $mux.Credentials = $creds
}
PS C:\> for ($dip in $VipHostMapping.DIPHosts) {
    $secpasswd = ConvertTo-SecureString <plaintext password> -AsPlainText -Force
    $creds = New-Object System.Management.Automation.PSCredential (<username>, $secpasswd)
    $dip.HostInfo.Credentials = $creds
}
PS C:\> $out = Debug-SlbDatapath -OperationId "1" -SourceIP "10.123.176.108" -TargetVIP "10.123.177.110" -PortNumber 445 -Muxes $VipHostMapping.MuxList -Dips $VipHostMapping.DIPHosts
```

第一个命令创建了一个包含MUX凭据的**PSCredential**对象，然后将其存储在$mux.Credentials变量中。

第二个命令创建一个包含DIP主机凭据的**PSCredential**对象，然后将其存储在$dip.HostInfo.Credentials变量中。

第三个命令会从指定的源IP地址发送测试流量，目标是与指定VIP端点进行通信。你可以使用命令 `$out | Format-Custom` 来查看收集到的MUX和DIP日志的路径信息。

## 参数

### -Dips
指定实现被测试虚拟 IP 地址（VIP）端点的设备（DIP）。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Muxes
指定用于对DIP（数字输入端口）进行负载均衡的MUX（多路复用器）。

```yaml
Type: Hashtable[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperationId
指定一个操作ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PortNumber
指定此操作所测试的VIP端点的端口号。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourceIP
指定源节点的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetVIP
指定本次操作所要测试的VIP的IP地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TraceFolderPath
指定跟踪日志文件夹的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

