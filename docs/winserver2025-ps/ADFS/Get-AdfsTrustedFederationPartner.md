---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfstrustedfederationpartner?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsTrustedFederationPartner
---

# Get-AdfsTrustedFederationPartner

## 摘要
在 Active Directory Federation Services (AD FS) 中找到一个值得信赖的联合伙伴。

## 语法

### 名称（默认值）
```
Get-AdfsTrustedFederationPartner [[-Name] <String[]>] [<CommonParameters>]
```

### FederationPartnerHostName
```
Get-AdfsTrustedFederationPartner [-FederationPartnerHostName] <Uri[]> [<CommonParameters>]
```

## 描述
`Get-AdfsTrustedFederationPartner` cmdlet 可以获取受此 Active Directory Federation Services (AD FS) 实例信任的联合伙伴信息。

## 示例

## 参数

### -FederationPartnerHostName
指定一个包含联合合作伙伴 URI 的数组，以便获取这些合作伙伴的相关信息。

```yaml
Type: Uri[]
Parameter Sets: FederationPartnerHostName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个联邦合作伙伴名称数组，用于获取相关信息。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsTrustedFederationPartner](./Add-AdfsTrustedFederationPartner.md)

[Remove-AdfsTrustedFederationPartner](./Remove-AdfsTrustedFederationPartner.md)

[Set-AdfsTrustedFederationPartner](./Set-AdfsTrustedFederationPartner.md)

