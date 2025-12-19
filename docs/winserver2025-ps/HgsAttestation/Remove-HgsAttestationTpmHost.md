---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.RemoteAttestation.Server.PowerShell.dll-Help.xml
Module Name: HgsAttestation
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsattestation/remove-hgsattestationtpmhost?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-HgsAttestationTpmHost
---

# 删除 HGS Attestation TpmHost

## 摘要
从HGS（Hardware Security Module）的认证服务中移除使用了TPM 2.0技术的受保护主机。

## 语法

```
Remove-HgsAttestationTpmHost [-Name] <String> [-PolicyVersion <PolicyVersion>] [-Stage] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-HgsAttestationTpmHost` cmdlet 用于将受保护的主机从 Host Guardian Service (HGS) 的 Attestation 服务中移除。该 cmdlet 适用于那些配备了 Trusted Platform Module (TPM) 2.0 硬件，并且是通过 `Add-HgsAttestationTpmHost` cmdlet 添加到系统中的主机。

## 示例

### 示例 1：移除一个 TPM 主机
```
PS C:\> Remove-HgsAttestationTpmHost -Name "TpmHost21"
```

此命令会将名为 TpmHost21 的主机从认证服务中删除。

## 参数

### -Name
指定该命令行参数要从认证服务中删除的保护主机的友好名称。

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
在运行cmdlet之前，会提示您进行确认。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-HgsAttestationTpmHost](./Add-HgsAttestationTpmHost.md)

[Get-HgsAttestationTpmHost](./Get-HgsAttestationTpmHost.md)

