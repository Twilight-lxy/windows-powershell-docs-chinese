---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Client.PowerShell.dll-Help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/get-hgsattestationbaselinepolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-HgsAttestationBaselinePolicy
---

# Get-HgsAttestationBaselinePolicy

## 摘要
生成一个认证基线策略（attestation baseline policy）。

## 语法

### 文件（默认设置）
```
Get-HgsAttestationBaselinePolicy -Path <String> [-Force] [-SkipValidation] [<CommonParameters>]
```

### 控制台
```
Get-HgsAttestationBaselinePolicy [-Console] [-SkipValidation] [<CommonParameters>]
```

## 描述

`Get-HgsAttestationBaselinePolicy` cmdlet 用于生成一个认证基线策略。您可以使用该策略来配置认证服务。

这个cmdlet从受信任平台模块（TPM）的“受信任计算组”（Trusted Computing Group）日志中获取上一次完全启动时的原始数据，从而得到一个表示认证基线策略的字节数组。

请确保在配置良好的主机上运行此 cmdlet。

## 示例

### 示例 1：生成一个基线策略

```powershell
Get-HgsAttestationBaselinePolicy -Path 'C:\Logs\AttestationBaselinePolicy001' -Force
```

该命令生成一个字节数组，用于表示文件`C:\Logs\AttestationBaselinePolicy001`中的基线策略。

## 参数

### -Console

表示此cmdlet在控制台模式下运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: Console
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

表示此 cmdlet 会覆盖由 **Output** 对象指定的现有文件。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: File
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path

指定一个文件路径。此 cmdlet 会将策略写入该参数所指定的文件中。

```yaml
Type: System.String
Parameter Sets: File
Aliases: FilePath

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipValidation

表示此 cmdlet 将跳过验证步骤。

```yaml
Type: System.Diagnostics.Switch
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Byte[]

## 备注

## 相关链接
