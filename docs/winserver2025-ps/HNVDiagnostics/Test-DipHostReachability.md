---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DipHostReachability.psm1-help.xml
Module Name: HNVDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hnvdiagnostics/test-diphostreachability?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-DipHostReachability
---

# 测试DipHost的可达性

## 摘要
测试是否可以访问DIP（数据交换点）。

## 语法

```
Test-DipHostReachability [[-OperationId] <String>] [-Dips] <String[]> [[-PayloadSize] <Int32>]
 [<CommonParameters>]
```

## 描述
`Test-DipHostReachability` 这个 cmdlet 用于测试是否可以访问数据中心的 IP（DIP）地址。

## 示例

### 示例 1：测试数字集成电路（DIP）
```
PS C:\> Test-DipHostReachability -Dips "10.123.176.108"
```

这个命令用于测试是否可以访问指定的DIP（数据接口点）。

## 参数

### -Dips
指定一个用于测试的DIP（Digital Integrated Product）数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OperationId
指定操作ID。

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

### -PayloadSize
指定要包含在互联网控制消息协议（ICMP）请求中的有效载荷的大小。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

