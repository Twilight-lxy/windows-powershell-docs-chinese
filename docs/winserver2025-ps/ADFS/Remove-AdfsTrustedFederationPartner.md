---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfstrustedfederationpartner?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsTrustedFederationPartner
---

# 删除 AdfsTrustedFederationPartner

## 摘要
从 Active Directory Federation Services (AD FS) 中移除一个受信任的联盟合作伙伴。

## 语法

### 名称（默认值）
```
Remove-AdfsTrustedFederationPartner [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### FederationPartnerHostName
```
Remove-AdfsTrustedFederationPartner [-TargetFederationPartnerHostName] <Uri> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject
```
Remove-AdfsTrustedFederationPartner [-TargetFederationPartner] <AdfsTrustedFederationPartner> [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsTrustedFederationPartner` cmdlet 用于移除被该 Active Directory Federation Services (AD FS) 实例信任的联合伙伴。

## 示例

## 参数

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetFederationPartner
指定一个需要移除的联盟伙伴。

```yaml
Type: AdfsTrustedFederationPartner
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetFederationPartnerHostName
指定要删除的联合伙伴（federation partner）的 URI。

```yaml
Type: Uri
Parameter Sets: FederationPartnerHostName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定要移除的联盟合作伙伴的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsTrustedFederationPartner](./Add-AdfsTrustedFederationPartner.md)

[Get-AdfsTrustedFederationPartner](./Get-AdfsTrustedFederationPartner.md)

[Set-AdfsTrustedFederationPartner](./Set-AdfsTrustedFederationPartner.md)

