---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/remove-hgsattestationpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-HgsAttestationPolicy
---

# 移除HGS证明政策（Remove-HgsAttestationPolicy）

## 摘要
从HGS中删除某个认证策略。

## 语法

```
Remove-HgsAttestationPolicy [-Name] <String> [-PolicyVersion <PolicyVersion>] [-Stage] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-HgsAttestationPolicy` cmdlet 用于从 Host Guardian Service (HGS) 中删除一个认证策略。需要通过名称来指定要删除的策略。

## 示例

### 示例 1：删除策略
```
PS C:\> Remove-HgsAttestationPolicy -Name "BaselineTpmPolicy16"
```

此命令会删除名为 BaselineTpmPolicy16 的认证策略。

## 参数

### -Name
指定此 cmdlet 将要删除的策略的名称。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Disable-HgsAttestationPolicy](./Disable-HgsAttestationPolicy.md)

[Enable-HgsAttestationPolicy](./Enable-HgsAttestationPolicy.md)

[Get-HgsAttestationPolicy](./Get-HgsAttestationPolicy.md)

