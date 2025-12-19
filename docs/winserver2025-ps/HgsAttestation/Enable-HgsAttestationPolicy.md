---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/enable-hgsattestationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-HgsAttestationPolicy
---

# 启用 HGS 证书政策（Enable-HgsAttestationPolicy）

## 摘要
在 HGS 中启用认证策略。

## 语法

```
Enable-HgsAttestationPolicy [-Name] <String> [-PolicyVersion <PolicyVersion>] [-Stage] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Enable-HgsAttestationPolicy` cmdlet 可以在 Host Guardian Service (HGS) 中启用一种认证策略。请通过名称指定要启用的策略。

## 示例

### 示例 1：启用某项策略
```
PS C:\> Enable-HgsAttestationPolicy -Name "BaselineTpmPolicy16"
```

此命令启用了名为 BaselineTpmPolicy16 的认证策略。该策略之前是被禁用的。运行此命令后，任何符合该策略要求的受保护主机都可以获取新的认证证书。

## 参数

### -Name
指定该cmdlet所启用的策略的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -PolicyVersion
保留以供将来使用。

```yaml
Type: PolicyVersion
Parameter Sets: (All)
Aliases:
Accepted values: None, PolicyVersion1503, PolicyVersion1704

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Stage
保留以供将来使用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### AttestationPolicyInfo
此 cmdlet 返回一个 **AttestationPolicyInfo** 对象。

## 备注

## 相关链接

[Disable-HgsAttestationPolicy](./Disable-HgsAttestationPolicy.md)

[Get-HgsAttestationPolicy](./Get-HgsAttestationPolicy.md)

[Remove-HgsAttestationPolicy](./Remove-HgsAttestationPolicy.md)

