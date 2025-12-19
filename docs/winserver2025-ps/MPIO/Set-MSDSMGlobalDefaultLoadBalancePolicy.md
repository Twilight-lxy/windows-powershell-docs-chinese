---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Mpio-help.xml
Module Name: MPIO
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/mpio/set-msdsmglobaldefaultloadbalancepolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-MSDSMGlobalDefaultLoadBalancePolicy
---

# 设置 MSDSMGlobalDefaultLoadBalancePolicy

## 摘要
为 MPIO 设备设置默认的负载均衡策略。

## 语法

```
Set-MSDSMGlobalDefaultLoadBalancePolicy [-Policy] <String> [<CommonParameters>]
```

## 描述
`Set-MSDSMGlobalDefaultLoadBalancePolicy` cmdlet 用于设置 Microsoft 多路径输入/输出（MPIO）设备的默认负载均衡策略。Microsoft 设备特定模块（MSDSM）仅在您设置该策略后，针对其管理的设备应用此策略。

使用 `Get-MSDSMGlobalDefaultLoadBalancePolicy` cmdlet 来查看当前的默认策略。

## 示例

### 示例 1：将轮询（round-robin）设置为默认策略
```
PS C:\> Set-MSDSMGlobalLoadBalancePolicy -Policy RR
```

此命令将默认的负载均衡策略设置为轮询（round robin）。

### 示例 2：清除默认策略
```
PS C:\> Set-MSDSMGlobalLoadBalancePolicy -Policy None
```

这个命令会清除当前配置的所有默认负载均衡策略。

## 参数

### -Policy
为负载均衡策略指定一个默认值。该参数的可接受值为：

- None.
Clears any currently configured default load balance policy.
- FOO.
Fail Over Only.
- RR.
Round Robin.
- LQD.
Least Queue Depth.
- LB.
Least Blocks.

```yaml
Type: String
Parameter Sets: (All)
Aliases:
Accepted values: None, FOO, RR, LQD, LB

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

## 备注

## 相关链接

[Get-MSDSMGlobalDefaultLoadBalancePolicy](./Get-MSDSMGlobalDefaultLoadBalancePolicy.md)

