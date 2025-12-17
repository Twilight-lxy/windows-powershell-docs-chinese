---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfstrustedfederationpartner?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsTrustedFederationPartner
---

# 添加 AdFS 可信赖的联邦合作伙伴

## 摘要
为 AD FS 中的可信联盟合作伙伴添加配置设置。

## 语法

```
Add-AdfsTrustedFederationPartner [-Name] <String> [-FederationPartnerHostName] <Uri> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsTrustedFederationPartner` cmdlet 用于添加一个受此 Active Directory Federation Services (AD FS) 实例信任的联合伙伴。

## 示例

## 参数

### -FederationPartnerHostName
指定联盟合作伙伴的 URI（统一资源定位符）。

```yaml
Type: Uri
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为联邦合作伙伴指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Get-AdfsTrustedFederationPartner](./Get-AdfsTrustedFederationPartner.md)

[Remove-AdfsTrustedFederationPartner](./Remove-AdfsTrustedFederationPartner.md)

[Set-AdfsTrustedFederationPartner](./Set-AdfsTrustedFederationPartner.md)

